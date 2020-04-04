#----------MAIN SOUTER---------
# VERSION 0403

import sys
from PyQt5 import QtGui, QtWidgets
from screengui import Ui_MainWindow

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
            self.ui.Crearnota(0.5,'B5') 
            self.ui.Crearnota(0.3,'KK') 
            self.ui.Crearnota(0.5,'KK') 
            self.ui.Crearnota(0.2,'KK') 
            self.ui.Crearnota(0.2,'C#5') 
            self.ui.Crearnota(0.2,'D5') 
            self.ui.Crearnota(0.8,'C5') 
            self.ui.Crearnota(0.8,'B#4') 
            self.ui.Crearnota(0.8,'A#4')
            self.ui.Crearnota(0.8,'G4') 
            self.ui.Crearnota(0.8,'F#4') 
            self.ui.Crearnota(0.8,'E4')         
            
        elif self.ui.cntbtt==2:

            self.ui.cntbtt=0
            self.ui.btn_grabar.setIcon(QtGui.QIcon("imagenes/grabar.tif"))
            self.ui.rec.setPixmap(QtGui.QPixmap("imagenes/offline.png"))
            


if __name__ == "__main__":
    app= QtWidgets.QApplication(sys.argv)
    ventana=Souter()
    ventana.show()
    sys.exit(app.exec_())




