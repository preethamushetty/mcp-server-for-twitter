from twitter_tools import delete_tweet
import os

def main():
    # Tweet ID from the sports news post that was just created
    tweet_id = "1954489838625018168"
    
    # Check if environment variables are set
    required_vars = ["TWITTER_API_KEY", "TWITTER_API_SECRET", "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"Missing environment variables: {missing_vars}")
        print("Please set up your Twitter API credentials in a .env file or environment variables.")
        return
    
    try:
        print(f"Attempting to delete tweet with ID: {tweet_id}")
        result = delete_tweet(tweet_id)
        print(f"Success: {result}")
    except Exception as e:
        print(f"Error deleting tweet: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
