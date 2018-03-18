####
#
# Twitter API querying, adapted from Joel Grus' great Data Science intro book
# https://github.com/joelgrus/data-science-from-scratch/blob/master/code-python3/getting_data.py
#
####
import json
import sys
import time
import tweepy
import tokenize

from collections import Counter
from tweepy import OAuthHandler
from twython import TwythonStreamer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from textblob import TextBlob

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

TWEET_TOPIC = sys.argv[1]
MAX_TWEETS = 1000
OUTPUT = 'data_{}.json'.format(int(time.time()))

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
 
api = tweepy.API(auth)

stop_words = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')


def get_tweets_by_search_term(term=""):
    if not term:
        return []
    return tweepy.Cursor(api.search, q=term).items(MAX_TWEETS)


def get_sentiment_of_tweets(tweets=[]):
    tweet_polarity = []
    for tweet in tweets:
        blob = TextBlob(tweet)
        tweet_polarity.append(blob.sentiment.polarity)
    return tweet_polarity


def determine_overall_sentiment(sentiments=[]):
    overall_sentiment = 0
    for sentiment in sentiments:
        overall_sentiment += sentiment
    return overall_sentiment / len(sentiments)


def tokenize_user_tweets(tweets=[]):
    sanitized_tweets = []
    for tweet in tweets:
        sanitized_tweet = []
        for word in tweet._json['text'].split(' '):
            if word.isalpha() and word.find('http') == -1 and word not in stop_words and len(word) > 2:
                sanitized_tweet.append(word)
        sanitized_tweets.append(' '.join(sanitized_tweet))
    return sanitized_tweets


if __name__ == "__main__":
    keywords_and = ' '.join(sys.argv[1:])

    print(determine_overall_sentiment(get_sentiment_of_tweets(tokenize_user_tweets(get_tweets_by_search_term(TWEET_TOPIC)))))
