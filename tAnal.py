import tweepy
from textblob import TextBlob

# Authenticate - later..
consumer_key = 'XEV3Vkx1I1Y7HwkhhBUHafGpM'
consumer_secret = 'GlH30jB0cVvYHmbUoryxPS1QWK1fI9V7RtiMlhmQHr3dKctnoY'
access_token = '3024576532-wmVGY9UttsDdCKISqpz9whdRRcRtLyr8U3eqTSI'
access_token_secret = 'Yf2bbCzsFanISpKy5iws7qTd55X2YduXY0CvvgpNyl9p9'

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