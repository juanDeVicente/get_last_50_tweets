#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Clase que permite contar las palabras de los útlimos tweets
"""

from src.word_count import word_count
from functools import reduce

import twitter
import os

ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''


class twitter_word_count(object):

    def __init__(self, api):
        self.api = api

    def get_last_n_tweets(self, screen_name=None):
        return [tweet.text for tweet in
                self.api.GetUserTimeline(screen_name=screen_name, count=200, include_rts=False, exclude_replies=True)[
                0:50]]

    def get_words_of_tweets(self, screen_name=None):
        tweets = self.get_last_n_tweets(screen_name)
        tweets = reduce((lambda x, y: x + ', ' + y), tweets)
        return word_count(tweets, stopwords_language='spanish')[0:20]


if __name__ == "__main__":
    try:
        ACCESS_TOKEN_KEY = os.environ['ACCESS_TOKEN_KEY']
        ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
        CONSUMER_KEY = os.environ['CONSUMER_KEY']
        CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
    except KeyError:
        print('No se ha establecido algun parametro para conectar con la api de Twitter')
        exit(-1)

    print(ACCESS_TOKEN_KEY)
    print(ACCESS_TOKEN_SECRET)
    print(CONSUMER_KEY)
    print(CONSUMER_SECRET)

    api = twitter.Api(
        CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
    )
    screen_name = '_lalusi'  # Aqui va le nombre de la cuenta que queramos mirar (Arturo Perez Reverte) Si es None, devuelve los del usuario a los que este asociado la cuenta
    twc = twitter_word_count(api)

    print(twc.get_words_of_tweets(screen_name))
