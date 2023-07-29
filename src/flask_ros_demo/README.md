# Flask frontend for Ohmni robot 


# HOST
- start ros ws server in one terminal `roslaunch rosbridge_server rosbridge_websocket.launch `

- export dialogflow credentials `export GOOGLE_APPLICATION_CREDENTIALS='/home/acefly/speech_module/ohmni-kai-dnsm-c5c53b0f9e3d.json'`

- in the same terminal source devel/setup.bash and run `rosrun flask_demo server.py`

open browser at http://127.0.0.1:5000


# Client 
- run wake word recognition 

-  `rosrun efficient_wakeword effnet_word.py`  and in another terminal `rostopic pub -1 /eff_wake_word_status std_msgs/String "data: 'on'"`

or 

- `rosrun porcupine_wake_word kai_wake_word.py --access_key 7segjTjkamk6oOQb/SLE8OBex4vHMdGxW+Z2cxX1EthTIJ13wNPnqg== --keyword_path /home/acefly/porcupine/resources/keyword_files/linux/Hello-Kai_en_linux_v2_1_0.ppn` 

and in another terminal `rostopic pub -1 /session_key std_msgd/String "data:on"`



- run voice recognition nodde

- `rosrun vosk_ros vosk_node.py `


# to run RASA : 

- in speech module go to cogbot_chatbot and start the server using `rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml --enable-api`

- make sure rasa is already installed and init is completed in cogbot_chatbot