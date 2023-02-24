import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists
from tools.logging import logger
from things.actors import actor
import random
import json
import pickle
import datetime
from pprint import pformat

from tools.nlp import *

CORPUS = {}

with open('chatbot_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

input_message = ''

def get_response(act, message):
    input_message = message
    response = 'NOT FOUND'

    if message in CORPUS['input']:
        response = random.choice(CORPUS['input'][input_message])
    else:
        response = generate(message)
        with open('chatbot_corpus.json', 'w') as myfile:
            myfile.write(json.dumps(CORPUS, indent=4 ))
    
    return response

def generate(message):
    response = 'Response generation failed.'

    # Get message sentiment score
    polarity_scores = get_polarity_scores(message)
    print("Polarity scores: ", polarity_scores)
    message_sentiment = get_message_sentiment(message)
    pos_tags = get_pos_tags(message)
    print(pos_tags)

    # Determine next path based on message sentiment
    if message_sentiment == SentimentType.POSITIVE:
        print("The message is positive")
        response = positive_response(message)
    elif message_sentiment == SentimentType.NEGATIVE:
        print("The message is negative")
        response = negative_response(message)
    else:
        print("The message is neutral")
        response = neutral_response(message)

    # Send response to webhook
    return response

def negative_response(message):
    response = 'negative'

    if "you" in message:
        response = random.choice(CORPUS['negative']['you'])

    return response

def neutral_response(message):
    response = 'neutral'


    return response

def positive_response(message):
    response = 'positive'

    
    return response

# For reference might use a data structure like this later so that multiple inputs can represent
# one input into the corpus
# pairs = [
#     # Greetings
#     (r"hi|hello|hey", ["Hello, dear.", "Hi there!", "Howdy!"]),
#     (r"how are you", ["I'm doing well, thank you for asking. How about you?"]),
#     (r"fine|good", ["That's great to hear."]),
#     (r"not (good|well|fine)", ["Oh, I'm sorry to hear that. Is there anything I can do to help?"]),
    
#     # Age-related topics
#     (r"how old are you", ["Oh my, I'm quite old! I've lost count of my years."]),
#     (r"what's your age", ["Well, let's just say I've been around for quite some time."]),
#     (r"grandchild|grandchildren", ["Yes, I have many grandchildren. They bring me so much joy."]),
#     (r"memory|remember", ["My memory isn't what it used to be, but I still cherish the memories I have."]),
    
#     # Farewells
#     (r"bye|goodbye", ["Goodbye, dear. Take care!"]),
#     (r"thank you", ["You're welcome, dear. Anytime."]),
#     (r"thanks", ["You're welcome, dear. Take care!"])
# ]
