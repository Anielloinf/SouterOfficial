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

from scipy.stats import mode
import DamianAniello as DaAn 



class Worker(QRunnable):

    def __init__(self, fn):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        

    #@pyqtSlot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
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
        self.pyaudio_format = pyaudio.paInt16
        self.n_channels = 1
        self.samplerate = 44100
        self.stream = self.p.open(format=self.pyaudio_format,
                        channels=self.n_channels,
                        rate=self.samplerate,
                        input=True,
                        frames_per_buffer=self.buffer_size)


        # setup pitch
        

        #Llamado a las funciones al iniciar o detener la grabacion
        self.ui.btn_grabar.clicked.connect(self.ActiveSouter)
        self.ui.btn_stop.clicked.connect(self.ResetSouter)

        #SE CREA EL POOL DE HILOS ACÁ 
        self.threadpool = QThreadPool()

    def execute_this_fn(self):
        #self.arrgloNotacion=np.asarray([])
        self.MagEnElTiempo=[]
        self.sig0FFT=np.arange(self.buffer_size//2)*0
        self.sig0RMS=0
        self.sig0Pico=self.sig0FFT+1


        self.senalConNota=np.asarray([])
        

        self.variacionDeCambioNota=1000 #Evaluar si vale la pena cambiar esto por una fraccion o multiplo del valor maximo de sig0FFT
        self.umbralRuido=5000


        while (self.ui.cntbtt==1):
            try:
                
                self.audiobuffer = self.stream.read(self.buffer_size)
                self.signal1 = np.fromstring(self.audiobuffer, dtype=np.int16)
                
                self.sig1RMS=DaAn.encontrarRMS(self.signal1)

                print("signal1 "+ str(self.sig1RMS))

                if self.sig1RMS >self.umbralRuido:
                    self.sig1FFT=np.fft.fft(self.signal1)
                    self.sig1FFT=np.abs(self.sig1FFT)
                    print('nota '+ str(max(self.sig1FFT)))

                    self.sig1FFT=self.sig1FFT[range(len(self.sig1FFT)//2)]/len(self.sig1FFT) # arreglo con la parte positiva del espectro en frecuencia
                else:
                    self.sig1RMS=0
                    self.sig1FFT=np.arange(len(self.signal1)//2)*0
                    print('silencio '+ str(max(self.sig0FFT)))




                if max((self.sig1FFT-self.sig0FFT)*self.sig0Pico)>self.variacionDeCambioNota or (self.sig0RMS==0 and self.sig1RMS!=0) or (self.sig0RMS!=0 and self.sig1RMS==0):
                    '''
                    '''
                    self.tNota=len(self.senalConNota)/self.samplerate
                    
                    if self.sig0RMS==0:

                        self.nota="KK"
                    else:
                        self.notasExtraidas,self.magnitudes=DaAn.EncontrarNotaEnSenal(self.senalConNota,len(self.senalConNota),self.samplerate)
                        self.nota=self.notasExtraidas[0]



                    self.ui.Crearnota(self.tNota, self.nota)
                    print("Nota ######################  "+ self.nota)

                    self.senalConNota=self.signal1


                else:
                     
                    self.senalConNota=np.append(self.senalConNota,self.signal1)


                self.sig0RMS=self.sig1RMS
                self.sig0FFT=self.sig1FFT*1
                
                
                self.sig0Pico=(self.sig0FFT<max(self.sig0FFT)) 
                ''' en sig0Pico el elemento de posición paralela al pico mas alto de sig0FFT se hace 0 
                y el resto de los elementos valen 1 '''

                
            
            except KeyboardInterrupt:
                print("*** Ctrl+C pressed, exiting")
                break

            

       
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
