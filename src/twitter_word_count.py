#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Downloads all tweets from a given user.
Uses twitter.Api.GetUserTimeline to retreive the last 3,200 tweets from a user.
Twitter doesn't allow retreiving more tweets than this through the API, so we get
as many as possible.
t.py should contain the imported variables.
"""

from __future__ import print_function

import twitter
import os

ACCESS_TOKEN_KEY = ''
ACCESS_TOKEN_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''


def get_last_n_tweets(api=None, screen_name=None, n_tweets=50):
    return api.GetUserTimeline(screen_name=screen_name, count=n_tweets)


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
    screen_name = 'perezreverte'  # Aqui va le nombre de la cuenta que queramos mirar (Arturo Perez Reverte) Si es None, devuelve los del usuario a los que este asociado la cuenta
    tweets = get_last_n_tweets(api=api, screen_name=screen_name, n_tweets=50)

    print([tweet for tweet in tweets])
