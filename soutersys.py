#----------MAIN SOUTER---------
# RAMA TESISCONAUBIO
#---PRUEBA PRIMERA VERSION LISTA DE LA TESIS CON AUBIO
# VERSION 0407
#----------codigo pulido, quitado las lineas sobrantes
import pyaudio
import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import *
from screengui import Ui_MainWindow
import numpy as np
import aubio
from math import log2, pow


class Worker(QRunnable):

    def __init__(self, fn):

        super(Worker, self).__init__()
        self.fn = fn

    def run(self):

        self.fn()

class Souter(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        # initialise pyaudio
        self.total_frames = 0
        self.p = pyaudio.PyAudio()

        # open stream
        self.buffer_size = 1024
        self.pyaudio_format = pyaudio.paFloat32
        self.n_channels = 1
        self.samplerate = 44100
        self.stream = self.p.open(format=self.pyaudio_format,
                        channels=self.n_channels,
                        rate=self.samplerate,
                        input=True,
                        frames_per_buffer=self.buffer_size)

        # setup pitch
        self.tolerance = 0.8
        self.win_s = 4096 # fft size
        self.hop_s = self.buffer_size # hop size
        self.pitch_o = aubio.pitch("default", self.win_s, self.hop_s, self.samplerate)
        #Fijar unidades de salida
        self.pitch_o.set_unit("Hz")
        #Filtro
        self.pitch_o.set_silence(-28)
        #Fijar tolerancia
        self.pitch_o.set_tolerance(self.tolerance)
        self.sg=0
        self.cnt=0
        self.nota=''

        #Llamado a las funciones al iniciar o detener la grabacion
        self.ui.btn_grabar.clicked.connect(self.ActiveSouter)
        self.ui.btn_stop.clicked.connect(self.ResetSouter)

        #SE CREA EL POOL DE HILOS ACÁ 
        self.threadpool = QThreadPool()

    def execute_this_fn(self):
        while (self.ui.cntbtt==1):

            self.audiobuffer = self.stream.read(self.buffer_size)
            self.signal = np.frombuffer(self.audiobuffer, dtype=np.float32)
            self.pitch = self.pitch_o(self.signal)[0]       
            if self.pitch > 15 and self.pitch < 2100:

            #Condicion en sonido
                if self.sg==0:
                #De silencio a sonido

                    self.sg=1
                    self.nota=self.pitching(self.pitch)
                    self.cnt+=1
                elif self.nota==self.pitching(self.pitch):
                #Se mantiene la misma nota
                    self.cnt+=1

                else:
                #Cambia de nota sin pasar por silencio 

                        self.ui.Crearnota(self.cnt/43,self.nota)
                        print("Nota: %3s, Tiempo: %4.2f,segundos" % (self.nota,self.cnt/43))
                        self.nota=self.pitching(self.pitch)
                        self.cnt=0
                  

            else:

            #Condicion en silencio

                if self.sg==1:
                    if self.nota:
                #De sonido a silencio    
                            self.ui.Crearnota(self.cnt/43,self.nota)
                            print("Nota: %3s, Tiempo: %4.2f,segundos" % (self.nota,self.cnt/43))
                            self.nota=0
                            self.sg=0
                            self.cnt=0
        
    def pitching(self, freq):
        self.A4 = 440
        self.C0 = self.A4*pow(2, -4.75)
        self.name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.h = round(12*log2(freq/self.C0))
        self.octave = self.h // 12
        self.n = self.h % 12 
        return self.name[self.n] + str(self.octave)
       
    def ActiveSouter(self): 

        self.ui.cntbtt+=1  
        if self.ui.cntbtt==1:
                self.ui.btn_grabar.setIcon(QtGui.QIcon("imagenes/pause.tif"))
                self.ui.rec.setPixmap(QtGui.QPixmap("imagenes/online.png"))

                worker = Worker(self.execute_this_fn) 
                self.threadpool.start(worker) 
                                 
        elif self.ui.cntbtt==2:
                self.ui.cntbtt=0
                self.ui.btn_grabar.setIcon(QtGui.QIcon("imagenes/grabar.tif"))
                self.ui.rec.setPixmap(QtGui.QPixmap("imagenes/offline.png"))

    def ResetSouter(self):
        self.ui.LimpiaLabel()
        self.ui.posx=1
        self.ui.cntbtt=0
        self.ui.btn_grabar.setIcon(QtGui.QIcon("imagenes/grabar.tif"))
        self.ui.rec.setPixmap(QtGui.QPixmap("imagenes/offline.png"))                

if __name__ == "__main__":
    app= QtWidgets.QApplication(sys.argv)
    ventana=Souter()
    ventana.show()
    sys.exit(app.exec_())
    stream.stop_stream()
    stream.close()
    p.terminate()



