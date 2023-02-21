import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
import os
from tools.logging import logger
from things.actors import actor
import random
import json
import pickle
import datetime
from response_gen import generate
from pprint import pformat

from tools.nlp import *

yml_configs = {}

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

def handle_request():
    logger.debug(request.form)
    act = None

    # Check if the actor exists
    if os.path.exists( f"users/{request.form['From']}.pkl") :
        with open(f"users/{request.form['From']}.pkl", 'rb') as p:
            act = pickle.load(p) 
    else:
        act= actor(request.form['From'])

    # Save actor's message that was sent
    act.save_msg({'from': 'ACTOR', 'msg': request.form['Body'], 'timestamp': datetime.datetime.now()})

    response = 'NOT FOUND'

    # Parse sent input from actor
    sent_input = str(request.form['Body']).lower()

    response = generate(act, sent_input)

    # Save the chatbot's response to the actor
    act.save_msg({'from': 'CHATBOT', 'msg': response, 'timestamp': datetime.datetime.now()})

    # Log current response
    logger.debug(response)

    # Log message thread from current actor
    logger.info('Actor message thread:\n%s', pformat(act.prev_msgs))

    # Pickle the actor
    with open(f"users/{request.form['From']}.pkl", 'wb') as p:
        pickle.dump(act,p)

    message = g.sms_client.messages.create(
                     body=response,
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])
    
    return json_response( status = "ok" )




