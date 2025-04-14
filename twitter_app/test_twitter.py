import os
import sys
import django

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_dir)

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twitter_project.settings')
django.setup()

import tweepy
from twitter_utils import get_twitter_api

def test_twitter_connection():
    try:
        # Get the Twitter API instance
        api = get_twitter_api()
        
        # Try to verify credentials (this should work with basic access)
        user = api.verify_credentials()
        
        print("Successfully connected to Twitter API!")
        print(f"\nAuthenticated as: @{user.screen_name}")
        print(f"Account name: {user.name}")
        print(f"Followers: {user.followers_count}")
        print(f"Following: {user.friends_count}")
        
        # Try to post a test tweet
        try:
            tweet = api.update_status("Hello from my Twitter API test! 🐦 #TwitterAPI")
            print("\nSuccessfully posted a test tweet!")
            print(f"Tweet ID: {tweet.id}")
        except Exception as e:
            print(f"\nCouldn't post tweet: {str(e)}")
            
    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nMake sure you have set up your Twitter API credentials in settings.py:")
        print("TWITTER_API_KEY = 'your_api_key'")
        print("TWITTER_API_SECRET = 'your_api_secret'")
        print("ACCESS_TOKEN = 'your_access_token'")
        print("ACCESS_TOKEN_SECRET = 'your_access_token_secret'")

if __name__ == "__main__":
    test_twitter_connection() 