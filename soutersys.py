#----------MAIN SOUTER---------
# RAMA TESISCONAUBIO
#---PRUEBA PRIMERA VERSION LISTA DE LA TESIS CON AUBIO
# VERSION 0404

import pyaudio
import sys
from PyQt5 import QtGui, QtWidgets
from screengui import Ui_MainWindow
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


class Souter(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #Funcion click boton iniciar grabacion
        self.ui.btn_grabar.clicked.connect(self.ActiveSouter)
        
        self.ui.btn_stop.clicked.connect(self.ResetSouter)

    def ResetSouter(self):
        self.ui.LimpiaLabel()
        self.ui.posx=1
        self.ui.cntbtt=0
        self.ui.btn_grabar.setIcon(QtGui.QIcon("imagenes/grabar.tif"))
        self.ui.rec.setPixmap(QtGui.QPixmap("imagenes/offline.png"))                

    #funcion prueba

    def ActiveSouter(self):     
        self.ui.cntbtt+=1 
             
        if self.ui.cntbtt==1:
                self.ui.btn_grabar.setIcon(QtGui.QIcon("imagenes/pause.tif"))
                self.ui.rec.setPixmap(QtGui.QPixmap("imagenes/online.png"))
                self.ui.Crearnota(1,'D5')
                
        elif self.ui.cntbtt==2:
                self.ui.cntbtt=0
                self.ui.btn_grabar.setIcon(QtGui.QIcon("imagenes/grabar.tif"))
                self.ui.rec.setPixmap(QtGui.QPixmap("imagenes/offline.png"))

if __name__ == "__main__":
    app= QtWidgets.QApplication(sys.argv)
    ventana=Souter()
    #ventana.Revisarsys()
    ventana.show()
    sys.exit(app.exec_())




