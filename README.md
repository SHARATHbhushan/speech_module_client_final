#Research Project on Implementation of Speech Module on Ohmni Telepresence Robot

This documents serves as a complete description to setup and start a speech module on ohmni robot 



Maintainer: Sharath Nataraj 
Email id: sharathnataraj7@gmail.com

# Filetree
# src

* [cogrob_chatbot/](./src/cogrob_chatbot)
  * [.rasa/](./src/cogrob_chatbot/.rasa)
    * [cache/](./src/cogrob_chatbot/.rasa/cache)
  * [actions/](./src/cogrob_chatbot/actions)
    * [__pycache__/](./src/cogrob_chatbot/actions/__pycache__)
    * [__init__.py](./src/cogrob_chatbot/actions/__init__.py)
    * [actions.py](./src/cogrob_chatbot/actions/actions.py)
  * [data/](./src/cogrob_chatbot/data)
    * [nlu.yml](./src/cogrob_chatbot/data/nlu.yml)
    * [rules.yml](./src/cogrob_chatbot/data/rules.yml)
    * [stories.yml](./src/cogrob_chatbot/data/stories.yml)
  * [models/](./src/cogrob_chatbot/models)
    * [20220926-120721-accepting-quarter.tar.gz](./src/cogrob_chatbot/models/20220926-120721-accepting-quarter.tar.gz)
  * [tests/](./src/cogrob_chatbot/tests)
    * [test_stories.yml](./src/cogrob_chatbot/tests/test_stories.yml)
  * [config.yml](./src/cogrob_chatbot/config.yml)
  * [credentials.yml](./src/cogrob_chatbot/credentials.yml)
  * [domain.yml](./src/cogrob_chatbot/domain.yml)
  * [endpoints.yml](./src/cogrob_chatbot/endpoints.yml)
* [efficient_wakeword/](./src/efficient_wakeword)
  * [src/](./src/efficient_wakeword/src)
    * [hello_kai/](./src/efficient_wakeword/src/hello_kai)
    * [sample_refs/](./src/efficient_wakeword/src/sample_refs)
    * [__init__.py](./src/efficient_wakeword/src/__init__.py)
    * [audio_processing.py](./src/efficient_wakeword/src/audio_processing.py)
    * [baseModel.tflite](./src/efficient_wakeword/src/baseModel.tflite)
    * [effnet_word.py](./src/efficient_wakeword/src/effnet_word.py)
    * [engine.py](./src/efficient_wakeword/src/engine.py)
    * [generate_reference.py](./src/efficient_wakeword/src/generate_reference.py)
    * [ibm_generate.py](./src/efficient_wakeword/src/ibm_generate.py)
    * [logmelcalc.tflite](./src/efficient_wakeword/src/logmelcalc.tflite)
    * [package_installation_scripts.py](./src/efficient_wakeword/src/package_installation_scripts.py)
    * [streams.py](./src/efficiestartnt_wakeword/src/streams.py)
    * [tO_README](./src/efficient_wakeword/src/tO_README)
  * [CMakeLists.txt](./src/efficient_wakeword/CMakeLists.txt)
  * [package.xml](./src/efficient_wakeword/package.xml)
* [flask_ros_demo/](./src/flask_ros_demo)
  * [flask_demo/](./src/flask_ros_demo/flask_demo)
    * [launch/](./src/flask_ros_demo/flask_demo/launch)
    * [msg/](./src/flask_ros_demo/flask_demo/msg)
    * [scripts/](./src/flask_ros_demo/flask_demo/scripts)
    * [CMakeLists.txt](./src/flask_ros_demo/flask_demo/CMakeLists.txt)
    * [package.xml](./src/flask_ros_demo/flask_demo/package.xml)
    * [requirements.txt](./src/flask_ros_demo/flask_demo/requirements.txt)
  * [README.md](./src/flask_ros_demo/README.md)
* [porcupine_wake_word/](./src/porcupine_wake_word)
  * [src/](./src/porcupine_wake_word/src)
    * [kai_wake_word.py](./src/porcupine_wake_word/src/kai_wake_word.py)
  * [CMakeLists.txt](./src/porcupine_wake_word/CMakeLists.txt)
  * [To Readme.txt](./src/porcupine_wake_word/To Readme.txt)
  * [package.xml](./src/porcupine_wake_word/package.xml)
* [porcupine_wakeword_model/](./src/porcupine_wakeword_model)
  * [112b040e-7860-46d0-bf6e-2437c35ad026.zip](./src/porcupine_wakeword_model/112b040e-7860-46d0-bf6e-2437c35ad026.zip)
  * [a47f61cc-1c94-4869-99bf-0d88d98472d0.zip](./src/porcupine_wakeword_model/a47f61cc-1c94-4869-99bf-0d88d98472d0.zip)
* [rasa_ros/](./src/rasa_ros)
  * [launch/](./src/rasa_ros/launch)
    * [dialogue.xml](./src/rasa_ros/launch/dialogue.xml)
  * [scripts/](./src/rasa_ros/scripts)
    * [dialogue_interface.py](./src/rasa_ros/scripts/dialogue_interface.py)
    * [dialogue_server.py](./src/rasa_ros/scripts/dialogue_server.py)
    * [rasa_action.sh](./src/rasa_ros/scripts/rasa_action.sh)
    * [rasa_server.sh](./src/rasa_ros/scripts/rasa_server.sh)
  * [srv/](./src/rasa_ros/srv)
    * [Dialogue.srv](./src/rasa_ros/srv/Dialogue.srv)
  * [CMakeLists.txt](./src/rasa_ros/CMakeLists.txt)
  * [package.xml](./src/rasa_ros/package.xml)
* [tts/](./src/tts)
  * [src/](./src/tts/src)
    * [__pycache__/](./src/tts/src/__pycache__)
    * [nix/](./src/tts/src/nix)
    * [pyflite/](./src/tts/src/pyflite)
    * [.gitignore](./src/tts/src/.gitignore)
    * [LICENSE](./src/tts/src/LICENSE)
    * [README.md](./src/tts/src/README.md)
    * [ed_tts.py](./src/tts/src/ed_tts.py)
    * [espeak.py](./src/tts/src/espeak.py)
    * [mbrola.py](./src/tts/src/mbrola.py)
    * [nix-ljspeech-stochastic-v0.1-20220916T150228Z-001.zip](./src/tts/src/nix-ljspeech-stochastic-v0.1-20220916T150228Z-001.zip)
    * [nix.py](./src/tts/src/nix.py)
    * [pico.py](./src/tts/src/pico.py)
    * [requirements.txt](./src/tts/src/requirements.txt)
    * [sound.raw](./src/tts/src/sound.raw)
    * [test.py](./src/tts/src/test.py)
  * [CMakeLists.txt](./src/tts/CMakeLists.txt)
  * [package.xml](./src/tts/package.xml)
* [vosk_ros/](./src/vosk_ros)
  * [config/](./src/vosk_ros/config)
    * [params.yaml](./src/vosk_ros/config/params.yaml)
  * [launch/](./src/vosk_ros/launch)
    * [start_dialogflow_service.launch](./src/vosk_ros/launch/start_dialogflow_service.launch)
    * [start_rasa_service.launch](./src/vosk_ros/launch/start_rasa_service.launch)
  * [models/](./src/vosk_ros/models)
    * [vosk-model-small-en-us-0.15/](./src/vosk_ros/models/vosk-model-small-en-us-0.15)
  * [msg/](./src/vosk_ros/msg)
    * [speech_recognition.msg](./src/vosk_ros/msg/speech_recognition.msg)
  * [src/](./src/vosk_ros/src)
    * [tts_engine.py](./src/vosk_ros/src/tts_engine.py)
    * [vosk_node.py](./src/vosk_ros/src/vosk_node.py)
  * [CMakeLists.txt](./src/vosk_ros/CMakeLists.txt)
  * [README.md](./src/vosk_ros/README.md)
  * [package.xml](./src/vosk_ros/package.xml)
* [CMakeLists.txt](./src/CMakeLists.txt)
* [Ohmni_kai.zip](./src/Ohmni_kai.zip)
* [Our_data.db](./src/Our_data.db)
* [mailer.py](./src/mailer.py)
* [requirements.txt](./src/requirements.txt)
* [webbhook.py](./src/webbhook.py)

# Robot Setup

- pull this repo into robot by using linux shell follow instructions from : https://docs.ohmnilabs.com/

- `cd speech_module`

- `pip install -r src/requirements.txt`

**A google mail id has been created to manage multiple services for the robot**

**email id: ohmni.iaas@gmail.com**

**password: Ohmni@123@iaas**


This module allows you to choose between two wake word recognition models 1 and 2

## 1.Procupine Wake word Recognition Setup

- This repo contains pre-trained model in the folder  [porcupine_wakeword_model/](./src/porcupine_wakeword_model) Extract the contents and save it outside the repository since the model is quite big. 
- This model can be directly used to for inference from [kai_wake_word.py](./src/porcupine_wake_word/src/kai_wake_word.py)
- The path to extracted model can be passed while astarting the wake word, Remember the porcupine wake word must be started before launching the other nodes.
- picovoice console: https://console.picovoice.ai/signup
- Login through the given google account
- training and creating access key: https://picovoice.ai/docs/porcupine/


### launcing the Porcupine wake word
- working with pre-trained models: `rosrun porcupine_wake_word kai_wake_word.py --access_key 7segjTjkamk6oOQb/SLE8OBex4vHMdGxW+Z2cxX1EthTIJ13wNPnqg== --keyword_path path_to_extracted file/Hello-Kai_en_linux_v2_1_0.ppn`
- Custom trained model: `rosrun porcupine_wake_word kai_wake_word.py --access_key access_key_generated_from the previous steps --keyword_path path_to_extracted file/Hello-Kai_en_linux_v2_1_0.ppn`

## 2.Efficient Net Wake Word Recognition Setup


- some extra requirements, 
`pip install librosa && pip install ffmpeg`
- This repo also contains a pre-trained efficent-net model [sample_refs/](./src/efficient_wakeword/src/sample_refs), 
- remember to change the directorty path of the pre-trained model in **line 12** of [effnet_word.py](./src/efficient_wakeword/src/effnet_word.py)
- it is also possible to train a new wake word using the instructions https://github.com/Ant-Brain/EfficientWord-Net#generating-custom-wakewords
- simply replace json modle inside the sample_refs directory and change the directory path of newly trained model at **line 12** of [effnet_word.py](./src/efficient_wakeword/src/effnet_word.py)
- remember to run the wake word node before starting other nodes.
- node can be started by `rosrun efficient_wakeword effnet_word.py`
- `rostopic pub -1 /eff_wake_word_status std_msgs/String "data: 'on'"`


Next is the speech recognition models

by default this branch contains only vosk as STT model, switch to devel branch to find more models

## Vosk Speech Recognition Engine

- Vosk STT is pre-compiled with models and can be started easily with a simle command
- `rosrun vosk_ros vosk_node.py`


## Choosing Different NLU models

- This repository provides two differet NLU models which can be choosen by choosing different launch files in [launch/](./src/vosk_ros/launch)

### 1.Dialogflow Launch
- login to google cloud platform from the given google credentials
- create a servcice key using the email id given and sownload the json file: https://cloud.google.com/iam/docs/creating-managing-service-account-keys#iam-service-account-keys-create-console
- add this to bot environment shell by `export GOOGLE_APPLICATION_CREDENTIALS='/path_to_doownloaded_file/service_key.json'`
- `roslaunch vosk_ros start_dialogflow_service.launch`

### 2.RASA Launch
- navigate to [cogrob_chatbot/](./src/cogrob_chatbot) and start the rasa server 
- ` rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml --enable-api`
- `roslaunch vosk_ros start_rasa_service.lauch`
- this node is currently under development this can be used to get replies on the frontend but some features like apointment scheduling system and controlling IOT systems may not work, refer rasa docs to change  intents and rules inside [cogrob_chatbot/](./src/cogrob_chatbot)

# Quick start

## Robot Setup

- contact sharathnataraj@gmail.com for dialogflow service key.
- clone this repository onto the robo
- add the service key to evironment using `export GOOGLE_APPLICATION_CREDENTIALS='/path_to_doownloaded_file/service_key.json'`
- `catkin_make`
- `rosrun rosrun porcupine_wake_word kai_wake_word.py --access_key 7segjTjkamk6oOQb/SLE8OBex4vHMdGxW+Z2cxX1EthTIJ13wNPnqg== --keyword_path path_to_porcupine_model/Hello-Kai_en_linux_v2_1_0.ppn &`
- `roslaunch vosk_ros start_dialogflow_service.launch`
- this starts all the required nodes for the operation
 

## Local Setup


### Configuring Dialogflow service 
- this configuration can be made from a host computer and not on ohmni robot
- login to google dialogflow with the given credentials at the start of the readme file
- install ngrok: https://ngrok.com/download
- start ngrok service `ngrok http 8000` this connects dialogflow with webhook.py application
- copy the url generated and paste it in fullfilment section of dialogflow console with a route `/webhook`, the url looks like : www.example_url.com/webhook
- save the changes 
- the console can be used to add changes to intents



### Conecting to Home Assistant 

- Use the SD card provided with the deliverables, and insert it to Raspberry pi 4 with atleast 2GB of RAM, the SD card is configured to automatically connect to Service lab's WiFi. and boot Home Assistant.
- Check the IP adddress of Raspberry pi and make a note of it
- add the IP address of Raspberry pi in line 20 of [webbhook.py](./src/webbhook.py) and line 17 of [mailer.py](./src/mailer.py), mailer.py provides an example schema of how the employee database can be structured, more customization and development can be made to suite the needs.
- start both the applications `python3 webook.py` and `python3 mailer.py`
- setup of mailer.py is rather simple nacvigate to app passwords in google account setup and create a password with other application. copy and paste the password at line 15 of mailer.py
- This ensures mails can be  sent through this python script.





















