from __future__ import annotations
import numpy as np
from scipy.optimize import minimize

from prototype import quadratic_values, minimax_target


def exchange_control_window(
    model,
    coordinate_map,
    target_matrices,
    target_eta,
    initial_control_matrices,
    dense_control_matrices,
    arithmetic_floor,
    rounds=12,
):
    """Floating exchange-method prototype for a sampled semi-infinite QCQP."""
    qmatrix = coordinate_map.T @ model["q_arithmetic"] @ coordinate_map
    dimension = qmatrix.shape[0]
    active = list(initial_control_matrices)

    initial = minimax_target(
        model, coordinate_map, target_matrices, arithmetic_floor
    )
    start = initial.x[:dimension]
    history = []

    for round_index in range(rounds):
        active_array = np.asarray(active)

        def target_fun(z):
            return -target_eta-quadratic_values(
                target_matrices,z[:dimension]
            )

        def target_jac(z):
            y = z[:dimension]
            return np.c_[
                -2.0*np.einsum("kij,j->ki",target_matrices,y),
                np.zeros(len(target_matrices)),
            ]

        def control_fun(z):
            return z[-1]-quadratic_values(
                active_array,z[:dimension]
            )

        def control_jac(z):
            y = z[:dimension]
            return np.c_[
                -2.0*np.einsum("kij,j->ki",active_array,y),
                np.ones(len(active_array)),
            ]

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
            {"type":"ineq","fun":control_fun,"jac":control_jac},
        ]

        initial_u = quadratic_values(active_array,start).max()+1e-5
        result = minimize(
            lambda z:z[-1],
            np.r_[start,initial_u],
            jac=lambda z:np.r_[np.zeros(dimension),1.0],
            constraints=constraints,
            method="SLSQP",
            options={"maxiter":1800,"ftol":1e-12},
        )
        start = result.x[:dimension]
        dense_values = quadratic_values(dense_control_matrices,start)
        worst_index = int(np.argmax(dense_values))
        dense_maximum = float(dense_values[worst_index])
        history.append({
            "round":round_index,
            "active_constraint_count":len(active),
            "active_maximum":float(result.x[-1]),
            "dense_maximum":dense_maximum,
            "optimizer_success":bool(result.success),
        })
        if dense_maximum <= result.x[-1]+1e-5:
            break
        active.append(dense_control_matrices[worst_index])

    return result, history
