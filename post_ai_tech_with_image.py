from twitter_tools import post_tweet_with_image
import os

def main():
    # AI technology image URL
    ai_image_url = "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=600&fit=crop"
    
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
        print(f"Attempting to post AI technology tweet with image...")
        print(f"Tweet length: {len(tweet_text)} characters")
        print(f"Image URL: {ai_image_url}")
        result = post_tweet_with_image(tweet_text, ai_image_url)
        print(f"Success: {result}")
    except Exception as e:
        print(f"Error posting tweet with image: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
