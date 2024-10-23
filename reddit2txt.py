from reddit2text import Reddit2Text
import argparse
import os
from dotenv import load_dotenv

print("stehos")

# Load environment variables from .env file
load_dotenv()

# Get Reddit API credentials from environment variables
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
user_agent = os.getenv('REDDIT_USER_AGENT')

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description='Get text from a Reddit post.')
parser.add_argument('url', type=str, help='The URL of the Reddit post to textualize.')

args = parser.parse_args()

r2t = Reddit2Text(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Get the URL from the command-line argument
URL = args.url

# Textualize the Reddit post
output = r2t.textualize_post(URL)
print(output)
