#Rohan Lekhwani
#Completed on - 10/11/18

import tweepy
from textblob import TextBlob

#Add Consumer Key and Consumer Secret from https://developer.twitter.com
consumer_key = ''
consumer_secret = ''

#Add Access Token and Access Token Secret from https://developer.twitter.com
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Mark Zuckerberg')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
