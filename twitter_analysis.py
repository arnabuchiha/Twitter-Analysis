import tweepy
from textblob import TextBlob

consumer_key=	'yo8mYPmefJ82Lt5pqPz2JiteT'
consumer_secret='e8L7dsV5qiQOSbkj3iY6XW25DLh5RG0JQWkkhUX3wHzBFAdu5a'

access_token='4884998369-5dvP3ZYzrnBaa2DFBRT0RwSV8VUCz8oG3uJYOBq'
access_token_secret='MECbKyA141YaTvQIQG0OJKBOL9WmHEenMdzImT8jN6nbr'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('ISIS')

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")