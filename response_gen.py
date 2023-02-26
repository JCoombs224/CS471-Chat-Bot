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
import nltk
from nltk.chat.util import Chat, reflections
from chat_dictionary import pairs

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
        response = generate(act, message)
        #with open('chatbot_corpus.json', 'w') as myfile:
        #    myfile.write(json.dumps(CORPUS, indent=4 ))
    
    return response

def generate(act, message):
    response = ''

    # Get message sentiment score
    polarity_scores = get_polarity_scores(message)
    print("Polarity scores: ", polarity_scores)
    message_sentiment = get_message_sentiment(message)
    pos_tags = get_pos_tags(message)
    print(pos_tags)

    chat = Chat(pairs, reflections)
    response = chat.respond(message)

    if response:
        state = response.partition('#')[1]
        response = response.partition('#')[0]
        print(state)
        return response

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

    #TODO: Respond to a neutral message here

    return response

def positive_response(message):
    response = 'positive'

    #TODO: Respond to a positive message here

    return response

