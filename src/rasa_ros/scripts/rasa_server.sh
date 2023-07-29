#!/bin/bash

BOT_DIR="/home/acefly/speech_module/src/cogrob_chatbot"

cd $BOT_DIR

rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml --enable-api
