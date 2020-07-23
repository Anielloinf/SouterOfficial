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
#import aubio
import wave
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
        self.audioCompleto= []  #Señal con todo el sonido desde el ultimo play hasta la ultima pausa

        self.wf=wave.open('SonidoCaptadoPorSoutersys.wav', 'wb')
        self.wf.setnchannels(1)
        self.wf.setsampwidth(self.p.get_sample_size(self.pyaudio_format))
        self.wf.setframerate(self.samplerate)

        #Llamado a las funciones al iniciar o detener la grabacion
        self.ui.btn_grabar.clicked.connect(self.ActiveSouter)
        self.ui.btn_stop.clicked.connect(self.ResetSouter)

        #SE CREA EL POOL DE HILOS ACÁ 
        self.threadpool = QThreadPool()

    def execute_this_fn(self):
                
        self.duracionMinima=0.0625  # a 120 bpm 0.0625 representa un 'cuarto de tiempo'
        
        self.umbralRuido=50    #umbralRuido es el valor que determina cuando la señal deja o no de ser silencio 
       
        self.variacionDeCambioNota=200     #variacionDeCambioNota es el cambio de magnitud que determina cuando una nota empieza a tocarse despues de haber tocado una anteriormente
        #Evaluar si vale la pena cambiar esto por una fraccion o multiplo del valor maximo de sig0FFT
       
        self.factorDeApreciacion=0.6    #factorDeApreciacion define la relacion máxima que tiene la magnitud mas alta del espectro de frecuencia con respecto a la magnitud que corresponde a la frecuencia de la nota tocada
       
        self.noise_level=50        #noise_level es el valor mínimo en el espectro de frecuencia que se considera como posible pico de la frecuencia representativa de la señal

        

        self.senalConNota=np.asarray([])
        self.MagEnElTiempo=[]
        self.sig0RMS=0
        self.empezoDescenso=False

        #self.sig0FFT=np.zeros(self.buffer_size//2)
        
        #self.sig0Pico=np.ones(self.buffer_size//2)


        

        while (self.ui.cntbtt==1):
            try:
                
                self.audiobuffer = self.stream.read(self.buffer_size)
                self.signal1 = np.fromstring(self.audiobuffer, dtype=np.int16)


                self.audioCompleto.append(self.signal1)# Audio para guardar

                
                self.sig1RMS=DaAn.encontrarRMS(self.signal1)

                self.VariacionRMS=self.sig1RMS  -   self.sig0RMS



                

                self.tNota=len(self.senalConNota)/self.samplerate


                self.cambioNotaASilencio    =   (self.VariacionRMS  >   self.variacionDeCambioNota and self.empezoDescenso)
                self.cambioSilencioANota    =   (self.sig0RMS<self.umbralRuido and self.sig1RMS>=self.umbralRuido)
                self.cambioNotaANota        =   (self.sig0RMS>=self.umbralRuido and self.sig1RMS<self.umbralRuido)

                if self.cambioNotaASilencio or self.cambioSilencioANota or self.cambioNotaANota:
                    

                    if self.tNota>self.duracionMinima:

                        if self.sig0RMS<self.umbralRuido:

                            self.nota="KK"
                        else:
                            self.nota,self.magnitudes=DaAn.EncontrarNotaEnSenal(self.senalConNota,self.samplerate,factorDeApreciacion=self.factorDeApreciacion,noise_level=self.noise_level)
                            ###### Veririficar uso de factorDeApreciacion, borrar para version final



                        self.ui.Crearnota(self.tNota, self.nota)
                        print("Nota ######################  "+ self.nota)

                        self.senalConNota=self.signal1

                    else:
                        self.senalConNota=np.append(self.senalConNota,self.signal1)

                    self.empezoDescenso=False


                else:
                     
                    self.senalConNota=np.append(self.senalConNota,self.signal1)

                    if self.tNota>self.duracionMinima and self.VariacionRMS<0:
                        self.empezoDescenso=True


                self.sig0RMS=self.sig1RMS
                

                #self.sig0FFT=self.sig1FFT*1
                
                
                #self.sig0Pico=(self.sig0FFT<max(self.sig0FFT)) 
                
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
                print('##################   '+str(len(self.audioCompleto)))
                

                self.wf.writeframes(b''.join(self.audioCompleto))#Guardando audio
                self.wf.close()




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
