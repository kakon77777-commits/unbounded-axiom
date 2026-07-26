from __future__ import annotations

import math
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy.linalg import eigh, null_space
from scipy.optimize import minimize


def paired_bump_basis(t, radius=3.0, count=24, width_factor=1.2, power=3):
    t = np.asarray(t, dtype=float)
    spacing = radius / (count - 0.5)
    width = width_factor * spacing
    centers = np.linspace(0.0, max(0.0, radius - width), count)

    def bump(x):
        u = x / width
        return np.where(np.abs(u) < 1.0, (1.0 - u*u) ** power, 0.0)

    columns = []
    for index, center in enumerate(centers):
        columns.append(
            bump(t) if index == 0 else bump(t-center) + bump(t+center)
        )
    return np.stack(columns, axis=1), centers, width


def paired_bump_derivative(t, radius=3.0, count=24, width_factor=1.2, power=3):
    t = np.asarray(t, dtype=float)
    spacing = radius / (count - 0.5)
    width = width_factor * spacing
    centers = np.linspace(0.0, max(0.0, radius - width), count)

    def derivative(x):
        u = x / width
        return np.where(
            np.abs(u) < 1.0,
            power * (1.0-u*u) ** (power-1) * (-2.0*u) / width,
            0.0,
        )

    columns = []
    for index, center in enumerate(centers):
        columns.append(
            derivative(t) if index == 0
            else derivative(t-center) + derivative(t+center)
        )
    return np.stack(columns, axis=1)


def trapezoid_weights(size, step):
    weights = np.full(size, step, dtype=float)
    weights[0] = weights[-1] = step / 2.0
    return weights


def fourier_vector(w, t, basis, weights):
    return np.sum(
        weights[:,None] * basis * np.exp(1j*complex(w)*t)[:,None],
        axis=0,
    )


def block_value(w, coefficients, model):
    value = coefficients @ fourier_vector(
        w, model["t"], model["basis"], model["weights"]
    )
    return float(2.0*np.real(value*value))


def block_matrix(w, model, coordinate_map):
    vector = coordinate_map.T @ fourier_vector(
        w, model["t"], model["basis"], model["weights"]
    )
    return 2.0*np.real(np.outer(vector,vector))


def primes_upto(limit):
    if limit < 2:
        return []
    sieve = np.ones(limit+1,dtype=bool)
    sieve[:2] = False
    for prime in range(2,int(limit**0.5)+1):
        if sieve[prime]:
            sieve[prime*prime::prime] = False
    return np.flatnonzero(sieve).astype(int).tolist()


def build_model(radius=3.0, count=24, step=0.01, width_factor=1.2):
    t = np.arange(-radius,radius+step/2,step)
    basis, centers, width = paired_bump_basis(
        t,radius,count,width_factor
    )
    derivative = paired_bump_derivative(
        t,radius,count,width_factor
    )
    weights = trapezoid_weights(len(t),step)

    c0 = basis.T @ (weights[:,None]*basis)
    derivative_matrix = derivative.T @ (weights[:,None]*derivative)
    g0 = fourier_vector(0.0,t,basis,weights).real
    endpoint = fourier_vector(0.5j,t,basis,weights).real

    core = np.zeros((count,count))
    shifts = np.arange(0.0,2.0*radius+step/2,step)
    for index,x in enumerate(shifts):
        shifted,_,_ = paired_bump_basis(
            t-x,radius,count,width_factor
        )
        correlation = basis.T @ (weights[:,None]*shifted)
        correlation = (correlation+correlation.T)/2.0
        if index == 0:
            integrand = c0/2.0
        else:
            integrand = (math.exp(x/2.0)*correlation-c0)/math.sinh(x)
        qweight = step/2.0 if index in (0,len(shifts)-1) else step
        core += qweight*integrand

    q_infinity = (
        -(math.log(4.0*math.pi)+float(mp.euler))*c0
        - core - math.log(math.tanh(radius))*c0
    )

    q_finite = np.zeros_like(q_infinity)
    prime_powers = []
    for prime in primes_upto(int(math.exp(2.0*radius))+2):
        exponent = 1
        while exponent*math.log(prime) < 2.0*radius-1e-12:
            x = exponent*math.log(prime)
            shifted,_,_ = paired_bump_basis(
                t-x,radius,count,width_factor
            )
            correlation = basis.T @ (weights[:,None]*shifted)
            correlation = (correlation+correlation.T)/2.0
            coefficient = -2.0*math.log(prime)*prime**(-exponent/2.0)
            q_finite += coefficient*correlation
            prime_powers.append((prime,exponent,x))
            exponent += 1

    return {
        "radius":radius, "count":count, "step":step,
        "t":t, "basis":basis, "weights":weights,
        "c0":c0, "derivative":derivative_matrix,
        "g0_constraint":g0, "endpoint_constraint":endpoint,
        "q_infinity":q_infinity, "q_finite":q_finite,
        "q_arithmetic":q_infinity+q_finite,
        "prime_powers":prime_powers,
        "centers":centers, "width":width,
    }


def constrained_whitener(model, ordinates):
    rows = [model["g0_constraint"],model["endpoint_constraint"]]
    for ordinate in ordinates:
        rows.append(
            fourier_vector(
                ordinate,model["t"],model["basis"],model["weights"]
            ).real
        )
    kernel = null_space(np.vstack(rows),rcond=1e-11)
    gram = kernel.T @ model["c0"] @ kernel
    values,vectors = eigh(gram)
    keep = values > 1e-9
    return kernel @ vectors[:,keep] @ np.diag(1.0/np.sqrt(values[keep]))


def quadratic_values(matrices, vector):
    return np.einsum("i,kij,j->k",vector,matrices,vector)


def minimax_target(model, coordinate_map, target_matrices, arithmetic_floor):
    qmatrix = coordinate_map.T @ model["q_arithmetic"] @ coordinate_map
    dimension = qmatrix.shape[0]

    def target_fun(z):
        return z[-1]-quadratic_values(target_matrices,z[:dimension])

    def target_jac(z):
        y = z[:dimension]
        jacobian = np.empty((len(target_matrices),dimension+1))
        jacobian[:,:dimension] = -2.0*np.einsum(
            "kij,j->ki",target_matrices,y
        )
        jacobian[:,-1] = 1.0
        return jacobian

    constraints = [
        {
            "type":"eq",
            "fun":lambda z: z[:dimension]@z[:dimension]-1.0,
            "jac":lambda z: np.r_[2.0*z[:dimension],0.0][None,:],
        },
        {
            "type":"ineq",
            "fun":lambda z: z[:dimension]@qmatrix@z[:dimension]-arithmetic_floor,
            "jac":lambda z: np.r_[2.0*qmatrix@z[:dimension],0.0][None,:],
        },
        {"type":"ineq","fun":target_fun,"jac":target_jac},
    ]

    eigenvalues,eigenvectors = np.linalg.eigh(qmatrix)
    start = eigenvectors[:,-1]
    initial_t = quadratic_values(target_matrices,start).max()+1e-5

    return minimize(
        lambda z:z[-1],
        np.r_[start,initial_t],
        jac=lambda z:np.r_[np.zeros(dimension),1.0],
        constraints=constraints,
        method="SLSQP",
        options={"maxiter":1600,"ftol":1e-12},
    )
