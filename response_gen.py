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

def generate(act, message):
    
    polarity_scores = get_polarity_scores(message)
    print("Polarity scores: ", polarity_scores)
    message_sentiment = get_message_sentiment(message)
    if message_sentiment == SentimentType.POSITIVE:
        print("The message is positive")
    elif message_sentiment == SentimentType.NEGATIVE:
        print("The message is negative")
    elif message_sentiment == SentimentType.NEUTRAL:
        print("The message is neutral")
    pos_tags = get_pos_tags(message)
    print(pos_tags)

    if message in CORPUS['input']:
        response = random.choice(CORPUS['input'][message])
    else:
        CORPUS['input'][message] = ['DID NOT FIND']
        with open('chatbot_corpus.json', 'w') as myfile:
            myfile.write(json.dumps(CORPUS, indent=4 ))

