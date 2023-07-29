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
from rasa_ros.srv import Dialogue, DialogueResponse
import requests
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
    get_answer_url = 'http://localhost:5002/webhooks/rest/webhook'
    message = {
        "sender": 'bot',
        "message": input_text
    }
    def proto_message_to_dict(message):
        return json.loads(message)
    r = requests.post(get_answer_url, json=message)
    response = DialogueResponse()
    print(r)
    response.answer = ""
    for i in r.json():
        response.answer += i['text'] + ' ' if 'text' in i else ''
    print(response.answer)
    responses = {"message": response.answer
                    , "payload": None}
    return jsonify(responses)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug= True)