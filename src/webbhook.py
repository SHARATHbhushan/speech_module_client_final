# import flask dependencies 
from dataclasses import dataclass
from email import message
from urllib import response
import eventlet
import json
from os import popen
from flask import Flask, request, make_response, jsonify 
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
import time
eventlet.monkey_patch()


# initialize the flask app 
app = Flask(__name__) 
app.config['SECRET'] = 'my secret key'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['MQTT_BROKER_URL'] = '192.168.192.89'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'Ohmni'
app.config['MQTT_PASSWORD'] = 'root'
app.config['MQTT_KEEPALIVE'] = 5
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_CLEAN_SESSION'] = True

try :
	mqtt = Mqtt(app)
	socketio = SocketIO(app)
	bootstrap = Bootstrap(app)
except:
	pass
	print("connection to raspberry pi home failed, please switch on raspberry pi")
 # default route 
@app.route('/') 
def index(): 
	return 'Hello World!'

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
	print("mqtt connected")
@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
	payload=message.payload.decode()
	print(payload)
	with open('message.txt', 'r+') as f:
		f.seek(0)
		f.write(payload)
		f.truncate()  

# function for responses 
def results(): 
	# build a request object 
	data = ""
	req = request.get_json(force=True) 
	req_json = json.dumps(req)
	print(req_json)
	# fetch action from json
	action = req.get('queryResult').get('action') 
	param = req.get('queryResult').get('parameters') 
	request_1 = req.get('queryResult').get('queryText')
	#print(action)
	if action == "email":
		mqtt.publish('home/mail', req_json)
	elif action == "TurnLights":
		mqtt.publish('/home/request', action+param.get('OnOff'))
		print(param.get('OnOff'))
	else: 
		mqtt.publish('/home/request', action)
	mqtt.subscribe('/home/response')
	time.sleep(1)
	with open('message.txt', 'r+') as f:
		data = f.read().rstrip()
		f.seek(0)
		f.write("None")
		f.truncate()   
	print(data)
	return {'fulfillmentText': data }


	

# create a route for webhook 
@app.route('/webhook', methods=['GET', 'POST']) 
def webhook(): 
	# return response 
	return make_response(jsonify(results())) 

# run the app 
if __name__ == '__main__': 
	 socketio.run(app, host='0.0.0.0', port=8000, use_reloader=False, debug=False)
