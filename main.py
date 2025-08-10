from twitter_tools import post_tweet, reply_to_tweet, delete_tweet
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Twitter Assistant")

@mcp.tool()
def post_to_twitter(text: str) -> str:
    return post_tweet(text)

@mcp.tool()
def reply_to_twitter(tweet_id: str, text: str) -> str:
    return reply_to_tweet(tweet_id, text)

@mcp.tool()
def delete_from_twitter(tweet_id: str) -> str:
    return delete_tweet(tweet_id)

@mcp.prompt()
def post_prompt(content: str) -> str:
    return f"Post the following tweet: {content}"

@mcp.prompt()
def reply_prompt(tweet_id: str, reply: str) -> str:
    return f"Reply to tweet {tweet_id} with: {reply}"

if __name__ == "__main__":
    mcp.run()
