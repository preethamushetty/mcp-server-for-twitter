from twitter_tools import post_tweet_with_image
import os

def main():
    # Trending sports news image URL (using a sports news image)
    sports_image_url = "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=800&h=600&fit=crop"
    
    # Tweet text about trending sports news
    tweet_text = "🏈⚽🏀 Breaking: Latest trending sports news! Stay updated with the biggest stories in sports today. #SportsNews #Trending"
    
    # Check if environment variables are set
    required_vars = ["TWITTER_API_KEY", "TWITTER_API_SECRET", "TWITTER_ACCESS_TOKEN", "TWITTER_ACCESS_SECRET"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"Missing environment variables: {missing_vars}")
        print("Please set up your Twitter API credentials in a .env file or environment variables.")
        return
    
    try:
        print(f"Attempting to post tweet with sports image: '{tweet_text}'")
        print(f"Image URL: {sports_image_url}")
        result = post_tweet_with_image(tweet_text, sports_image_url)
        print(f"Success: {result}")
    except Exception as e:
        print(f"Error posting tweet with image: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
