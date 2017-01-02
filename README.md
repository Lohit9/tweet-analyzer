# Sentiment Analyzer for Twitter 

##Overview
The code uses the tweepy library to access the Twitter API and the TextBlob library to perform Sentiment Analysis on each Tweet. Given a topic we'll be able to see how positive or negative the most recent tweets are. 

##Demo

##Uses - Try these out!
* Can be used to see how positive or negative the tweets are, about a given celebrity(i.e for example we can check what people thinking about Trump over the past few days)

* Can be used to find out the general sentiment that customers feel after a product launch(i.e for example we can try checking what people Apple AirPods)

* Assuming that your classmates use twitter, you can try to find out how they felt about your recent exam! 

##Dependencies
- tweepy
- TextBlob
- LingPipe

Install missing dependencies using [pip](https://pip.pypa.io/en/stable/installing/)

##Usage
Once you have your dependencies installed via pip, run the script in terminal via

```
python tAnal.py
```
To analyze a custom topic, open up the `tAnal.py` file and change the demo topic string variable i.e `q="Trump"`
