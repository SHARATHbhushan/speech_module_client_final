import soundfile as sf
import soundcard as sc

default_speaker = sc.default_speaker()
samples, samplerate = sf.read('response.raw')
samplerate = 44100
default_speaker.play(samples,44100)