from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import os
import pydub
import numpy as np
from pygame import mixer
import pyaudio  
import wave 

folder = r"C:\Users\MarcoJimenezRodrigue\OneDrive - UPTECH SENSING S.L\Marco - Local\0-Administración\1-Personal\Python_testing\songs\Reggae"

agogo = r"Agogo.wav"
surdo = r"Surdo.wav"
caixa = r"Caixa.wav"

sound = read(folder + "\\" + agogo)
# reg_surdo = read(folder + "\\" + surdo)
# reg_caixa = read(folder + "\\" + caixa)

# arr1 = np.zeros((2,sound[0]))
# for n in range(sound[0]):
#     arr1[0,n]=sound[1][n,0]
#     arr1[1,n]=sound[1][n,1]





#%%

from pydub import AudioSegment
from pydub.playback import play

reg_agogo = AudioSegment.from_file(folder + "\\" + agogo, 'wav')
reg_surdo = AudioSegment.from_wav(folder + "\\" + surdo, 'wav')
reg_caixa = AudioSegment.from_wav(folder + "\\" + caixa, 'wav')

fs = reg_agogo.frame_rate

# sound1 6 dB louder
reg_agogo = reg_agogo - 10
reg_caixa = reg_caixa - 6
reg_surdo = reg_surdo + 3

# # Overlay sound2 over sound1 at position 0  (use louder instead of sound1 to use the louder version)
full_song = reg_surdo.overlay(reg_agogo, position=0)
full_song = full_song.overlay(reg_caixa, position=0)
# simple export
# file_handle = full_song.export(r"C:\Users\MarcoJimenezRodrigue\Downloads\testing\output.wav", format="wav")

# combined = reg_agogo*reg_surdo*reg_caixa
# file_handle = combined.export(r"C:\Users\MarcoJimenezRodrigue\Downloads\testing\output.wav", format="wav")

BPS_value = 120

RATE = full_song.frame_rate
change_rate = BPS_value/90
RATE = round(RATE*change_rate)

# velocidad = 1.5
# full_song = full_song.speedup(velocidad_X, 150, 25)

file_handle = full_song.export(r"C:\Users\MarcoJimenezRodrigue\OneDrive - UPTECH SENSING S.L\Marco - Local\0-Administración\1-Personal\Python_testing\output\output.wav", format="wav")


#%%
chunk = 1024  
    
    #open a wav format music  
f = wave.open(r"C:\Users\MarcoJimenezRodrigue\OneDrive - UPTECH SENSING S.L\Marco - Local\0-Administración\1-Personal\Python_testing\output\output.wav","rb")  

#instantiate PyAudio  
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

#%%
#define stream chunk   
chunk = 1024  

datos = full_song.raw_data

#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(full_song.sample_width),  
                channels = full_song.channels,  
                rate = RATE,  
                output = True)  

data = datos[0:chunk] 

#play stream 
count = 0 
while count<len(datos):  
    stream.write(data)  
    data = datos[count*chunk:chunk*(count+1)]  
    count = count+1
    
#stop stream  
stream.stop_stream()  
stream.close()  

#close PyAudio  
p.terminate()  

#%%

mixer.music.load(r"C:\Users\MarcoJimenezRodrigue\Downloads\testing\output.wav")
mixer.music.play()