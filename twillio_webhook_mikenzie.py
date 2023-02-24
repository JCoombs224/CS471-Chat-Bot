import yaml
from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from os.path import exists
############################
from os import getcwd

from tools.logging import logger
from things.actors import actor


import random
import json
import pickle
###################
import datetime


yml_configs = {}
BODY_MSGS = []
with open('config.yml', 'r') as yml_file:
    yml_configs = yaml.safe_load(yml_file)

CORPUS = {}

with open('new_corpus.json', 'r') as myfile:
    CORPUS = json.loads(myfile.read())


def handle_request():
    logger.debug(request.form)
    print(request.form)
    act = None

    #if the user has already texted the number before
    if exists( f"users/{request.form['From']}.pkl") :
        with open(f"users/{request.form['From']}.pkl", 'rb') as p:
            act = pickle.load(p)
            #if there is a fork in the state transition paths (user input matters)
            if type(CORPUS[act.state]['next_state']) != str: #user input determines what state we go to next
                found = False
                for next_state in CORPUS[act.state]['next_state']:
                    if (request.form['Body']).lower() == (next_state['input']).lower():
                        found = True
                        act.state = next_state['next_state']
                    if not found:
                        act.state = 'confused'
            else: #the program doesn't care what the user says and moves to the next sequential state
                act.state = (CORPUS[act.state]['next_state'])

    #this is the first time the phone number has texted the bot
    else:
        act= actor(request.form['From'])

    response = (CORPUS[act.state]['content'])
    act.save_msg({'from': 'CHATBOT', 'msg': response, 'timestamp': datetime.datetime.now()})
    act.save_msg({'from': 'ACTOR', 'msg': request.form['Body'], 'timestamp': datetime.datetime.now()})
    with open(f"users/{request.form['From']}.pkl", 'wb') as p:
        pickle.dump(act,p)




    #response = 'NOT FOUND'

#code for matching exact responses in the corpus
    #TODO: if no resonpse is found, bot defaults to rambling on about random stuff
    #if response = 'NOT FOUND'


    logger.debug(response)

    message = g.sms_client.messages.create(
                     body=response,
                     from_=yml_configs['twillio']['phone_number'],
                     to=request.form['From'])
    return json_response( status = "ok" )
