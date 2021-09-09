from phrase import getPhrase
from tweet import tweet
from time import time
from tweepy.error import TweepError

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
