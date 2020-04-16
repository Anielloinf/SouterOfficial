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
        self.arrgloNotacion=np.asarray([])
        self.MagEnElTiempo=[]
        self.arrNotasTocadas=["Silencio"]
        self.sigRMS0=0
        self.df=0
        self.capNota=False
        self.magnitudes=np.asarray([])
        self.maDetallada=np.asarray([])
        self.arrPuntoRojo=np.asarray([]) #Quitar sino funciona
        


        while (self.ui.cntbtt==1):
            try:
                
                self.audiobuffer = self.stream.read(self.buffer_size)
                self.signal = np.fromstring(self.audiobuffer, dtype=np.int16)
                print("signal "+ str(len(self.signal)))

                self.number_samples = len(self.signal)
                self.sigRMS=DaAn.encontrarRMS(self.signal)
                self.maDetallada=np.append(self.maDetallada,self.signal)


        #audio_samples, sample_rate  = soundfile.read(audiobuffer, dtype='int16')
                self.df=self.sigRMS-self.sigRMS0
                print("number_samples "+ str(self.number_samples))
                print(self.sigRMS)

                if self.sigRMS<500 and self.capNota:
                    
                #MostraNotas ANIELLO!!
                    print(self.arrNotasTocadas)
                    self.nota=DaAn.Moda(self.arrNotasTocadas)#DaAn.Moda(self.arrNotasTocadas)
                    print(self.nota)
                    tNota=len(self.arrNotasTocadas)*self.buffer_size/self.samplerate
                    print("\n"+"###########################  Largo de la nota "+ str(self.tNota)+" s  ###########################"+"\n")
                    print("#####################       Comienza el silencio          ####################")
                    self.capNota=False
                    self.ui.Crearnota(self.tNota,self.nota)
                    self.arrNotasTocadas=[]

                if self.df>500:
            #MostraNotas ANIELLO!!

                    print(self.arrNotasTocadas)
                    self.nota=DaAn.Moda(self.arrNotasTocadas)
                    print(self.nota)
                    self.tNota=len(self.arrNotasTocadas)*self.buffer_size/self.samplerate
                    print("\n"+"###########################  Largo de la nota "+ str(self.tNota)+" s  ###########################"+"\n")
                    print("-----------------------     Cambio sin silencio          ---------------------")
                    self.capNota=True
                    self.ui.Crearnota(self.tNota,self.nota)
                    self.arrNotasTocadas=[]


                if self.capNota:

                    self.notasExtraidas,self.magnitudes=DaAn.EncontrarNotaEnSenal(self.signal,self.number_samples,self.samplerate)
            #signalRMSfourier=fourierRMS(normalization_data)
                    self.notaExtraida=self.notasExtraidas[0]
            

                else:
                    self.notaExtraida="KK"
            

                self.arrNotasTocadas.append(self.notaExtraida)


                if self.sigRMS>500:
                    self.sigRMS0=self.sigRMS



                if self.df>0:
                    if self.sigRMS0==0:
                        self.sigRMS0=1
                    self.puntoRojo=self.df/abs(self.sigRMS0)
                else:
                    if self.sigRMS==0:
                        self.sigRMS=1
                    self.puntoRojo=self.df/abs(self.sigRMS)

                self.arrPuntoRojo=np.append(self.arrPuntoRojo,self.puntoRojo)


        #MagEnElTiempo.append(signalRMSfourier)
                self.MagEnElTiempo.append(self.sigRMS)
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
