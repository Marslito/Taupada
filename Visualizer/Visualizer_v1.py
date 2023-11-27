#%% 
get_ipython().magic('reset -sf')
get_ipython().magic('clear')

#%% Libraries import-----------------------------------------------------------

from numpy import where, array
import tkinter as tk 
from tkinter import ttk
from tkinter import *
from tkinter import messagebox 
# import tkinter
import matplotlib.pyplot as plt 
import os
from pydub import AudioSegment
import pyaudio  
import wave  
import threading
from pygame import mixer
import pygame


    
pygame.init()

# Root definition-------------------------------------------------------------:
root   = tk.Tk()

try:
    os.remove(r"C:\Users\MarcoJimenezRodrigue\Downloads\testing\temp\temp_song.wav")
except:
    print("No temporary files")
# width  = root.winfo_screenwidth()               
# height = root.winfo_screenheight()    
width  = 600             
height = 400              
root.geometry("%dx%d" % (width, height))
root.title("TaupaEscuela")

px = 1/plt.rcParams['figure.dpi']  # pixel in inches


# Master frame:
master_frame = tk.Frame(root)
master_frame.pack(expand = True, fill = tk.BOTH)

quit_btn = tk.Button(master_frame, text = 'Quit')
quit_btn.pack(side = tk.BOTTOM)


# Sub frame 0-----------------------------------------------------------------: 
frame_0 = tk.LabelFrame(master_frame)
frame_0.pack(fill = tk.Y, side = tk.LEFT)

### MODIFICAR POR SELECT SONG ###
# Sub sub frame 00:     
frame_0_0 = tk.LabelFrame(frame_0)
frame_0_0.pack(expand = True, fill = tk.BOTH)
songs_label = tk.Label(frame_0_0,text = 'CANCIÓN')
songs_label.pack()
ritmos = ["REGGAE","RIO", "PARTIDO ALTO", "MARACATU", 
          "AFRICANO"]
songs_combobox = ttk.Combobox(frame_0_0,state = "readonly",
                                  value = ritmos)

songs_combobox.pack()

frame_0_1 = tk.LabelFrame(frame_0)
frame_0_1.pack(expand = True, fill = tk.BOTH)
play_song_btn = tk.Button(frame_0_1, text = 'PLAY')
play_song_btn.pack()
stop_song_btn = tk.Button(frame_0_1, text = 'STOP')
stop_song_btn.pack()
pause_song_btn = tk.Button(frame_0_1, text = 'PAUSE')
pause_song_btn.pack()
resume_song_btn = tk.Button(frame_0_1, text = 'RESUME')
resume_song_btn.pack()


# # Sub sub frame 1_0: 



frame_1 = tk.LabelFrame(master_frame)
frame_1.pack(fill = tk.Y, side = tk.TOP)
frame_1_0 = tk.LabelFrame(frame_1, text = 'INSTRUMENTOS')
frame_1_0.pack(expand = True, fill = tk.BOTH)

surdo_state = IntVar()
caixa_state = IntVar()
agogo_state = IntVar()
loop_state  = IntVar()

surdo_btn = Checkbutton(frame_1_0, text = "Surdos", variable = surdo_state, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 10)
surdo_btn.pack()
caixa_btn = Checkbutton(frame_1_0, text = "Caixa", variable = caixa_state, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 10)
caixa_btn.pack()
agogo_btn = Checkbutton(frame_1_0, text = "Agogo", variable = agogo_state, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 10)
agogo_btn.pack()

instruments_btn = tk.Button(frame_1_0, text = 'ACEPTAR SELECCIÓN')
instruments_btn.pack()

frame_1_1 = tk.LabelFrame(frame_1, text = 'VELOCIDAD')
frame_1_1.pack(expand = True, fill = tk.BOTH)
BPS_entry = tk.Entry(frame_1_1, width = 4)
BPS_entry.pack()
update_BPS_btn = tk.Button(frame_1_1, text = "BPS")
update_BPS_btn.pack()

frame_1_2 = tk.LabelFrame(frame_1, text = 'REPETICIÓN')
frame_1_2.pack(expand = True, fill = tk.BOTH)
loop_entry = tk.Entry(frame_1_2, width = 4)
loop_entry.pack()
update_loop_btn = tk.Button(frame_1_2, text = "CICLOS")
update_loop_btn.pack()

# Sub frame 2-----------------------------------------------------------------: 
frame_2 = tk.LabelFrame(master_frame)
frame_2.pack(fill = tk.X, side = tk.RIGHT)

frame_2_0 = tk.LabelFrame(frame_2)
frame_2_0.pack(expand = True, fill = tk.BOTH)


def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
          "frame_rate": int(sound.frame_rate * speed)
      })
      # convert the sound with altered frame rate to a standard frame rate
      # so that regular playback programs will work right. They often only
      # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


# from Update_functions import *
def quit_app():
    
    plt.close('all')
    root.quit()
    root.destroy()

def select_songs(value): 
    
    global selected_song
    global BPS_value
    global agogo, surdo, caixa
    global repetitions
    
    repetitions = 0
    
    BPS_value = 0
    
    selected_song = songs_combobox.get()
    print(selected_song)
    if selected_song == 'REGGAE':    
        folder = r"C:\Users\MarcoJimenezRodrigue\Downloads\testing\songs\Reggae"
        os.chdir(folder)
        
        # file = r"Agogo.wav"
        # agogo = AudioSegment.from_file(file, 'wav')
        # agogo = agogo - 10
        # file = r"Surdo.wav"
        # surdo = AudioSegment.from_file(file, 'wav')
        # surdo = surdo + 6
        # file = r"Caixa.wav"
        # caixa = AudioSegment.from_file(file, 'wav')
        # caixa = caixa - 5
        
    elif selected_song == "RIO":
        messagebox.showinfo(message="Ritmo RIO en construcción", title="Aviso")
    elif selected_song == "PARTIDO ALTO":
        messagebox.showinfo(message="Ritmo PARTIDO ALTO en construcción", title="Aviso")
    elif selected_song == "MARACATU":
        messagebox.showinfo(message="Ritmo MARACATU en construcción", title="Aviso")
    elif selected_song == "AFRICANO" : 
        messagebox.showinfo(message="Ritmo AFRICANO en construcción", title="Aviso")
    else:
        messagebox.showinfo(message="Debes seleccionar un ritmo", title="Error")

def select_instruments():
    
    mixer.music.stop() 
    mixer.music.unload()
    
    global estado_instrumentos, marked_states
    global song
    estado_instrumentos = array((surdo_state.get(), caixa_state.get(), agogo_state.get()))
    print(estado_instrumentos)
    marked_states = where(estado_instrumentos==1)
    
    if selected_song == "Selecciona":
        messagebox.showinfo(message="Debes seleccionar un ritmo", title="Error")
    else:     
        file = r"Agogo.wav"
        agogo = AudioSegment.from_file(file, 'wav')
        agogo = agogo - 10
        file = r"Surdo.wav"
        surdo = AudioSegment.from_file(file, 'wav')
        surdo = surdo + 6
        file = r"Caixa.wav"
        caixa = AudioSegment.from_file(file, 'wav')
        caixa = caixa - 5
    
        instrumentos = {0 :     surdo,
                        1 :     caixa,
                        2 :     agogo}

        
        if len(marked_states[0])==0:
            messagebox.showinfo(message="No has seleccionado instrumentos", title="Error")
        elif len(marked_states[0])==1:
            song = instrumentos[marked_states[0][0]]
            song.export(r"C:\Users\MarcoJimenezRodrigue\Downloads\testing\temp\temp_song.wav", format="wav")
        elif len(marked_states[0])==2:
            song = instrumentos[marked_states[0][0]].overlay(instrumentos[marked_states[0][1]], position=0)
            song.export(r"C:\Users\MarcoJimenezRodrigue\Downloads\testing\temp\temp_song.wav", format="wav")
        elif len(marked_states[0])==3:
            song = instrumentos[marked_states[0][0]].overlay(instrumentos[marked_states[0][1]], position=0)
            song = song.overlay(instrumentos[marked_states[0][2]], position=0)
            song.export(r"C:\Users\MarcoJimenezRodrigue\Downloads\testing\temp\temp_song.wav", format="wav")
            

def update_BPS():
    
    mixer.music.stop() 
    mixer.music.unload()
    
    global song
    
    BPS_value = float(BPS_entry.get())
    if BPS_value == 0:
        messagebox.showinfo(message="Valor no aceptado", title="Error")
    else:
        # os.remove(r"C:\Users\MarcoJimenezRodrigue\Downloads\testing\temp\temp_song.wav")
        change_rate = BPS_value/90
        updated_song = speed_change(song,change_rate)
        updated_song.export(r"C:\Users\MarcoJimenezRodrigue\Downloads\testing\temp\temp_song.wav", format="wav")

def repeat_song():
    
    global repetitions
    
    repetitions = int(loop_entry.get()) 
    
    
    
def begin_song():
    
    global playing
    global stream
    
    print(repetitions)
    
    if selected_song == "REGGAE":
        if len(marked_states[0])==0:
            messagebox.showinfo(message="No has seleccionado instrumentos", title="Error")
        else:  
            mixer.music.load(r"C:\Users\MarcoJimenezRodrigue\Downloads\testing\temp\temp_song.wav","rb")
            mixer.music.play(repetitions)
    else:
        messagebox.showinfo(message="Debes seleccionar un ritmo válido", title="Error")
    
def stop_music():
    mixer.music.stop() 
    mixer.music.unload()
    
def pause_music():
    mixer.music.pause() 


def resume_music():
    mixer.music.unpause() 

    
# =============================================================================
#  Assign functions to widgets
# =============================================================================

# Master frame commands-------------------------------------------------------:
quit_btn.configure(command = quit_app)
    
# Subframe 0 commands --------------------------------------------------------:

# Sub sub frame 00 
songs_combobox.set("Selecciona")
songs_combobox.bind("<<ComboboxSelected>>", select_songs)

## Sub sub frame 01
instruments_btn.configure(command = select_instruments)

## Sub sub frame 01
update_BPS_btn.configure(command = update_BPS)

update_loop_btn.configure(command = repeat_song)

## Sub sub frame 02
play_song_btn.configure(command = begin_song)
stop_song_btn.configure(command = stop_music)
pause_song_btn.configure(command = pause_music)
resume_song_btn.configure(command = resume_music)

print("%d,%d" %(width,height))
root.mainloop()
