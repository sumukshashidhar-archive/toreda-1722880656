import sys
import json
import time
import re
import requests
import nltk
import argparse
import logging
import string

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse
from tweepy.streaming import StreamListener
from tweepy import API, Stream, OAuthHandler, TweepError
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup

from random import randint, randrange
from datetime import datetime
from newspaper import Article, ArticleException

from config import *

IS_PY3 = sys.version_info >= (3, 0)

if not IS_PY3:
    print("you need python3 for this to run")
    sys.exit(1)


# sentiment text-processing url
sentimentURL = 'http://text-processing.com/api/sentiment/'




# tweet id list
tweet_ids = []

# file to hold twitter user ids
twitter_users_file = './twitteruserids.txt'

prev_time = time.time()
sentiment_avg = [0.0,0.0,0.0]
