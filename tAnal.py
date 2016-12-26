import tweepy
import numpy
from textblob import TextBlob
#from flask import Flask, render_template

#app = Flask(__name__)

# index view function suppressed for brevity

def sem_Anal():
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
    public_tweets = api.search(q="Trump", count=5, lang='en')
    # t_list = api.create_list(public_tweets)
    count = 0
    l = []
    # print "the number of tweets is" + public_tweets.count
    for tweet in public_tweets:
        count = count + 1
        print str(count) + ". " + (tweet.text)

        #Sentiment analysis using textBlob
        analysis = TextBlob(tweet.text)
        l.append(analysis.polarity)
        print(analysis.sentiment)
        print("")

    mean_polarity = numpy.mean(l)

    #classify based on polarity - range: [-1,1]
    # very positive - [0.5, 1]
    # moderately positive - [0.5, 0]
    # very negative - [-0.5,0]
    # negative - [-1, -0.5]
    #
    # very_pos_range = numpy.arange(0.5, 1)
    # pos_range = numpy.arange(0, 0.5)
    # neg_range = numpy.arange(-0.5, 0)
    # very_neg_range = numpy.arange(-1, -0.5)


    print mean_polarity
    if 0.5 <= mean_polarity <= 1:
        print "very positive"
    if  0 <= mean_polarity <= 0.5:
        print "neutral"
    if  -0.5 <= mean_polarity <= 0:
        print "moderately negative"
    if  -1 <= mean_polarity <= -0.5:
        print "very negative"


# @app.route('/')
# def index():
#     return render_template('template.html', title='Home', user='Lohit')

if __name__ == '__main__':
  # app.run(debug=True)
  sem_Anal()
