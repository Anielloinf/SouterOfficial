#----------MAIN SOUTER---------
# RAMA TESISCONAUBIO
#---PRUEBA PRIMERA VERSION LISTA DE LA TESIS CON AUBIO
# VERSION 0404
import pyaudio
import sys
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from screengui import Ui_MainWindow
import numpy as np
import aubio
import traceback, sys
from math import log2, pow

#---espacio de pruebas para multihilos


class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int,str)



class Worker(QRunnable):

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()

        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()    

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress        

    @pyqtSlot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done


#--fin de espacio de pruebas




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

        #Configura notas    
 #       def notacion(self, nota,time):
  #          if self.time>=5:
   #             return print("Nota: %3s, Tiempo: %4.2f,segundos" % (nota,time/43))

        #self.outputsink = None


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

        #Funcion click boton iniciar grabacion
        self.ui.btn_grabar.clicked.connect(self.ActiveSouter)
        
        self.ui.btn_stop.clicked.connect(self.ResetSouter)

        #Aqui se deberia crear el pool 
#SE CREA EL POOL DE HILOS ACÁ Y SE DEFINE EL TOPE
        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

#ESTO ES LO QUE OCURRE EN EL HILO
    def progress_fn(self, cnt,nota):
        pass
    def execute_this_fn(self, progress_callback):
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
                    #if self.cnt>5:
                        self.ui.Crearnota(self.cnt/43,self.nota)
                        print("Nota: %3s, Tiempo: %4.2f,segundos" % (self.nota,self.cnt/43))
                    #self.notacion(self.nota,self.cnt)
                    #progress_callback.emit(self.cnt, self.nota)
                        self.nota=self.pitching(self.pitch)
                        self.cnt=0
                  
            #print(pitching(pitch))
            else:
            #Condicion en silencio

                if self.sg==1:
                    if self.nota:
                #De sonido a silencio
                        #if self.cnt>5:    
                            self.ui.Crearnota(self.cnt/43,self.nota)
                            print("Nota: %3s, Tiempo: %4.2f,segundos" % (self.nota,self.cnt/43))
                        #self.notacion(self.nota,self.cnt)
                        #progress_callback.emit(self.cnt, self.nota)
                            
                            self.nota=0
                            
                            self.sg=0
                            
                            self.cnt=0
           #     else:
            #        self.nota="kk"
             #       progress_callback.emit(self.cnt, self.nota)
 #AQUI TERMINA LOS CALCULOS               
 
    def print_output(self, s):
        print(s)
    def thread_complete(self):
        print("THREAD COMPLETE!")

#    def notacion(nota,time):
 #       if time>=5:

  #          return print("Nota: %3s, Tiempo: %4.2f,segundos" % (nota,time/43))
             
    def pitching(self, freq):
        self.A4 = 440
        self.C0 = self.A4*pow(2, -4.75)
        self.name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.h = round(12*log2(freq/self.C0))
        self.octave = self.h // 12
        self.n = self.h % 12 
        return self.name[self.n] + str(self.octave)
       

 #---/* AQUI TERMINA EL HILO CREADO 



    #funcion prueba

    def ActiveSouter(self):     
        self.ui.cntbtt+=1 
             
        if self.ui.cntbtt==1:
                self.ui.btn_grabar.setIcon(QtGui.QIcon("imagenes/pause.tif"))
                self.ui.rec.setPixmap(QtGui.QPixmap("imagenes/online.png"))
         # Pass the function to execute
                worker = Worker(self.execute_this_fn) # Any other args, kwargs are passed to the run function
                worker.signals.result.connect(self.print_output)
                worker.signals.finished.connect(self.thread_complete)
                worker.signals.progress.connect(self.progress_fn)
        
        # Execute
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



