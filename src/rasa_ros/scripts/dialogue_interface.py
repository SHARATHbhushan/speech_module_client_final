#!/usr/bin/env python3


from tracemalloc import start
import rospy
from rasa_ros.srv import Dialogue, DialogueResponse
from std_msgs.msg import String
from std_msgs.msg import Bool
import time
class TerminalInterface():
    '''Class implementing a terminal i/o interface. 

    Methods
    - get_text(self): return a string read from the terminal
    - set_text(self, text): prints the text on the terminal

    '''
    def __init__(self):  
        rospy.Subscriber("speech_recognition/final_result", String, self.callback)
        self.pubStatus = rospy.Publisher('/tts/phrase', String, queue_size=0)

    def callback(self, data):

        message = data.data
        try:
            start_time = time.time()
            bot_answer = dialogue_service(message)
            self.pubStatus.publish(bot_answer.answer)
            end_time = time.time()
            time_diff = end_time - start_time
            print(time_diff)
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)
 

if __name__ == '__main__':
    try: 
        rospy.init_node('writing')
        tint = TerminalInterface()
        rospy.wait_for_service('dialogue_server')
        dialogue_service = rospy.ServiceProxy('dialogue_server', Dialogue)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass