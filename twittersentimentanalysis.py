import tweepy
from textblob import TextBlob

consumer_key = 'Z3BGBjKgkL3ct6bk03TJ76ZF0'
consumer_secret = 'EvDBuHPFrvVEv51G4AoxCEt6YE6o8fQ92OgINKvDGJiu0X3oDI'

access_token = '119448626-DnhFwmDmuG1YrkeLMI22hizPpd1BMPnOK55dF8A7'
access_token_secret = 'P71ZdR6Ypsaou2LiVWWn5QllRGD9gYsV8OPalrjeRzjpY'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Mark Zuckerberg')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
