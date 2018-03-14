import sys
from collections import Counter

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

import spacy

import usertweets


stop_words = set(stopwords.words('english'))
tokenizer = RegexpTokenizer(r'\w+')
nlp = spacy.load('en')


def tokenize_user_tweets(tweets=[]):
    tweets = Counter(
                    tokenizer.tokenize(
                        ' '.join(
                            [word 
                                for tweet in tweets 
                                    for word in tweet._json['text'].split(' ') 
                                        if word.isalpha() and word.find('http') == -1 and word not in stop_words and len(word) > 2])))
    return [word for word in tweets if tweets[word] > 1]

def similar_tweeters(user1, user2):
    user1_tweets = nlp(' '.join(tokenize_user_tweets(usertweets.UserTweets(user1))))
    user2_tweets = nlp(' '.join(tokenize_user_tweets(usertweets.UserTweets(user2))))
    return user1_tweets.similarity(user2_tweets)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: {} <user1> <user2>'.format(sys.argv[0]))
        sys.exit(1)

    user1, user2 = sys.argv[1:3]
    similar_tweeters(user1, user2)
