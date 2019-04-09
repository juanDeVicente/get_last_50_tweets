#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from unittest.mock import MagicMock
from src.twitter_word_count import twitter_word_count


def test_example():
    tweets = ['hola', 'que tal estas', 'pues yo muy bien']
    twc = twitter_word_count(None)
    twc.get_last_n_tweets = MagicMock(return_value=tweets)
    assert twc.get_words_of_tweets() == [('hola', 1), ('tal', 1), ('pues', 1), ('bien', 1)]


def test_quijote():
    tweets = ['En un lugar de la Mancha, de cuyo nombre no quiero acordarme,',
              'o ha mucho tiempo que vivía un hidalgo de los de lanza en astillero,', 'adarga antigua, rocín flaco',
              ' y galgo corredor', 'Una olla de algo más vaca que carnero, ',
              'salpicón las más noches, duelos y quebrantos los sábados,', 'sábados', 'y lentejas los viernes']
    twc = twitter_word_count(None)
    twc.get_last_n_tweets = MagicMock(return_value=tweets)
    print(twc.get_words_of_tweets())
    assert twc.get_words_of_tweets() == [('sábados', 2), ('lugar', 1), ('mancha', 1), ('cuyo', 1), ('nombre', 1),
                                         ('quiero', 1), ('acordarme', 1), ('tiempo', 1), ('vivía', 1), ('hidalgo', 1),
                                         ('lanza', 1), ('astillero', 1), ('adarga', 1), ('antigua', 1), ('rocín', 1),
                                         ('flaco', 1), ('galgo', 1), ('corredor', 1), ('olla', 1), ('vaca', 1)]


def test_none_tweets():
    tweets = []
    twc = twitter_word_count(None)
    twc.get_last_n_tweets = MagicMock(return_value=tweets)
    with pytest.raises(TypeError):
        twc.get_words_of_tweets()


def test_boolean():
    twc = twitter_word_count(None)
    twc.get_last_n_tweets = MagicMock(return_value=True)
    with pytest.raises(TypeError):
        twc.get_words_of_tweets()


def test_stop_words_tweet():
    tweets = ['ella el', 'nosotros y ellos', 'un una', 'unos', 'yo', 'tu tu', 'que', 'estas']
    twc = twitter_word_count(None)
    twc.get_last_n_tweets = MagicMock(return_value=tweets)
    assert twc.get_words_of_tweets() == []


def test_puntuation_marks():
    tweets = [',,,,', '....', '???', '!!!!', '¡¡¡¡¡', ';;;;', '::::::']
    twc = twitter_word_count(None)
    twc.get_last_n_tweets = MagicMock(return_value=tweets)
    assert twc.get_words_of_tweets() == []

