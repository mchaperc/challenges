import feedparser

NUM_PACKS_TO_REACH = 150000
PYPI = 'https://pypi.python.org/pypi'


feed = feedparser.parse('https://pypi.python.org/simple/')

print(feed)


def get_existing_packages_data():
    pass


if __name__ == "__main__":
    pass
