import numpy as np
import pandas as pd

# Transition matrix for each actress
matrices_transition = {
    "Fernanda Torres": np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],  # S0 -> S1
        [0.0, 0.0, 0.4, 0.6, 0.0, 0.0],  # S1 -> S2 or S3
        [0.0, 0.0, 0.0, 0.5, 0.5, 0.0],  # S2 -> S3 or S5
        [0.0, 0.0, 0.0, 0.0, 0.2, 0.8],  # S3 -> S4 or S5
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],  # S4 (win) absorbing state
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]   # S5 (loss) absorbing state
    ]),
    "Demi Moore": np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 
        [0.0, 0.0, 0.5, 0.5, 0.0, 0.0], 
        [0.0, 0.0, 0.0, 0.6, 0.4, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.3, 0.7], 
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    ]),
    "Mikey Madison": np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 
        [0.0, 0.0, 0.3, 0.7, 0.0, 0.0], 
        [0.0, 0.0, 0.0, 0.6, 0.4, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.25, 0.75], 
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    ]),
    "Karla Sofía Gascón": np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 
        [0.0, 0.0, 0.55, 0.45, 0.0, 0.0], 
        [0.0, 0.0, 0.0, 0.4, 0.6, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.35, 0.65], 
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    ]),
    "Cynthia Erivo": np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0], 
        [0.0, 0.0, 0.6, 0.4, 0.0, 0.0], 
        [0.0, 0.0, 0.0, 0.55, 0.45, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.4, 0.6], 
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0], 
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]
    ])
}

# Initial state: All actresses start at S0 (not nominated)
initial_state = np.array([1, 0, 0, 0, 0, 0])

# Calculate the final probability of winning (S4) for each actress
results = {}
for actress, matrix in matrices_transition.items():
    # Using a smaller number of steps to avoid early convergence
    probability_final = np.linalg.matrix_power(matrix, 100) @ initial_state
    results[actress] = probability_final[4]  # Probability of S4 (win)

# Create a table of results
results_table = pd.DataFrame({
    "Actress": list(results.keys()),
    "Winning Probability (%)": [p * 100 for p in results.values()]
})

# Sort by highest probability
results_table.sort_values(by="Winning Probability (%)", ascending=False, inplace=True)
results_table.reset_index(drop=True, inplace=True)

# Display the final table
print(results_table)
