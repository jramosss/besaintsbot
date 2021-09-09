from utils import sliceTweet
import tweepy as tw
from os import environ
from dotenv import load_dotenv

load_dotenv('.env')

KEY = environ["API_KEY"]
SECRET = environ["API_SECRET_KEY"]
ACCESS_TOKEN = environ["ACCESS_TOKEN"]
ACCESS_SECRET = environ["ACCESS_TOKEN_SECRET"]

auth = tw.OAuthHandler(KEY,SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tw.API(auth)

def getTweetID (response):
    return response._json["id_str"]

def tweetLongTweet (text : str):
    slices = sliceTweet(text)
    first = True
    prev_id = 0
    for s in slices:
        if first:
            prev_id = getTweetID(api.update_status(s)) 
            first = False
        else:
            prev_id = getTweetID(api.update_status(status=s,in_reply_to_status_id=prev_id)) 

def tweet (text):
    return api.update_status(text)