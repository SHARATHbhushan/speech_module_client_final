from voxpopuli import Voice
import voxpopuli
import pyaudio
import wave
import time
import sys

from array import array
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 41000
voice = Voice(lang="us", pitch=60, speed=120, voice_id=1)
'''
voice = Voice(lang="en", pitch=90, speed=50, voice_id=1)

voice.say("hello how are you doing")

voice.say("hello how are you doing")
while not voxpopuli.main.AudioPlayer.play:
    print("playing audio ")
print("complete")
'''
import pyflite
import subprocess
p = pyaudio.PyAudio()
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
from struct import *
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
        #wav = voice.to_audio(phrase)  
        pyflite.init()

        x = pyflite.select_voice("src/tts/src/pyflite/cmu_us_rms.flitevox")
        y = pyflite.text_to_wave(phrase, x);
        samples = array('h', y['samples'])
        with open("sound.raw", 'wb') as f:
            samples.tofile(f)
                
        with open("sound.raw", "rb") as inp_f:
            data = inp_f.read()
            with wave.open("sound.wav", "wb") as out_f:
                out_f.setnchannels(1)
                out_f.setsampwidth(2) # number of bytes
                out_f.setframerate(20000)
                out_f.writeframesraw(data)
        wf = wave.open("sound.wav", 'rb')
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)
        data = wf.readframes(CHUNK)
        while len(data):
            stream.write(data)
            data = wf.readframes(CHUNK)

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
