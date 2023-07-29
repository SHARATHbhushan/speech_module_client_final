import espeakng
import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool

class tts_engine():

    def __init__(self):
        rospy.Subscriber("tts/phrase", String, self.callback)
        self.pubStatus = rospy.Publisher('/stt_session_key', Bool, queue_size=0)
        self.mySpeaker = espeakng.Speaker()

    def callback(self, msg):
        phrase = msg.data
        self.app(phrase)
    
    def publish_status(self, isSpeaking):
        # Make the status true if it is speaking and false if it is not
        if isSpeaking == True:
            self.pubStatus.publish(False)
            rospy.logdebug("Started Speaking!")
        else:
            self.pubStatus.publish(True)
            rospy.logdebug("Finished Speaking..")
    
    def app(self, phrase):
        
        rospy.loginfo("The robot says: " + phrase)
        self.mySpeaker.pitch = 500
        self.mySpeaker.wpm = 150
        self.voice = 'en'
        start_time = time.time()
        self.mySpeaker.say(phrase)
        if self.mySpeaker.is_talking:
            self.pubStatus.publish(False)
        self.mySpeaker.wait()
        end_time = time.time()
        time_dif = end_time - start_time
        print(time_dif)
        time.sleep(0.3)
        if phrase.lower() == "speak to you soon":
            self.pubStatus.publish(False)
        else:
            self.pubStatus.publish(True)
   
if __name__ == '__main__':
    try:
        rospy.init_node('tts_engine', anonymous=True)
        tts = tts_engine()
        rospy.spin() 
    except KeyboardInterrupt:
        rospy.loginfo("Stopping tts engine...")
        rospy.sleep(1)
        print("node terminated")