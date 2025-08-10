from dotenv import load_dotenv
import tweepy
import os
import requests
from io import BytesIO

load_dotenv()  # ✅ Load .env file

API_KEY = os.getenv("TWITTER_API_KEY")
API_SECRET = os.getenv("TWITTER_API_SECRET")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Use v2 API instead of v1.1
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET
)

def post_tweet(text):
    try:
        # Try v2 API first
        response = client.create_tweet(text=text)
        tweet_id = response.data['id']
        return f"Tweet posted: https://twitter.com/user/status/{tweet_id}"
    except Exception as e:
        print(f"V2 API failed: {e}")
        # Fallback to v1.1 API
        status = api.update_status(status=text)
        return f"Tweet posted: https://twitter.com/user/status/{status.id}"

def post_tweet_with_image(text, image_path_or_url):
    """
    Post a tweet with an image
    Args:
        text: The tweet text
        image_path_or_url: Local file path or URL to the image
    """
    try:
        # Handle both local files and URLs
        if image_path_or_url.startswith(('http://', 'https://')):
            # Download image from URL
            response = requests.get(image_path_or_url)
            response.raise_for_status()
            media_data = BytesIO(response.content)
            filename = "downloaded_image.jpg"
        else:
            # Local file
            media_data = open(image_path_or_url, 'rb')
            filename = os.path.basename(image_path_or_url)
        
        # Upload media using v1.1 API (media upload is not available in v2)
        media = api.media_upload(filename=filename, file=media_data)
        
        # Post tweet with media using v2 API
        response = client.create_tweet(text=text, media_ids=[media.media_id])
        tweet_id = response.data['id']
        
        return f"Tweet with image posted: https://twitter.com/user/status/{tweet_id}"
        
    except Exception as e:
        print(f"Error posting tweet with image: {e}")
        # Fallback to text-only tweet
        return post_tweet(text)

def delete_tweet(tweet_id):
    try:
        # Try v2 API first
        client.delete_tweet(tweet_id)
        return f"Tweet {tweet_id} deleted."
    except Exception as e:
        print(f"V2 API failed: {e}")
        # Fallback to v1.1 API
        api.destroy_status(tweet_id)
        return f"Tweet {tweet_id} deleted."

def reply_to_tweet(tweet_id, text):
    try:
        # Try v2 API first
        response = client.create_tweet(text=text, in_reply_to_tweet_id=tweet_id)
        reply_id = response.data['id']
        return f"Replied: https://twitter.com/user/status/{reply_id}"
    except Exception as e:
        print(f"V2 API failed: {e}")
        # Fallback to v1.1 API
        tweet = api.get_status(tweet_id)
        username = tweet.user.screen_name
        reply = f"@{username} {text}"
        status = api.update_status(status=reply, in_reply_to_status_id=tweet_id)
        return f"Replied: https://twitter.com/user/status/{status.id}"



