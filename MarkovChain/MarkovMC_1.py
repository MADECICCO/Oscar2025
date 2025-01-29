
# Enhanced Python Script for Real-Time Social Media Data and Influencer Analysis

# Below is a Python script that integrates real-time social media APIs
# and influencer impact analysis to enhance the calculation of probabilities for Fernanda Torres
# and other actresses winning the 2025 Oscar for Best Actress.
# The script uses libraries like tweepy for Twitter, facebook-sdk for Facebook,
# and TextBlob for sentiment analysis.
#  It also incorporates influencer impact metrics based on social media engagement.

import tweepy
import facebook
from textblob import TextBlob
import pandas as pd
import numpy as np




# API Keys and Tokens (Replace with your own credentials)
TWITTER_API_KEY = 'your_twitter_api_key'
TWITTER_API_SECRET = 'your_twitter_api_secret'
TWITTER_ACCESS_TOKEN = 'your_twitter_access_token'
TWITTER_ACCESS_TOKEN_SECRET = 'your_twitter_access_token_secret'
FACEBOOK_ACCESS_TOKEN = 'your_facebook_access_token'

# Authenticate Twitter API
auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth)

# Authenticate Facebook API
facebook_api = facebook.GraphAPI(FACEBOOK_ACCESS_TOKEN)

# Candidates and their social media handles
candidates = {
    "Fernanda Torres": {"twitter": "@fernandatorres", "facebook": "fernandatorres"},
    "Demi Moore": {"twitter": "@demimoore", "facebook": "demimoore"},
    "Cynthia Erivo": {"twitter": "@cynthiaerivo", "facebook": "cynthiaerivo"},
    "Karla Sofía Gascón": {"twitter": "@karlasofiasg", "facebook": "karlasofiasg"},
    "Mikey Madison": {"twitter": "@mikeymadison", "facebook": "mikeymadison"},
}

# Function to fetch real-time engagement data from Twitter
def fetch_twitter_engagement(handle):
    try:
        tweets = twitter_api.user_timeline(screen_name=handle, count=10, tweet_mode="extended")
        engagement = sum([tweet.favorite_count + tweet.retweet_count for tweet in tweets])
        return engagement
    except tweepy.errors.TweepyException as e:
        print(f"Error fetching Twitter data for {handle}: {e}")
        return 0

# Function to fetch real-time engagement data from Facebook
def fetch_facebook_engagement(page_name):
    try:
        page = facebook_api.get_object(page_name, fields="engagement")
        return page['engagement']['reaction_count'] + page['engagement']['comment_count']
    except facebook.GraphAPIError as e:
        print(f"Error fetching Facebook data for {page_name}: {e}")
        return 0

# Function to analyze sentiment of social media posts
def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity  # Returns a value between -1 (negative) and 1 (positive)

# Function to calculate influencer impact score
def calculate_influencer_impact(engagement, sentiment):
    return engagement * (1 + sentiment)  # Higher sentiment amplifies impact

# Main function to calculate probabilities
def calculate_probabilities():
    results = {}
    for name, handles in candidates.items():
        # Fetch real-time engagement data
        twitter_engagement = fetch_twitter_engagement(handles["twitter"])
        facebook_engagement = fetch_facebook_engagement(handles["facebook"])
        total_engagement = twitter_engagement + facebook_engagement

        # Fetch sentiment analysis from recent tweets
        tweets = twitter_api.user_timeline(screen_name=handles["twitter"], count=10, tweet_mode="extended")
        sentiment = np.mean([analyze_sentiment(tweet.full_text) for tweet in tweets])

        # Calculate influencer impact
        influencer_impact = calculate_influencer_impact(total_engagement, sentiment)

        # Store results
        results[name] = influencer_impact

    # Normalize probabilities
    total_impact = sum(results.values())
    probabilities = {name: (impact / total_impact) * 100 for name, impact in results.items()}

    return probabilities

# Run the analysis
probabilities = calculate_probabilities()
print("Probabilities of Winning the 2025 Oscar for Best Actress:")
for name, prob in probabilities.items():
    print(f"{name}: {prob:.2f}%")