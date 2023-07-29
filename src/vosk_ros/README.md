# The vosk_ros package
## Integrating VOSK in ROS for Speech Recognition with our robotics projects 😊
### Source code based on <https://github.com/alphacep/vosk-api/blob/master/python/example/test_microphone.py> from VOSK's python example code


### How to install..
#### Download it to the src folder of your catkin workspace
#### don't forget to run `catkin_make`

### Depends on: 
#### If using ROS MELODIC run first: 
`$sudo apt install python3-pip python3-yaml`
#### Then run for MELODIC & NOETIC: 
`$pip3 install sounddevice`
`$pip3 install vosk`
#### And if you want to use the TTS engine please run: 
`$sudo apt install espeak`
`$pip install pyttsx3`


### Package's Structure: 
#### Topics:
* speech_recognition/vosk_result    -> vosk_node.py publishes a custom "speech_recognition" message
* speech_recognition/final_result   -> vosk_node.py publishes a simple string with the final result
* speech_recognition/partial_result -> vosk_node.py publishes a simple string with the partial result
* tts/status -> tts_engine.py publishes the state of the engine. True if it is speaking False if it is not. If the status is true vosk_node won't process the audio stream so it won't listen to itself 
* tts/phrase -> tts_engine.py subscribes to this topic in order to speake the given string. Name your desire and it shall be heard by all in the room..

#### run the package by: 
`roslaunch vosk_ros vosk_speech_recognition.launch`
#### or by:
`rosrun vosk_ros vosk_node`