from voxpopuli import Voice
import voxpopuli
import pyaudio
import wave
import time
import sys
CHUNK = 1024
voice = Voice(lang="us", pitch=60, speed=120, voice_id=1)
'''
voice = Voice(lang="en", pitch=90, speed=50, voice_id=1)

voice.say("hello how are you doing")

voice.say("hello how are you doing")
while not voxpopuli.main.AudioPlayer.play:
    print("playing audio ")
print("complete")
'''
p = pyaudio.PyAudio()
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool

class tts_engine():

    def __init__(self):
        rospy.Subscriber("tts/phrase", String, self.callback)
        self.pubStatus = rospy.Publisher('/stt_session_key', Bool, queue_size=0)
        
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
        self.pubStatus.publish(False)
        start_time = time.time()
        wav = voice.to_audio(phrase)
        with open("response.wav", "wb") as wavfile:
            wavfile.write(wav)
        wf = wave.open("response.wav", 'rb')
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
        data = wf.readframes(CHUNK)
        while len(data):
            stream.write(data)
            data = wf.readframes(CHUNK)
        end_time = time.time()
        time_dif = end_time - start_time
        print(time_dif)
        #while not voxpopuli.main.AudioPlayer.play:
        #    time.sleep(0.3)
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
