#Now, we will integrate:
# Twitter (X) Sentiment Analysis – Using AI to analyze public opinion.
# Google Trends Data – Measuring public interest over time.
# Prediction Markets – Collecting odds from betting platforms.

import numpy as np
import pandas as pd
import requests
from textblob import TextBlob
import random  # Simulating prediction market odds since real-time access is limited

# Function to analyze Twitter sentiment (simulated for now)
def analyze_sentiment(nominee):
    # In a real implementation, this function would pull live tweets and analyze sentiment
    sample_tweets = [
        f"{nominee} gave an incredible performance! Oscar-worthy!",
        f"I'm not sure if {nominee} will win, but she deserves the nomination.",
        f"{nominee} is totally overrated. Others did better this year."
    ]
    scores = [TextBlob(tweet).sentiment.polarity for tweet in sample_tweets]
    return np.mean(scores)  # Average sentiment score

# Simulated Google Trends scores (normalized between 0 and 1)
google_trends = {
    "Fernanda Torres": 0.45,  
    "Demi Moore": 0.80,  
    "Mikey Madison": 0.60,  
    "Karla Sofía Gascón": 0.75,  
    "Cynthia Erivo": 0.85  
}

# Simulated prediction market odds (normalized probabilities)
prediction_market_odds = {
    "Fernanda Torres": 0.10,
    "Demi Moore": 0.35,
    "Mikey Madison": 0.15,
    "Karla Sofía Gascón": 0.25,
    "Cynthia Erivo": 0.40
}

# Compute sentiment scores
sentiment_scores = {nominee: analyze_sentiment(nominee) for nominee in google_trends.keys()}

# Weighting factors
WEIGHT_SENTIMENT = 0.40
WEIGHT_TRENDS = 0.30
WEIGHT_MARKETS = 0.30

# Compute final probability
final_probabilities = {
    nominee: (
        WEIGHT_SENTIMENT * sentiment_scores[nominee] +
        WEIGHT_TRENDS * google_trends[nominee] +
        WEIGHT_MARKETS * prediction_market_odds[nominee]
    )
    for nominee in google_trends.keys()
}

# Convert to percentages
final_percentages = {nominee: prob * 100 for nominee, prob in final_probabilities.items()}

# Create a DataFrame
results_df = pd.DataFrame({
    "Actress": list(final_percentages.keys()),
    "Winning Probability (%)": list(final_percentages.values())
}).sort_values(by="Winning Probability (%)", ascending=False)

# Display results
print(results_df)
