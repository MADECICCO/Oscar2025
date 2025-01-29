# This version improves the Markov Chain by integrating weights based on past trends, social influence, and award history.

# Key Points:
# incorporating additional factors that can influence Oscar wins, such as:

# Historical Trends – Previous winners' characteristics (e.g., nationality, age, past nominations, genre).
#Social Trends – Sentiment analysis from social media, critics' scores, and box office performance.
# Precursor Awards – The influence of Golden Globes, BAFTAs, and Critics’ Choice on the Oscars.
# Director & Studio Weight – Major studios and directors have a track record of influencing Oscar wins.

import numpy as np
import pandas as pd

# Historical weight adjustments based on previous winners and trends
historical_factors = {
    "Fernanda Torres": 0.85,  # Brazilian actress, needs more international exposure
    "Demi Moore": 1.10,  # Hollywood veteran, high recognition
    "Mikey Madison": 0.95,  # Emerging talent, indie film credibility
    "Karla Sofía Gascón": 1.05,  # Unique role, strong representation factor
    "Cynthia Erivo": 1.15  # Multi-talented performer, past nominee
}

# Social sentiment analysis weight (based on online discussions, critics, trends)
social_trends = {
    "Fernanda Torres": 0.80,  # Moderate social buzz
    "Demi Moore": 1.20,  # High engagement due to comeback factor
    "Mikey Madison": 0.90,  # Strong critical reception but low mainstream buzz
    "Karla Sofía Gascón": 1.10,  # Positive representation in LGBTQ+ discussions
    "Cynthia Erivo": 1.05  # Balanced critical and audience reception
}

# Influence of precursor awards (Golden Globes, BAFTAs, Critics’ Choice)
precursor_awards = {
    "Fernanda Torres": 0.75,  # Fewer previous major international awards
    "Demi Moore": 1.30,  # Stronger chances if she wins a Golden Globe
    "Mikey Madison": 1.00,  # Balanced, no significant boost
    "Karla Sofía Gascón": 1.05,  # Some recognition potential
    "Cynthia Erivo": 1.20  # Strong potential if BAFTA win
}

# Adjusted transition matrices incorporating historical and social factors
adjusted_probabilities = {}

for actress in historical_factors.keys():
    weight = historical_factors[actress] * social_trends[actress] * precursor_awards[actress]
    
    base_matrix = np.array([
        [0.0, 1.0, 0.0, 0.0, 0.0, 0.0],  # S0 -> S1
        [0.0, 0.0, 0.45, 0.55, 0.0, 0.0],  # S1 -> S2 or S3
        [0.0, 0.0, 0.0, 0.55, 0.45, 0.0],  # S2 -> S3 or S5
        [0.0, 0.0, 0.0, 0.0, 0.35, 0.65],  # S3 -> S4 or S5
        [0.0, 0.0, 0.0, 0.0, 1.0, 0.0],  # S4 (Winner) absorbing state
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0]   # S5 (Loser) absorbing state
    ])
    
    adjusted_matrix = base_matrix * weight  # Scaling probabilities
    adjusted_probabilities[actress] = adjusted_matrix

# Initial state: all actresses start at S0 (not nominated)
initial_state = np.array([1, 0, 0, 0, 0, 0])

# Compute final probabilities of winning (S4) using matrix exponentiation
final_results = {}
for actress, matrix in adjusted_probabilities.items():
    final_prob = np.linalg.matrix_power(matrix, 1000) @ initial_state
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
