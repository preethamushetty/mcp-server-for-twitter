from twitter_tools import post_tweet
import os

def main():
    # Tweet about emerging AI technologies with trending hashtags (under 280 characters)
    tweet_text = "🤖🚀 Emerging AI technologies are revolutionizing every industry! From Generative AI to Computer Vision, the future is here. What excites you most about the AI revolution? #AI #MachineLearning #TechTrends #Innovation #FutureTech #AIRevolution"
    
    # Check if environment variables are set
    required_vars = ["TWITTER_API_KEY", "TWITTER_API_SECRET", "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"Missing environment variables: {missing_vars}")
        print("Please set up your Twitter API credentials in a .env file or environment variables.")
        return
    
    try:
        print(f"Attempting to post AI technology tweet...")
        print(f"Tweet length: {len(tweet_text)} characters")
        result = post_tweet(tweet_text)
        print(f"Success: {result}")
    except Exception as e:
        print(f"Error posting tweet: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
