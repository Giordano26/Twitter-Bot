import tweepy
import time
import datetime

auth = tweepy.OAuthHandler('','') # API HASH / API HASH CODE

auth.set_access_token('','') # Secret API hash / Secret API hash code

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True ) #wait on rate --> avoid getting limited by multiples requests

user = api.me()

search = '' # Word for the twitter action

nTweets = 100

for tweet in tweepy.Cursor(api.search,search).items(nTweets):
    try:
        tweet.retweet()
        timer = datetime.datetime.now()
        print("Retweeted")
        print(timer.hour,":",timer.minute,":",timer.second)
        time.sleep(480)
    except tweepy.TweepError as error:
        print(error.reason)
    except StopIteration:
        break