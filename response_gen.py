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
import re
from pprint import pformat

from tools.nlp import *
import nltk
from nltk.chat.util import Chat, reflections
from chat_dictionary import pairs

CORPUS = {}

PROFANITIES = []

with open('chatbot_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())

with open('profanities.txt', 'r') as myfile:
    PROFANITIES = myfile.read().splitlines()

input_message = ''

def get_response(act, message):
    input_message = message
    response = 'NOT FOUND'

    # remove punctuation
    message = re.sub(r'[^\w\s]', '', message)

    #if message in CORPUS['input']:  
    #    response = random.choice(CORPUS['input'][input_message])
    #else:
        #response = generate(act, message)
        #with open('chatbot_corpus.json', 'w') as myfile:
        #    myfile.write(json.dumps(CORPUS, indent=4 ))

    response = generate(act, message)
    
    return response

def generate(act, message):
    response = ''

    # Get message sentiment score
    polarity_scores = get_polarity_scores(message)
    print("Polarity scores: ", polarity_scores)
    message_sentiment = get_message_sentiment(message)
    pos_tags = get_pos_tags(message)
    print(pos_tags)

    # Check for profanities. The chat bot will disregard any profane language entirely,
    # just like your grandmother.
    for word in PROFANITIES:
        if word in message:
            return random.choice(CORPUS['negative']['profanity'])

    chat = Chat(pairs, reflections)
    response = chat.respond(message)

    if response:
        #state = response.partition('#')[2]
        #response = response.partition('#')[0]

        if "SENTIMENT" in response:

            if response == "SENTIMENT to hear that, How can I help you?":
                if message_sentiment == SentimentType.POSITIVE:
                    response = response.replace("SENTIMENT", "Happy")
                elif message_sentiment == SentimentType.NEGATIVE:
                    response = response.replace("SENTIMENT", "I am sorry")
                else:
                    response = response.replace("SENTIMENT to hear that, ", "")

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

    if not response:
        response = random.choice(CORPUS['confused'])

    # Send response to webhook
    return response

def negative_response(message):
    response = 'negative'

    if "you" in message:
        response = random.choice(CORPUS['negative']['you'])

    return response

def neutral_response(message):
    response = ''

    #TODO: Respond to a neutral message here

    return response

def positive_response(message):
    response = ''

    #TODO: Respond to a positive message here

    return response

