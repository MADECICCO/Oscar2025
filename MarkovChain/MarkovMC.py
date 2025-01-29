

import numpy as np
import random

# Candidates and their base scores (from awards, engagement, campaigns, and historical penalties)
candidates = {
    "Fernanda Torres": {"globo": 1, "sag": 0, "bafta": 0, "engagement": 0.6, "campaign": 0.7},
    "Demi Moore": {"globo": 1, "sag": 1, "bafta": 1, "engagement": 0.9, "campaign": 0.9},
    "Cynthia Erivo": {"globo": 0, "sag": 1, "bafta": 1, "engagement": 0.8, "campaign": 0.7},
    "Karla Sofía Gascón": {"globo": 0, "sag": 0, "bafta": 0, "engagement": 0.6, "campaign": 0.8},
    "Mikey Madison": {"globo": 0, "sag": 1, "bafta": 1, "engagement": 0.7, "campaign": 0.7},
}

# Weights for each factor
weights = {
    "awards": 0.4,   # Weight for awards (Globo, SAG, BAFTA)
    "engagement": 0.3,  # Weight for social media engagement
    "campaign": 0.2,    # Weight for marketing campaigns
    "historical": 0.1,  # Weight for historical penalties
}

# Monte Carlo parameters
num_simulations = 1000  # Number of Monte Carlo trials

def calculate_score(candidate):
    """Calculate the candidate's score with added randomness for Monte Carlo simulation."""
    # Add random noise to engagement and campaign scores (normal distribution, std=0.05)
    engagement_noise = np.random.normal(0, 0.05)
    campaign_noise = np.random.normal(0, 0.05)
    
    # Calculate scores with noise (clipped between 0 and 1)
    awards_score = (candidate["globo"] + candidate["sag"] + candidate["bafta"]) / 3
    engagement_score = np.clip(candidate["engagement"] + engagement_noise, 0, 1)
    campaign_score = np.clip(candidate["campaign"] + campaign_noise, 0, 1)
    
    # Apply historical penalty for foreign candidates (Fernanda Torres and Karla)
    historical_penalty = 0.1 if "Fernanda" in candidate["name"] or "Karla" in candidate["name"] else 0
    
    # Total score calculation
    total_score = (
        awards_score * weights["awards"]
        + engagement_score * weights["engagement"]
        + campaign_score * weights["campaign"]
        - historical_penalty * weights["historical"]
    )
    return total_score

# Monte Carlo simulation
results = {name: 0 for name in candidates.keys()}  # Initialize results

for _ in range(num_simulations):
    scores = {}
    for name, data in candidates.items():
        data_with_name = data.copy()
        data_with_name["name"] = name  # Add name for penalty logic
        scores[name] = calculate_score(data_with_name)
    
    # Find the winner of this simulation
    winner = max(scores, key=scores.get)
    results[winner] += 1

# Convert results to probabilities
monte_carlo_probs = {name: (count / num_simulations) * 100 for name, count in results.items()}

# Print results
print("Monte Carlo Probabilities (1000 simulations):")
for name, prob in monte_carlo_probs.items():
    print(f"{name}: {prob:.2f}%")