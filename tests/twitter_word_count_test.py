import pytest
from unittest.mock import MagicMock
from src.twitter_word_count import twitter_word_count


def basic_test():
    twc = twitter_word_count(None)
    twc.get_last_n_tweets = MagicMock(return_value=3)

    assert twc.get_words_of_tweets() == 3
