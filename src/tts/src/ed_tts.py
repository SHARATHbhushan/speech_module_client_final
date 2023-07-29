import asyncio
import email
import tempfile
from tracemalloc import start
import soundfile
from playsound import playsound
import wave
import edge_tts 
import pyaudio
import librosa
import soundfile as sf  
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
import time
p = pyaudio.PyAudio()
CHUNK = 1024
class tts_engine():
    import asyncio
    def __init__(self):
        rospy.Subscriber("tts/phrase", String, self.callback)
        self.pubStatus = rospy.Publisher('/stt_session_key', Bool, queue_size=0)
        self.asynci = asyncio.get_event_loop()

    def callback(self, msg):
        phrase = msg.data
        self.app(phrase)
        
    async def main(phrase):
        """
        Main function
        """

        communicate = edge_tts.Communicate()
        ask = phrase
        start_time = time.time()
        with open('response.wav', 'wb') as temporary_file:
            async for i in communicate.run(ask, voice="Microsoft Server Speech Text to Speech Voice (en-US, GuyNeural)"):
                if i[2] is not None:
                    temporary_file.write(i[2])
            #sd.play(temporary_file.name, 44100)
            print(temporary_file.name)
            x,_ = librosa.load(temporary_file.name, sr=16000)
            sf.write('tmp.wav', x, 16000)
            wave.open('tmp.wav','r')

            # Now try to open the file with wave
            wf = wave.open("tmp.wav", 'rb')
            
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

            '''
            with open("response.raw", "rb") as inp_f:
                data = inp_f.read()
                with wave.open("sound.wav", "wb") as out_f:
                    out_f.setnchannels(1)
                    out_f.setsampwidth(2) # number of bytes
                    out_f.setframerate(44100)
                    out_f.writeframesraw(data)
            '''
            #playsound(temporary_file.name)
        print("worked")

    
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
        self.asynci.run_until_complete(tts_engine.main(phrase))
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