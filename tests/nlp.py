from tools.nlp import *


def exec_nlp_tests():
    message = "I like your shoes"
    print(get_polarity_scores(message))
    print(get_pos_tags(message))

    positive_message = "I like your shoes"
    negative_message = "I hate your shoes"
    neutral_message = "Your shoes are red"
    assert(get_message_sentiment(message) == SentimentType.POSITIVE)
    print("Positive message test passed")
    assert(get_message_sentiment(negative_message) == SentimentType.NEGATIVE)
    print("Negative message test passed")
    assert(get_message_sentiment(neutral_message) == SentimentType.NEUTRAL)
    print("Neutral message test passed")

