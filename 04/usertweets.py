from collections import namedtuple
import csv
import os

import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET
from config import ACCESS_TOKEN, ACCESS_SECRET

DEST_DIR = 'data'
EXT = 'csv'
NUM_TWEETS = 100


class UserTweets(object):
    def __init__(self, handle='', max_id=None):
        self.API = self.api_interface()
        self.tweets = self.get_all_tweets_for_handle(handle, max_id)
        self.generate_csv_from_tweets(handle=handle)

    def api_interface(self):
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        return tweepy.API(auth)

    def get_all_tweets_for_handle(self, handle='', max_id=None):
        if max_id:
            return self.API.user_timeline(self.API.get_user(handle)._json['id'], count=100, max_id=max_id)    
        return self.API.user_timeline(self.API.get_user(handle)._json['id'], count=100)

    def generate_csv_from_tweets(self, handle=''):
        keys = self.tweets[0]._json.keys()
        with open(f"data/{handle}.csv", 'w') as output_file:
            dict_writer = csv.DictWriter(output_file, keys, extrasaction='ignore')
            dict_writer.writeheader()
            for tweet in self.tweets:
                dict_writer.writerows([tweet._json])

    def __len__(self):
        return len(self.tweets)

    def __getitem__(self, position):
        return self.tweets[position]


if __name__ == "__main__":

    for handle in ('pybites', 'bbelderbos'):
        print('--- {} ---'.format(handle))
        user = UserTweets(handle)
        for tw in user[:5]:
            print(tw)
        print()
