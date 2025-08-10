from twitter_tools import post_tweet
import os

def main():
    message = "Save water, save lives."
    
    # Check if environment variables are set
    required_vars = ["TWITTER_API_KEY", "TWITTER_API_SECRET", "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"Missing environment variables: {missing_vars}")
        print("Please set up your Twitter API credentials in a .env file or environment variables.")
        return
    
    try:
        print(f"Attempting to post tweet: '{message}'")
        result = post_tweet(message)
        print(f"Success: {result}")
    except Exception as e:
        print(f"Error posting tweet: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()


