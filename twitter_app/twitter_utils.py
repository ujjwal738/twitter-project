import tweepy
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def get_twitter_api():
    try:
        # Verify that all required credentials are present
        required_credentials = [
            'TWITTER_API_KEY',
            'TWITTER_API_SECRET',
            'ACCESS_TOKEN',
            'ACCESS_TOKEN_SECRET'
        ]
        
        missing_credentials = [cred for cred in required_credentials if not getattr(settings, cred, None)]
        if missing_credentials:
            raise ValueError(f"Missing Twitter API credentials: {', '.join(missing_credentials)}")

        # Create OAuth 2.0 User Context
        client = tweepy.Client(
            consumer_key=settings.TWITTER_API_KEY,
            consumer_secret=settings.TWITTER_API_SECRET,
            access_token=settings.ACCESS_TOKEN,
            access_token_secret=settings.ACCESS_TOKEN_SECRET,
            wait_on_rate_limit=True
        )
        
        return client
    except Exception as e:
        logger.error(f"Error initializing Twitter API: {str(e)}")
        raise

def get_user_tweets(api, user_id=None, count=10):
    try:
        if user_id is None:
            # Get the authenticated user's ID
            user = api.get_me()
            user_id = user.data.id
        
        # Get user's tweets using v2 API
        tweets = api.get_users_tweets(
            id=user_id,
            max_results=count,
            tweet_fields=['created_at', 'public_metrics', 'author_id']
        )
        
        return tweets.data if tweets.data else []
    except Exception as e:
        logger.error(f"Error getting user tweets: {str(e)}")
        return []

def post_tweet(api, text):
    try:
        # First verify we can post
        user = api.get_me()
        if not user.data:
            raise Exception("Could not verify user permissions")
            
        response = api.create_tweet(text=text)
        return response.data
    except Exception as e:
        logger.error(f"Error posting tweet: {str(e)}")
        raise
