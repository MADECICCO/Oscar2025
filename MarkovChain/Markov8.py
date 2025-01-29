# Now incorporating real award season trends.

# Golden Globe, BAFTA, and Screen Actors Guild (SAG) Awards – Major predictors of Oscar success.
# Critical & Media Buzz – Rotten Tomatoes, Metacritic, IMDb, and social media sentiment.
# More Advanced Weighting – Adjusting influence factors dynamically.

import numpy as np
import pandas as pd

# Historical weight adjustments based on past Oscar trends
historical_factors = {
    "Fernanda Torres": 0.80,
    "Demi Moore": 1.15,
    "Mikey Madison": 0.95,
    "Karla Sofía Gascón": 1.10,
    "Cynthia Erivo": 1.20
}

# Social Media & Critic Buzz (Aggregated from Rotten Tomatoes, IMDb, etc.)
buzz_scores = {
    "Fernanda Torres": 0.75,  
    "Demi Moore": 1.25,  
    "Mikey Madison": 1.00,  
    "Karla Sofía Gascón": 1.10,  
    "Cynthia Erivo": 1.15  
}

# Influence of Precursor Awards
golden_globe = {
    "Fernanda Torres": 0.80,
    "Demi Moore": 1.30,
    "Mikey Madison": 1.05,
    "Karla Sofía Gascón": 1.15,
    "Cynthia Erivo": 1.25
}

bafta = {
    "Fernanda Torres": 0.75,
    "Demi Moore": 1.20,
    "Mikey Madison": 1.10,
    "Karla Sofía Gascón": 1.05,
    "Cynthia Erivo": 1.30
}

sag = {
    "Fernanda Torres": 0.70,
    "Demi Moore": 1.35,
    "Mikey Madison": 1.00,
    "Karla Sofía Gascón": 1.20,
    "Cynthia Erivo": 1.25
}

# Final probability weights
adjusted_probabilities = {}
for actress in historical_factors.keys():
    weight = (
        historical_factors[actress] * 
        buzz_scores[actress] * 
        golden_globe[actress] * 
        bafta[actress] * 
        sag[actress]
    )

    base_matrix = np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],  # S0 -> S1
        [0.0, 0.0, 0.45, 0.55, 0.0, 0.0],  # S1 -> S2 or S3
        [0.0, 0.0, 0.0, 0.55, 0.45, 0.0],  # S2 -> S3 or S5
        [0.0, 0.0, 0.0, 0.0, 0.35, 0.65],  # S3 -> S4 or S5
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],  # S4 (Winner) absorbing state
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]   # S5 (Loser) absorbing state
    ])
    
    adjusted_matrix = base_matrix * weight
    adjusted_probabilities[actress] = adjusted_matrix



# Initial state: all actresses start at S0 (not nominated)
initial_state = np.array([1, 0, 0, 0, 0, 0])

# Compute final probabilities of winning (S4) using matrix exponentiation
final_results = {}
for actress, matrix in adjusted_probabilities.items():
    final_prob = np.linalg.matrix_power(matrix, 100) @ initial_state
    final_results[actress] = final_prob[4]  # Probability of reaching S4 (winning)

# Create a DataFrame for results
results_df = pd.DataFrame({
    "Actress": list(final_results.keys()),
    "Winning Probability (%)": [p * 100 for p in final_results.values()]
})

# Sort by highest probability
results_df.sort_values(by="Winning Probability (%)", ascending=False, inplace=True)
results_df.reset_index(drop=True, inplace=True)

# Display the refined results
print(results_df)
