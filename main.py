from phrase import getPhrase
from tweet import tweet, tweetLongTweet
from time import time,sleep
from tweepy.error import TweepError
from pprint import pprint

#:)
DAY_IN_SECONDS = 86400.0

if __name__ == '__main__':
    starttime = time()
    while True:
        try:
            tweet(getPhrase())
        except TweepError as t:
            # This exception ocurrs if the same tweet is already tweeted
            # So we just let the day pass
            print("Taking the day off beacuse a tweet with that body is already posted ",t.__str__())
