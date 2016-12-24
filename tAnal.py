import tweepy
from textblob import TextBlob

# Authenticate - later..
consumer_key = '...'
consumer_secret = '...'
access_token = '...'
access_token_secret = '...'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


#acess the tweepy with the auth details
api = tweepy.API(auth)

#Retrieve tweets
public_tweets = api.search('lohit')

for tweet in public_tweets:
    print(tweet.text)
    #Sentiment analysis using textBlob
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
