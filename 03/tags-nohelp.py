from collections import Counter
from difflib import SequenceMatcher

import feedparser

TOP_NUMBER = 10
RSS_FEED = feedparser.parse('https://pybit.es/feeds/all.rss.xml')
SIMILAR = 0.87


def get_tags():
    return Counter([tag['term'] for entry in RSS_FEED.entries for tag in entry['tags']])

def get_top_tags(tags):
    return tags.most_common(TOP_NUMBER)


def get_similarities(tags):
    similar_tags = {}
    for tag in tags:
        for nested_tag in tags:
            if tag != nested_tag and SequenceMatcher(None, tag, nested_tag).ratio() >= SIMILAR and tag not in similar_tags and nested_tag not in similar_tags:
                similar_tags[tag] = nested_tag
    return similar_tags


if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
