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

input_message = ""

def get_response(act, message):
    input_message = message
    response = 'NOT FOUND'

    if message in CORPUS['input']:
        response = random.choice(CORPUS['input'][input_message])
    else:
        response = generate()
        with open('chatbot_corpus.json', 'w') as myfile:
            myfile.write(json.dumps(CORPUS, indent=4 ))
    
    return response

def generate():
    response = 'Response generation failed.'

    # Get message sentiment score
    polarity_scores = get_polarity_scores(input_message)
    print("Polarity scores: ", polarity_scores)
    message_sentiment = get_message_sentiment(input_message)
    pos_tags = get_pos_tags(input_message)
    print(pos_tags)

    if message_sentiment == SentimentType.POSITIVE:
        print("The message is positive")
    elif message_sentiment == SentimentType.NEGATIVE:
        print("The message is negative")
        response = negative_response()
    elif message_sentiment == SentimentType.NEUTRAL:
        print("The message is neutral")


    return response

def negative_response():
    response = 'negative'

    if "you" in input_message:
        response = random.choice(CORPUS['negative']['you'])

    return response
