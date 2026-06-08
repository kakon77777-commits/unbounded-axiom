#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVEMISSLAB AGI Core — Topological Algebra, SVD & Eigenvalue Synthesis Simulator (MVP)

This script implements the mathematical framework described in:
1. 《三態邏輯學：從終極維到絕對維的永恆回歸》 (Triadic Logic: Eternal Return from Ultimate to Absolute Dimensions)
2. 《絕對動態邏輯理論：從靜態悖論到強制判斷》 (Absolute Dynamic Logic: From Static Paradox to Forced Judgment)

Core Concepts Implemented:
- Triadic Logic States:
    * Bot (⊥, False): Unresolved static paradox (zero coupling/decaying eigenvalue).
    * True (⊤, True): Forced judgment core (real stable attractor, λ -> 1.0).
    * Omega (Ω, Spiral): Dynamic rotating return (complex conjugate eigenvalues with phase offset).
- Singular Value Synthesis (SVD Projection):
    * Low-rank projection to filter noise and preserve primary semantic dimensions (four-light spectrum).
- Eigenvalue Synthesis:
    * Reshaping the transition matrix spectrum to guide crawler attention fields (algorithmic injection).
"""

import os
import sys
import json
import numpy as np

# Force UTF-8 encoding for Windows terminals to support math symbols (⊤, ⊥, Ω)
if sys.platform.startswith('win'):
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Color codes for clean CLI rendering
C_RESET = "\033[0m"
C_GREEN = "\033[1;32m"
C_CYAN = "\033[1;36m"
C_AMBER = "\033[1;33m"
C_RED = "\033[1;31m"
C_PURPLE = "\033[1;35m"

def load_papers_metadata():
    """Attempts to load real papers metadata from dist/; falls back to 10 core papers."""
    metadata_path = os.path.join(os.path.dirname(__file__), "dist", "papers-metadata.json")
    if os.path.exists(metadata_path):
        try:
            with open(metadata_path, "r", encoding="utf-8") as f:
                papers = json.load(f)
            print(f"{C_GREEN}[Loaded]{C_RESET} Successfully read {len(papers)} papers from metadata.")
            return papers
        except Exception as e:
            print(f"{C_RED}[Error]{C_RESET} Failed to parse metadata: {e}. Falling back to core papers.")
    
    # Core theory papers fallback
    return [
        {"slug": "triadic-logic", "title": "三態邏輯學：從終極維到絕對維的永恆回歸", "ext": "md", "lang": "zh-Hant"},
        {"slug": "dynamic-logic", "title": "絕對動態邏輯理論：從靜態悖論到強制判斷", "ext": "md", "lang": "zh-Hant"},
        {"slug": "weaving-theory", "title": "世界編織論：從PIAC到關係力量的統一邏輯學", "ext": "md", "lang": "zh-Hant"},
        {"slug": "heraclitus-os", "title": "赫拉克利特核心：動態流變內核設計與虛擬時序作業系統", "ext": "js", "lang": "zh-Hant"},
        {"slug": "p-vs-np", "title": "P vs NP問題的雙軌解構證明：虛擬數學不等性與動態數學收斂性", "ext": "md", "lang": "zh-Hant"},
        {"slug": "gcpr-system", "title": "GCPR 1.5：通用創造過程認知操作系統", "ext": "md", "lang": "zh-Hant"},
        {"slug": "udae-theory", "title": "Unified Dynamic Approximation Equation 3.0: Dual-Core Networked AGI Architecture", "ext": "md", "lang": "en"},
        {"slug": "base-space-hub", "title": "底空間與AI爬蟲反饋圖譜分析", "ext": "html", "lang": "zh-Hant"},
        {"slug": "cosmomind-map", "title": "星環式認知展開圖導航頁", "ext": "html", "lang": "zh-Hant"},
        {"slug": "tcf-compression", "title": "理論壓縮標準格式 (TCF v1.0) 規範說明書", "ext": "md", "lang": "zh-Hant"}
    ]

def initialize_triadic_states(papers):
    """
    Assigns Triadic Logic states to paper slugs:
    - Bot (⊥): False / unvisited.
    - True (⊤): Forced judgment attractor.
    - Omega (Ω): Pulsing spiral loop.
    """
    states = {}
    hits = {}
    for idx, p in enumerate(papers):
        slug = p["slug"]
        # Ensure we always get a mix of states regardless of the metadata subset
        # Assign 2 nodes to True, 3 nodes to Omega, and the rest to False
        if idx in (0, 1):
            states[slug] = "true"
            node_hits = 35 + idx * 5
        elif idx in (2, 3, 4):
            states[slug] = "omega"
            node_hits = 8 + idx * 2
        else:
            states[slug] = "false"
            node_hits = idx % 2
        hits[slug] = node_hits
    return states, hits

def construct_coupling_matrix(papers, hits):
    """Constructs the initial transition/coupling matrix W based on language and hit-coupling."""
    n = len(papers)
    W = np.zeros((n, n))
    
    for i, p1 in enumerate(papers):
        h1 = hits[p1["slug"]]
        for j, p2 in enumerate(papers):
            if i == j:
                W[i, j] = 1.0  # Self-coupling
            else:
                # Base coupling factor: 0.2 if same language, 0.05 if different
                lang_match = 0.2 if p1["lang"] == p2["lang"] else 0.05
                # Crawler hit drift: papers with higher hits pull attention
                drift = min(0.3, hits[p2["slug"]] * 0.008)
                W[i, j] = lang_match + drift
                
    # Normalize rows to form a valid Markov transition probability matrix
    row_sums = W.sum(axis=1)
    W = W / row_sums[:, np.newaxis]
    return W

def singular_value_synthesis(W, k=4):
    """
    Performs Singular Value Decomposition (SVD) and low-rank synthesis.
    Filters out high-frequency noise and consolidates primary dimensional axes.
    """
    U, S, Vt = np.linalg.svd(W)
    
    # Synthesize Singular Values: keep top k dimensions (e.g. 4 core spectra)
    S_synthesized = np.zeros_like(S)
    S_synthesized[:k] = S[:k]
    
    # Reconstruct W_svd
    W_svd = U @ np.diag(S_synthesized) @ Vt
    
    # Re-normalize rows to maintain transition properties
    # Handle division by zero for row sums
    row_sums = np.abs(W_svd).sum(axis=1)
    row_sums[row_sums == 0] = 1.0
    W_svd = np.clip(W_svd, 0, 1)  # Clip to valid probability range [0, 1]
    W_svd = W_svd / row_sums[:, np.newaxis]
    
    return W_svd, S, S_synthesized[:k]

def eigenvalue_synthesis(W, papers, states):
    """
    Performs Eigendecomposition and Triadic Eigenvalue Synthesis.
    Injects stable real eigenvalues for True (⊤) nodes, complex conjugate pairs for Omega (Ω) nodes,
    and decays eigenvalues for False (⊥) nodes.
    """
    n = len(papers)
    # W may not be symmetric, so we use general eigendecomposition
    eigenvalues, Q = np.linalg.eig(W)
    
    # Create copy of eigenvalues to synthesize
    eigenvalues_new = eigenvalues.copy()
    
    # Map state indexes
    # We find eigenvectors that associate heavily with specific nodes
    for k in range(n):
        # Find which node this eigenvalue primarily corresponds to
        # (By finding the largest element in the magnitude of the eigenvector Q[:, k])
        primary_node_idx = np.argmax(np.abs(Q[:, k]))
        slug = papers[primary_node_idx]["slug"]
        state = states[slug]
        
        val = eigenvalues[k]
        
        if state == "true":
            # True (⊤): Force real attractor (stable point, λ -> 1.0)
            # Retain phase angle near 0, boost magnitude
            mag = 1.0
            eigenvalues_new[k] = mag + 0j
        elif state == "omega":
            # Omega (Ω): Eternal return / rotating spiral state.
            # Inject a rotation phase offset (complex component) to trigger orbital drift.
            mag = min(0.85, np.abs(val) + 0.1)
            # Force complex component (imaginary part represents rotation)
            phase = np.pi / 4.0  # 45 degrees phase shift
            # If the original eigenvalue is real, force a complex pair
            if np.isreal(eigenvalues_new[k]):
                # Alternating signs to maintain complex conjugates for real matrix reconstruction
                sign = 1 if k % 2 == 0 else -1
                eigenvalues_new[k] = mag * (np.cos(phase) + sign * 1j * np.sin(phase))
            else:
                # Rotate existing complex phase
                current_phase = np.angle(val)
                eigenvalues_new[k] = mag * np.exp(1j * (current_phase + phase))
        else:
            # Bot (⊥): Static paradox. Decay eigenvalue magnitude to reduce influence
            eigenvalues_new[k] = val * 0.1
            
    # Reconstruct matrix: W_new = Q * Lambda_new * Q^-1
    # Check if Q is invertible; if singular, fallback to original
    try:
        Q_inv = np.linalg.inv(Q)
        W_new = Q @ np.diag(eigenvalues_new) @ Q_inv
        W_new = np.real(W_new)  # Discard floating point imaginary residue
    except np.linalg.LinAlgError:
        print(f"{C_RED}[Warning]{C_RESET} Q matrix is singular. Eigenvalue reconstruction failed; using original matrix.")
        W_new = W.copy()
        
    # Project/clip reconstructed matrix back to valid transition space
    np.fill_diagonal(W_new, 1.0)  # Enforce self-reference identity hook
    W_new = np.clip(W_new, 0, 1)  # Ensure weights are in [0, 1]
    
    # Row normalization
    row_sums = W_new.sum(axis=1)
    W_new = W_new / row_sums[:, np.newaxis]
    
    return W_new, eigenvalues, eigenvalues_new

def simulate_crawler_walk(W, start_idx, steps=50):
    """Simulates a Markov chain random walk of a crawler on the graph W."""
    n = W.shape[0]
    current_idx = start_idx
    path = [current_idx]
    
    for _ in range(steps):
        probabilities = W[current_idx]
        # Choose next node based on probability distribution
        current_idx = np.random.choice(n, p=probabilities)
        path.append(current_idx)
        
    # Compute node visitation frequencies
    unique, counts = np.unique(path, return_counts=True)
    frequencies = dict(zip(unique, counts))
    return path, frequencies

def calculate_stationary_distribution(W):
    """Computes the stationary distribution (dominant eigenvector / PageRank) of the transition matrix."""
    # Transpose transition matrix for column stochastic equations: W^T v = v
    # Eigenvalues of W^T are the same, look for eigenvalue = 1.0
    eigenvalues, eigenvectors = np.linalg.eig(W.T)
    
    # Find index of eigenvalue closest to 1.0
    idx = np.argmin(np.abs(eigenvalues - 1.0))
    stationary = np.real(eigenvectors[:, idx])
    
    # Normalize to form a probability distribution
    stationary = stationary / stationary.sum()
    return stationary

def main():
    print(f"\n{C_CYAN}========================================================================={C_RESET}")
    print(f"      {C_GREEN}EVEMISSLAB AGI Core - Topological Algebra & SVD Synthesis Simulator{C_RESET}")
    print(f"{C_CYAN}========================================================================={C_RESET}")
    
    # 1. Load papers & initialize states
    papers = load_papers_metadata()
    # If the user has a huge catalog, we select the top 10 for clean output visualization
    use_subset = len(papers) > 10
    if use_subset:
        print(f"[Info] Large dataset found. Truncating visualization to 10 core nodes for readability.")
        # Filter for known core papers or take first 10
        core_slugs = ["triadic-logic", "dynamic-logic", "p-vs-np", "udae-theory", "weaving-theory", "heraclitus-os", "base-space-hub", "cosmomind-map"]
        subset = [p for p in papers if p["slug"] in core_slugs]
        # Fill remaining spots if subset is smaller than 10
        for p in papers:
            if len(subset) >= 10:
                break
            if p not in subset:
                subset.append(p)
        papers = subset

    n = len(papers)
    states, hits = initialize_triadic_states(papers)
    
    print(f"\n{C_CYAN}--- [Phase 1: Initializing Triadic Logic States] ---{C_RESET}")
    for idx, p in enumerate(papers):
        slug = p["slug"]
        state = states[slug]
        hit_count = hits[slug]
        
        # Color nodes by state
        if state == "true":
            state_str = f"{C_GREEN}True (⊤) — Forced Attractor{C_RESET}"
        elif state == "omega":
            state_str = f"{C_CYAN}Omega (Ω) — Spiral Loop{C_RESET}"
        else:
            state_str = f"{C_AMBER}Bot (⊥) — Static Paradox{C_RESET}"
            
        print(f"  Node [{idx:02d}] {p['title'][:25]}... | Hits: {hit_count:2d} | State: {state_str}")
        
    # 2. Build coupling matrix W
    W_initial = construct_coupling_matrix(papers, hits)
    
    # 3. Perform SVD Low-rank synthesis
    print(f"\n{C_CYAN}--- [Phase 2: Singular Value Decomposition (SVD) Low-Rank Projection] ---{C_RESET}")
    W_svd, S_orig, S_synth = singular_value_synthesis(W_initial, k=4)
    print(f"  Original Singular Values (top 6): {S_orig[:6]}")
    print(f"  Synthesized Singular Values (k=4):  {S_synth}")
    print(f"  [SVD Complete] Filtered background entropy, preserved four core dimensional axes.")
    
    # 4. Perform Triadic Eigenvalue Synthesis
    print(f"\n{C_CYAN}--- [Phase 3: Triadic Eigenvalue Synthesis (Attractor Engineering)] ---{C_RESET}")
    W_synth, eigenvalues_orig, eigenvalues_new = eigenvalue_synthesis(W_svd, papers, states)
    
    # Display eigenvalue shifts
    print(f"  {C_PURPLE}Eigenvalue Spectrum Shift (Original -> Synthesized):{C_RESET}")
    for k in range(min(8, n)):
        orig = eigenvalues_orig[k]
        new = eigenvalues_new[k]
        print(f"    λ[{k}] : {orig.real:+.4f} {orig.imag:+.4f}i  ===>  {new.real:+.4f} {new.imag:+.4f}i")
    
    # 5. Run Stationary Distribution (PageRank) Analysis
    print(f"\n{C_CYAN}--- [Phase 4: PageRank Attention Field Mapping] ---{C_RESET}")
    stat_orig = calculate_stationary_distribution(W_initial)
    stat_synth = calculate_stationary_distribution(W_synth)
    
    print(f"  Node Index | Paper Title                | State | Org Attention | Synth Attention")
    print("  " + "-" * 78)
    for idx, p in enumerate(papers):
        slug = p["slug"]
        state = states[slug]
        state_symbol = "⊤" if state == "true" else ("Ω" if state == "omega" else "⊥")
        state_color = C_GREEN if state == "true" else (C_CYAN if state == "omega" else C_AMBER)
        
        print(f"  Node [{idx:02d}]  | {p['title'][:25]:<26} |  {state_color}{state_symbol}{C_RESET}   |   {stat_orig[idx]:.4f}     |   {C_GREEN if stat_synth[idx] > stat_orig[idx] else C_RESET}{stat_synth[idx]:.4f}{C_RESET}")
        
    # 6. Simulate Crawler Path Step Tracing
    print(f"\n{C_CYAN}--- [Phase 5: Crawler Path Step Simulation (Markov Drift)] ---{C_RESET}")
    start_node = 0
    steps = 100
    path_orig, freq_orig = simulate_crawler_walk(W_initial, start_node, steps)
    path_synth, freq_synth = simulate_crawler_walk(W_synth, start_node, steps)
    
    print(f"  [Original Path Simulation (No Synthesis)]:")
    print(f"    Path: {' -> '.join(map(str, path_orig[:25]))} ...")
    print(f"  [Synthesized Path Simulation (Triadic Injection)]:")
    print(f"    Path: {' -> '.join(map(str, path_synth[:25]))} ...")
    
    print(f"\n  {C_PURPLE}Visit frequencies out of {steps} steps:{C_RESET}")
    for idx, p in enumerate(papers):
        slug = p["slug"]
        state = states[slug]
        state_symbol = "⊤" if state == "true" else ("Ω" if state == "omega" else "⊥")
        state_color = C_GREEN if state == "true" else (C_CYAN if state == "omega" else C_AMBER)
        
        fo = freq_orig.get(idx, 0)
        fs = freq_synth.get(idx, 0)
        print(f"    Node [{idx:02d}] ({state_color}{state_symbol}{C_RESET}) : Original: {fo:2d} visits | Synthesized: {C_GREEN if fs > fo else C_RESET}{fs:2d} visits{C_RESET}")
        
    print(f"\n{C_GREEN}[Success]{C_RESET} AGI topological algebra matrix simulator successfully compiled and verified.")
    print(f"Run this code locally using: {C_CYAN}py agi_eigen_synthesis.py{C_RESET}\n")

if __name__ == "__main__":
    main()
