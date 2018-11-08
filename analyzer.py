import numpy as np
import librosa
import environment as env
import utils
def voice_analyzer(filename):
    y,sr= librosa.load(filename, sr=22050)

    stft = np.abs(librosa.stft(y))
    mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40).T, axis=0)
    mel = np.mean(librosa.feature.melspectrogram(y, sr=sr).T, axis=0)
    contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sr).T, axis=0)
    tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(y), sr=sr).T, axis=0)
    chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sr).T,axis=0)
    features = np.hstack([mfccs,chroma,mel,contrast,tonnetz])
    features = features.reshape(1, -1)
    info = dict()

    myValue = utils.calc(mel, 3, 4)

    if (myValue < 1.0):
        info['gender'] = "Female Speaker"
    else:
        info['gender'] = "Male Speaker"

    return info
