#! /usr/bin/env python3

import os
from google.cloud import dialogflow
from flask import Flask, request, jsonify, render_template
from google.protobuf.json_format import MessageToDict
import json
import proto
import rospy
from std_msgs.msg import String
import threading
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import time
#speech_input = "test "
'''
def get_input(data):
    speech_input = data.data
    print(speech_input)
'''
# export GOOGLE_APPLICATION_CREDENTIALS='/home/acefly/speech_module/ohmni-kai-dnsm-c5c53b0f9e3d.json'



app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')


@app.route('/chat', methods=["Post"])
def chat():
    input_text = request.form['message']
    project_id = "ohmni-kai-dnsm"
    session_id = "101554181563138023613"
    language = "en-US"
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

    text_input = dialogflow.TextInput(text=input_text, language_code=language)

    query_input = dialogflow.QueryInput(text=text_input)
    start_time = time.time()
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    end_time = time.time()
    time_dif = end_time - start_time
    print(time_dif)
    def proto_message_to_dict(message: proto.Message) -> dict:
        return json.loads(message.__class__.to_json(message))
    
    result = proto_message_to_dict(response)

    print(result)
    if len(result['queryResult']['fulfillmentMessages']) == 2:
        response = {"message": result['queryResult']['fulfillmentText'],
                    "payload": result['queryResult']['fulfillmentMessages'][1]['payload']}
    else:
        response = {"message": result['queryResult']
                    ['fulfillmentText'], "payload": None}
    
    return jsonify(response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug= True)