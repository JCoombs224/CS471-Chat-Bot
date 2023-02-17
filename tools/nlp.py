import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

from enum import Enum

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
    if polarity_scores['pos'] > polarity_scores['neg'] and polarity_scores['pos'] > polarity_scores['neu']:
        return SentimentType.POSITIVE
    elif polarity_scores['neg'] > polarity_scores['pos'] and polarity_scores['neg'] > polarity_scores['neu']:
        return SentimentType.NEGATIVE
    return SentimentType.NEUTRAL

def get_polarity_scores(message: str):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(message)


# pos = part of speech
def get_pos_tags(message: str):
    tokenized_message = nltk.word_tokenize(message)
    return nltk.pos_tag(tokenized_message)
