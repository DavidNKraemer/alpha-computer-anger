import tweepy
from time import sleep
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

df = open('days.txt', 'r')
days = int(df.read().strip())
df.close()

df = open('days.txt', 'w')
df.truncate()
df.write("{}\n".format(days + 1))
df.close()

complaint = (
        "@alpha_computer It's been {} days, and " \
        "@david_kraemer STILL hasn't received the right laptop. " \
        "Why is your customer service so awful?").format(days)

api.update_status(status=complaint)

