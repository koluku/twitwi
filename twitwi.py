from dotenv import load_dotenv
import json
import os
from requests_oauthlib import OAuth1Session

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('ACCESS_TOKEN_SECRET')

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

tweet = input('Tweet: ')
params = {'status': tweet}
req = twitter.post('https://api.twitter.com/1.1/statuses/update.json', params = params)

if req.status_code != 200:
    print('Tweet was failed...')
else:
    print('Tweet was successfull!')