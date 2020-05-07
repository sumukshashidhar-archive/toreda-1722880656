"""
(C) Sumuk Shashidhar
"""

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


def get_page_text(url):

    max_paragraphs = 10

    try:
        logger.debug(url)
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        html_p = soup.findAll('p')

        logger.debug(html_p)

        if html_p:
            n = 1
            for i in html_p:
                if n <= max_paragraphs:
                    if i.string is not None:
                        logger.debug(i.string)
                        yield i.string
                n += 1

    except requests.exceptions.RequestException as re:
        logger.warning("Exception: can't crawl web site (%s)" % re)
        pass

def clean_text(text):
    # clean up text
    text = text.replace("\n", " ")
    text = re.sub(r"https?\S+", "", text)
    text = re.sub(r"&.*?;", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = text.replace("RT", "")
    text = text.replace(u"…", "")
    text = text.strip()
    return text

def clean_text_sentiment(text):
    # clean up text for sentiment analysis
    text = re.sub(r"[#|@]\S+", "", text)
    text = text.strip()
    return text

def get_sentiment_from_url(text, sentimentURL):
    # get sentiment from text processing website
    payload = {'text': text}

    try:
        #logger.debug(text)
        post = requests.post(sentimentURL, data=payload)
        #logger.debug(post.status_code)
        #logger.debug(post.text)
    except requests.exceptions.RequestException as re:
        logger.error("Exception: requests exception getting sentiment from url caused by %s" % re)
        raise

    # return None if we are getting throttled or other connection problem
    if post.status_code != 200:
        logger.warning("Can't get sentiment from url caused by %s %s" % (post.status_code, post.text))
        return None

    response = post.json()

    neg = response['probability']['neg']
    pos = response['probability']['pos']
    neu = response['probability']['neutral']
    label = response['label']

    # determine if sentiment is positive, negative, or neutral
    if label == "neg":
        sentiment = "negative"
    elif label == "neutral":
        sentiment = "neutral"
    else:
        sentiment = "positive"

    return sentiment, neg, pos, neu

def sentiment_analysis(text):
    """Determine if sentiment is positive, negative, or neutral
    algorithm to figure out if sentiment is positive, negative or neutral
    uses sentiment polarity from TextBlob, VADER Sentiment and
    sentiment from text-processing URL
    could be made better :)
    Uploads sentiment to stocksight website.
    """

    # pass text into sentiment url
    if True:
        ret = get_sentiment_from_url(text, sentimentURL)
        if ret is None:
            sentiment_url = None
        else:
            sentiment_url, neg_url, pos_url, neu_url = ret
    else:
        sentiment_url = None

    # pass text into TextBlob
    text_tb = TextBlob(text)

    # pass text into VADER Sentiment
    analyzer = SentimentIntensityAnalyzer()
    text_vs = analyzer.polarity_scores(text)

    # determine sentiment from our sources
    if sentiment_url is None:
        if text_tb.sentiment.polarity < 0 and text_vs['compound'] <= -0.05:
            sentiment = "negative"
        elif text_tb.sentiment.polarity > 0 and text_vs['compound'] >= 0.05:
            sentiment = "positive"
        else:
            sentiment = "neutral"
    else:
        if text_tb.sentiment.polarity < 0 and text_vs['compound'] <= -0.05 and sentiment_url == "negative":
            sentiment = "negative"
        elif text_tb.sentiment.polarity > 0 and text_vs['compound'] >= 0.05 and sentiment_url == "positive":
            sentiment = "positive"
        else:
            sentiment = "neutral"

    # calculate average and upload to sentiment website
    if args.upload:
        if sentiment_url:
            neg_avg = (text_vs['neg'] + neg_url) / 2
            pos_avg = (text_vs['pos'] + pos_url) / 2
            neutral_avg = (text_vs['neu'] + neu_url) / 2
            upload_sentiment(neg_avg, pos_avg, neutral_avg)
        else:
            neg_avg = text_vs['neg']
            pos_avg = text_vs['pos']
            neutral_avg = text_vs['neu']
            upload_sentiment(neg_avg, pos_avg, neutral_avg)

    # calculate average polarity from TextBlob and VADER
    polarity = (text_tb.sentiment.polarity + text_vs['compound']) / 2

    # output sentiment polarity
    print("************")
    print("Sentiment Polarity: " + str(round(polarity, 3)))

    # output sentiment subjectivity (TextBlob)
    print("Sentiment Subjectivity: " + str(round(text_tb.sentiment.subjectivity, 3)))

    # output sentiment
    print("Sentiment (url): " + str(sentiment_url))
    print("Sentiment (algorithm): " + str(sentiment))
    print("Overall sentiment (textblob): ", text_tb.sentiment)
    print("Overall sentiment (vader): ", text_vs)
    print("sentence was rated as ", round(text_vs['neg']*100, 3), "% Negative")
    print("sentence was rated as ", round(text_vs['neu']*100, 3), "% Neutral")
    print("sentence was rated as ", round(text_vs['pos']*100, 3), "% Positive")
    print("************")

    return polarity, text_tb.sentiment.subjectivity, sentiment
