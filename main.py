import json
import requests
from requests_oauthlib import OAuth1
from gpt import chat_gpt

#tweet function using credentials
def tweet(tweet_text):
    # Load your credentials
    with open('twitter_credentials.json') as f:
        credentials = json.load(f)

    consumer_key = credentials['consumer_key']
    consumer_secret = credentials['consumer_secret']
    access_token = credentials['access_token']
    access_token_secret = credentials['access_token_secret']

    # Set up OAuth1 authentication
    auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

    # Make the request to post a tweet
    url = "https://api.twitter.com/2/tweets"
    headers = {"Content-Type": "application/json"}
    payload = {"text": tweet_text}

    response = requests.post(url, auth=auth, headers=headers, json=payload)

    # Check the response
    if response.status_code == 201:
        print("Tweet posted successfully!")
        print(response.json())
    else:
        print(f"Failed to post tweet: {response.status_code}")
        print(response.json())


# notifies user of DM's from account using email smtplib



# Define the tweet
gpt_response = chat_gpt(user_message="draft a post")

if len(gpt_response) < 200:
    tweet_text = gpt_response
    tweet(tweet_text)
else:
    print("tweet is too long")