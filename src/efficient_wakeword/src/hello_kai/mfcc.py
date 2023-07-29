import librosa
import librosa.display
import matplotlib.pyplot as plt
audio_path='./hello kai_en-US_OliviaV3Voice.mp3' #location
(xf, sr) = librosa.load(audio_path)    
mfccs = librosa.feature.mfcc(y=xf, sr=sr, n_mfcc=4)
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.tight_layout()
plt.title('mfcc')
plt.savefig('record7_mfcc.png')
plt.show