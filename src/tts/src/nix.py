#import pyflite
import subprocess
import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Bool
from struct import *
#from nix.models.TTS import NixTTSInference
import pyaudio
import wave
p = pyaudio.PyAudio()
chunk = 1024  

import soundfile as sf

# Regex
import re

# Phonemizer
from phonemizer.backend import EspeakBackend
phonemizer_backend = EspeakBackend(
    language = 'en-us',
    preserve_punctuation = True,
    with_stress = True
)

class NixTokenizerEN:

    def __init__(
        self,
        tokenizer_state,
    ):
        # Vocab and abbreviations dictionary
        self.vocab_dict = tokenizer_state["vocab_dict"]
        self.abbreviations_dict = tokenizer_state["abbreviations_dict"]

        # Regex recipe
        self.whitespace_regex = tokenizer_state["whitespace_regex"]
        self.abbreviations_regex = tokenizer_state["abbreviations_regex"]

    def __call__(
        self,
        texts,
    ):
        # 1. Phonemize input texts
        phonemes = [ self._collapse_whitespace(
            phonemizer_backend.phonemize(
                self._expand_abbreviations(text.lower()),
                strip = True,
            )
        ) for text in texts ]

        # 2. Tokenize phonemes
        tokens = [ self._intersperse([self.vocab_dict[p] for p in phoneme], 0) for phoneme in phonemes ]

        # 3. Pad tokens
        tokens, tokens_lengths = self._pad_tokens(tokens)

        return tokens, tokens_lengths, phonemes

    def _expand_abbreviations(
        self,
        text
    ):
        for regex, replacement in self.abbreviations_regex:
            text = re.sub(regex, replacement, text)

        return text

    def _collapse_whitespace(
        self,
        text
    ):
        return re.sub(self.whitespace_regex, ' ', text)

    def _intersperse(
        self,
        lst,
        item,
    ):
        result = [item] * (len(lst) * 2 + 1)
        result[1::2] = lst
        return result

    def _pad_tokens(
        self,
        tokens,
    ):
        tokens_lengths = [len(token) for token in tokens]
        max_len = max(tokens_lengths)
        tokens = [token + [0 for _ in range(max_len - len(token))] for token in tokens]
        return tokens, tokens_lengths

import os
import pickle
import timeit

import numpy as np
import onnxruntime as ort

#from nix.tokenizers.tokenizer_en import NixTokenizerEN

class NixTTSInference:

    def __init__(
        self,
        model_dir,
    ):
        # Load tokenizer
        self.tokenizer = NixTokenizerEN(pickle.load(open(os.path.join(model_dir, "tokenizer_state.pkl"), "rb")))
        # Load TTS model
        self.encoder = ort.InferenceSession(os.path.join(model_dir, "encoder.onnx"))
        self.decoder = ort.InferenceSession(os.path.join(model_dir, "decoder.onnx"))

    def tokenize(
        self,
        text,
    ):
        # Tokenize input text
        c, c_lengths, phonemes = self.tokenizer([text])

        return np.array(c, dtype = np.int64), np.array(c_lengths, dtype = np.int64), phonemes

    def vocalize(
        self,
        c,
        c_lengths,
    ):
        """
        Single-batch TTS inference
        """
        # Infer latent samples from encoder
        z = self.encoder.run(
            None,
            {
                "c": c,
                "c_lengths": c_lengths,
            }
        )[2]
        # Decode raw audio with decoder
        xw = self.decoder.run(
            None,
            {
                "z": z,
            }
        )[0]

        return xw


'''
nix = NixTTSInference(model_dir = "/home/acefly/speech_module_client/src/tts/src/nix-ljspeech-stochastic-v0.1")
# Tokenize input text
c, c_length, phoneme = nix.tokenize("hello I am ohmni, I am a service robot")
# Convert text to raw speech
xw = nix.vocalize(c, c_length)

# Listen to the generated speech
#Audio(xw[0,0], rate = 22050)
sf.write("test.wav", xw[0,0], 22050) 
f = wave.open("test.wav","rb") 
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  

#play stream  
while data:  
    stream.write(data)  
    data = f.readframes(chunk)  

#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate()  

'''

from array import array
CHUNK = 1024
FORMAT = pyaudio.paInt16
RATE = 41000
# voice = Voice(lang="us", pitch=60, speed=120, voice_id=1)
'''
voice = Voice(lang="en", pitch=90, speed=50, voice_id=1)

voice.say("hello how are you doing")

voice.say("hello how are you doing")
while not voxpopuli.main.AudioPlayer.play:
    print("playing audio ")
print("complete")
'''

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
        
        nix = NixTTSInference(model_dir = "/home/acefly/nix-tts/nix-ljspeech-stochastic-v0.1")
        # Tokenize input text
        c, c_length, phoneme = nix.tokenize(phrase)
        # Convert text to raw speech
        xw = nix.vocalize(c, c_length)

        # Listen to the generated speech
        #Audio(xw[0,0], rate = 22050)
        start_time = time.time()
        sf.write("test.wav", xw[0,0], 22050)
        time.sleep(0.5)
        wf = wave.open("test.wav", 'rb')
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
        time.sleep(3)
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
