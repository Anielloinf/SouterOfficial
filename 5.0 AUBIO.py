 #Codigo funcional TESIS
#Version 3.0    --graba y entrega nota en vivo
#Ahora muestra la nota una vez e indica el tiempo que se sostiene la nota, FUNCIONANDO

import pyaudio

import numpy as np
import aubio
from math import log2, pow

# initialise pyaudio
total_frames = 0
p = pyaudio.PyAudio()

# open stream
buffer_size = 1024
pyaudio_format = pyaudio.paFloat32
n_channels = 1
samplerate = 44100
stream = p.open(format=pyaudio_format,
                channels=n_channels,
                rate=samplerate,
                input=True,
                frames_per_buffer=buffer_size)

#Configura notas
A4 = 440
C0 = A4*pow(2, -4.75)
name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    
def pitching(freq):
    h = round(12*log2(freq/C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)

def notacion(nota,time):
    if time>=5:

        return print("Nota: %3s, Tiempo: %4.2f,segundos" % (nota,time/43))

outputsink = None
record_duration = None

# setup pitch
tolerance = 0.8
win_s = 4096 # fft size
hop_s = buffer_size # hop size
pitch_o = aubio.pitch("default", win_s, hop_s, samplerate)
#Fijar unidades de salida
pitch_o.set_unit("Hz")
#Filtro
pitch_o.set_silence(-28)
#Fijar tolerancia
pitch_o.set_tolerance(tolerance)
sg=0
cnt=0
nota=''

print("*** starting recording")

while True:
    try:

        audiobuffer = stream.read(buffer_size)


        signal = np.fromstring(audiobuffer, dtype=np.float32)
        
        #tono=aubio.fvec(signal)
        tono = pitch_o(signal)[0]       
        #print(tono)

        
        if tono > 15 and tono < 2100:
            #Condicion en sonido

            if sg==0:
                #De silencio a sonido
                sg=1
                nota=pitching(tono)
                cnt+=1

            elif nota==pitching(tono):
                #Se mantiene la misma nota
                cnt+=1

            else:
                #Cambia de nota sin pasar por silencio 
                notacion(nota,cnt)
                nota=pitching(tono)
                cnt=0
                  
            #print(pitching(pitch))
        else:
            #Condicion en silencio

            if sg==1:
                if nota:
                #De sonido a silencio

                    notacion(nota,cnt)
                    nota=0
                    sg=0
                    cnt=0
                     
        
    except KeyboardInterrupt:
        print("*** Ctrl+C pressed, exiting")
        break

print("*** done recording")
stream.stop_stream()
stream.close()
p.terminate()