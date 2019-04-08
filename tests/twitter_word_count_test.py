#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from unittest.mock import MagicMock
from src.twitter_word_count import twitter_word_count


def test_example():
    twc = twitter_word_count(None)
    twc.get_last_n_tweets = MagicMock(return_value=['hola', 'que tal estas', 'pues yo muy bien'])
    assert twc.get_words_of_tweets() == [('hola', 1), ('tal', 1), ('pues', 1), ('bien', 1)]

