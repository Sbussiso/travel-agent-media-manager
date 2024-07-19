import os
import requests
from requests_oauthlib import OAuth1
from gpt import chat_gpt
from authentication import authenticate
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Tweet function using credentials from environment variables
def tweet(tweet_text):
    try:
        # Load your credentials from environment variables
        consumer_key = os.getenv('CONSUMER_KEY')
        consumer_secret = os.getenv('CONSUMER_SECRET')
        access_token = os.getenv('ACCESS_TOKEN')
        access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

        if not all([consumer_key, consumer_secret, access_token, access_token_secret]):
            raise ValueError("Missing Twitter API credentials in environment variables.")

        # Set up OAuth1 authentication
        auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

        # Make the request to post a tweet
        url = "https://api.twitter.com/2/tweets"
        headers = {"Content-Type": "application/json"}
        payload = {"text": tweet_text}

        response = requests.post(url, auth=auth, headers=headers, json=payload)

        # Check the response
        if response.status_code == 201:
            logger.info("Tweet posted successfully!")
            logger.info(response.json())
        else:
            logger.error(f"Failed to post tweet: {response.status_code}")
            logger.error(response.json())

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        authenticate()

if __name__ == "__main__":
    # Define the tweet
    tweet_text = chat_gpt(user_message="draft a post")
    logger.info(f"Generated tweet: {tweet_text}")

    retry = True
    while retry:
        try:
            tweet(tweet_text)

            # Save the tweet to post history
            file = "post-history.txt"
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    f.write(f"")

            with open(file, 'a') as f:
                f.write(f"-- Post History -- {tweet_text} -- Post History --\n")
            retry = False

        except Exception as e:
            logger.error(f"An error occurred: {e}")
            authenticate()
            retry = True
