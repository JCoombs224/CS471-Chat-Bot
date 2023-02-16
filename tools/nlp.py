import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

from enum import Enum

from things.pos_tags import *

class SentimentType(Enum):
    NEUTRAL = 0
    POSITIVE = 1
    NEGATIVE = 2

# Create a function that returns the general sentiment of a message
def get_message_sentiment(message: str) -> SentimentType:
    sia = SentimentIntensityAnalyzer()
    polarity_scores = sia.polarity_scores(message)
    return greatest_sentiment(polarity_scores)

def greatest_sentiment(polarity_scores: dict) -> SentimentType:
    if polarity_scores['pos'] > polarity_scores['neg']:
        return SentimentType.POSITIVE
    elif polarity_scores['pos'] < polarity_scores['neg']:
        return SentimentType.NEGATIVE
    else:
        return SentimentType.NEUTRAL

def get_polarity_scores(message: str):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(message)


# pos = part of speech
def get_pos_tags(message: str):
    tokenized_message = nltk.word_tokenize(message)
    return nltk.pos_tag(tokenized_message)
