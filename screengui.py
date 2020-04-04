#-------SOUTER 0403-------
#---CODIGO BASE DE GUI SOUTER (Hijo)---
#funciona al pelo
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):



    def setupUi(self, MainWindow):

        #Dimensiones de la pantalla
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1070, 627)

        #Posición de la pantalla
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        #Parametros barra de menu superior
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName("menubar")    
        
        #-------VARIABLES DEL SISTEMA---------

        self.cntbtt=0 
        self.posx=1
        self.GenTemp=36
        
        #----- SIMBOLOS GRAFICOS---

        #Imagen de fondo de Souter
        self.fondo = QtWidgets.QLabel(self.centralwidget)
        self.fondo.setGeometry(QtCore.QRect(0, 0, 1070, 627))
        self.fondo.setPixmap(QtGui.QPixmap("imagenes/fondo.jpg"))

        # Imagen de BARRA DE OPCIONES inferior de Souter
        self.barrainf = QtWidgets.QLabel(self.centralwidget)
        self.barrainf.setGeometry(QtCore.QRect(-1, 493, 349, 58))
        self.barrainf.setPixmap(QtGui.QPixmap("imagenes/barra.png"))
        self.barrainf.setScaledContents(True)
        self.barrainf.setObjectName("barrainf")

        # Imagen de BARRA DE OPCIONES DERECHA inferior de Souter
        self.barrainfder = QtWidgets.QLabel(self.centralwidget)
        self.barrainfder.setGeometry(QtCore.QRect(721, 493, 349, 58))
        self.barrainfder.setPixmap(QtGui.QPixmap("imagenes/barrader.png"))
        self.barrainfder.setScaledContents(True)
        self.barrainfder.setObjectName("barrainf")
        
         # Imagen de PLAY inferior de Souter
        self.botonplay = QtWidgets.QLabel(self.centralwidget)
        self.botonplay.setGeometry(QtCore.QRect(72, 460, 119, 119))
        self.botonplay.setPixmap(QtGui.QPixmap("imagenes/playbuton.png"))
        self.botonplay.setScaledContents(True)
       
         # Boton para iniciar y pausar grabacion
        self.btn_grabar=QtWidgets.QPushButton(MainWindow)
        self.btn_grabar.setIcon(QtGui.QIcon("imagenes/grabar.tif"))
        self.btn_grabar.setIconSize(QtCore.QSize(130,130))
        self.btn_grabar.setGeometry(QtCore.QRect(89, 498, 84, 84))
        self.btn_grabar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))  

         # Boton para reiniciar la escritura
        self.btn_stop=QtWidgets.QPushButton(MainWindow)
        self.btn_stop.setIcon(QtGui.QIcon("imagenes/stop.tif"))
        self.btn_stop.setIconSize(QtCore.QSize(140,43))
        self.btn_stop.setGeometry(QtCore.QRect(191, 521, 140, 43))
        self.btn_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))  

         # Imagen de aviso de grabacion activa
        self.rec = QtWidgets.QLabel(self.centralwidget)
        self.rec.setGeometry(QtCore.QRect(752, 503, 127, 38))
        self.rec.setPixmap(QtGui.QPixmap("imagenes/offline.png"))
        self.rec.setScaledContents(True)

         # Imagen de PARTITURA INICIAL de Souter
        self.partiA = QtWidgets.QLabel(self.centralwidget)
        self.partiA.setGeometry(QtCore.QRect(42, 56, 970, 80))
        self.partiA.setPixmap(QtGui.QPixmap("imagenes/elementos/iniciocancion.png"))
        self.partiA.setScaledContents(True)

         # Imagen de PARTITURA SIGUIENTE de Souter
        self.partB = QtWidgets.QLabel(self.centralwidget)
        self.partB.setGeometry(QtCore.QRect(42, 162, 970, 80))
        self.partB.setPixmap(QtGui.QPixmap("imagenes/elementos/pentnext.png"))
        self.partB.setScaledContents(True)

         # Imagen de PARTITURA SIGUIENTE de Souter
        self.partC = QtWidgets.QLabel(self.centralwidget)
        self.partC.setGeometry(QtCore.QRect(42, 276, 970, 80))
        self.partC.setPixmap(QtGui.QPixmap("imagenes/elementos/pentnext.png"))
        self.partC.setScaledContents(True)

        # Imagen de PARTITURA SIGUIENTE de Souter
        self.partD = QtWidgets.QLabel(self.centralwidget)
        self.partD.setGeometry(QtCore.QRect(42, 390, 970, 80))
        self.partD.setPixmap(QtGui.QPixmap("imagenes/elementos/pentnext.png"))
        self.partD.setScaledContents(True)

        #---Ubicacion de cada label en pantalla---
        self.lbla1 = QtWidgets.QLabel(self.centralwidget)
        self.lbla1.setScaledContents(True)       
        self.lbla2 = QtWidgets.QLabel(self.centralwidget)
        self.lbla2.setScaledContents(True)            
        self.lbla3 = QtWidgets.QLabel(self.centralwidget)
        self.lbla3.setScaledContents(True)            
        self.lbla4 = QtWidgets.QLabel(self.centralwidget)
        self.lbla4.setScaledContents(True) 
        self.lbla5 = QtWidgets.QLabel(self.centralwidget)
        self.lbla5.setScaledContents(True)
        self.lbla6 = QtWidgets.QLabel(self.centralwidget)   
        self.lbla6.setScaledContents(True)
        self.lbla7 = QtWidgets.QLabel(self.centralwidget)
        self.lbla7.setScaledContents(True)
        self.lbla8 = QtWidgets.QLabel(self.centralwidget)
        self.lbla8.setScaledContents(True)  
        self.lbla9 = QtWidgets.QLabel(self.centralwidget)
        self.lbla9.setScaledContents(True)       
        self.lbla10 = QtWidgets.QLabel(self.centralwidget)
        self.lbla10.setScaledContents(True)      
        self.lbla11 = QtWidgets.QLabel(self.centralwidget)
        self.lbla11.setScaledContents(True)       
        self.lbla12 = QtWidgets.QLabel(self.centralwidget)
        self.lbla12.setScaledContents(True)       
        self.lbla13 = QtWidgets.QLabel(self.centralwidget)
        self.lbla13.setScaledContents(True) 
        self.lbla14 = QtWidgets.QLabel(self.centralwidget)
        self.lbla14.setScaledContents(True)       
        self.lbla15 = QtWidgets.QLabel(self.centralwidget)
        self.lbla15.setScaledContents(True)       
        self.lbla16 = QtWidgets.QLabel(self.centralwidget)
        self.lbla16.setScaledContents(True)       
        self.lbla17 = QtWidgets.QLabel(self.centralwidget)
        self.lbla17.setScaledContents(True)     
        self.lbla18 = QtWidgets.QLabel(self.centralwidget)
        self.lbla18.setScaledContents(True)
        self.lblb1 = QtWidgets.QLabel(self.centralwidget)
        self.lblb1.setScaledContents(True)       
        self.lblb2 = QtWidgets.QLabel(self.centralwidget)
        self.lblb2.setScaledContents(True)   
        self.lblb3 = QtWidgets.QLabel(self.centralwidget)
        self.lblb3.setScaledContents(True)       
        self.lblb4 = QtWidgets.QLabel(self.centralwidget)
        self.lblb4.setScaledContents(True)       
        self.lblb5 = QtWidgets.QLabel(self.centralwidget)
        self.lblb5.setScaledContents(True)       
        self.lblb6 = QtWidgets.QLabel(self.centralwidget)   
        self.lblb6.setScaledContents(True)       
        self.lblb7 = QtWidgets.QLabel(self.centralwidget)
        self.lblb7.setScaledContents(True)       
        self.lblb8 = QtWidgets.QLabel(self.centralwidget)
        self.lblb8.setScaledContents(True)       
        self.lblb9 = QtWidgets.QLabel(self.centralwidget)
        self.lblb9.setScaledContents(True)       
        self.lblb10 = QtWidgets.QLabel(self.centralwidget)
        self.lblb10.setScaledContents(True)       
        self.lblb11 = QtWidgets.QLabel(self.centralwidget)
        self.lblb11.setScaledContents(True)       
        self.lblb12 = QtWidgets.QLabel(self.centralwidget)
        self.lblb12.setScaledContents(True)       
        self.lblb13 = QtWidgets.QLabel(self.centralwidget)
        self.lblb13.setScaledContents(True)       
        self.lblb14 = QtWidgets.QLabel(self.centralwidget)
        self.lblb14.setScaledContents(True)       
        self.lblb15 = QtWidgets.QLabel(self.centralwidget)
        self.lblb15.setScaledContents(True)       
        self.lblb16 = QtWidgets.QLabel(self.centralwidget)
        self.lblb16.setScaledContents(True)       
        self.lblb17 = QtWidgets.QLabel(self.centralwidget)
        self.lblb17.setScaledContents(True)       
        self.lblb18 = QtWidgets.QLabel(self.centralwidget)
        self.lblb18.setScaledContents(True)  
        self.lblc1 = QtWidgets.QLabel(self.centralwidget)
        self.lblc1.setScaledContents(True)       
        self.lblc2 = QtWidgets.QLabel(self.centralwidget)
        self.lblc2.setScaledContents(True)    
        self.lblc3 = QtWidgets.QLabel(self.centralwidget)
        self.lblc3.setScaledContents(True)       
        self.lblc4 = QtWidgets.QLabel(self.centralwidget)
        self.lblc4.setScaledContents(True)    
        self.lblc5 = QtWidgets.QLabel(self.centralwidget)
        self.lblc5.setScaledContents(True)       
        self.lblc6 = QtWidgets.QLabel(self.centralwidget)   
        self.lblc6.setScaledContents(True)       
        self.lblc7 = QtWidgets.QLabel(self.centralwidget)
        self.lblc7.setScaledContents(True)       
        self.lblc8 = QtWidgets.QLabel(self.centralwidget)
        self.lblc8.setScaledContents(True)       
        self.lblc9 = QtWidgets.QLabel(self.centralwidget)
        self.lblc9.setScaledContents(True)       
        self.lblc10 = QtWidgets.QLabel(self.centralwidget)
        self.lblc10.setScaledContents(True)       
        self.lblc11 = QtWidgets.QLabel(self.centralwidget)
        self.lblc11.setScaledContents(True)       
        self.lblc12 = QtWidgets.QLabel(self.centralwidget)
        self.lblc12.setScaledContents(True)       
        self.lblc13 = QtWidgets.QLabel(self.centralwidget)
        self.lblc13.setScaledContents(True)       
        self.lblc14 = QtWidgets.QLabel(self.centralwidget)
        self.lblc14.setScaledContents(True)       
        self.lblc15 = QtWidgets.QLabel(self.centralwidget)
        self.lblc15.setScaledContents(True)       
        self.lblc16 = QtWidgets.QLabel(self.centralwidget)
        self.lblc16.setScaledContents(True)       
        self.lblc17 = QtWidgets.QLabel(self.centralwidget)
        self.lblc17.setScaledContents(True)       
        self.lblc18 = QtWidgets.QLabel(self.centralwidget)
        self.lblc18.setScaledContents(True)  
        self.lbld1 = QtWidgets.QLabel(self.centralwidget)
        self.lbld1.setScaledContents(True)       
        self.lbld2 = QtWidgets.QLabel(self.centralwidget)
        self.lbld2.setScaledContents(True)      
        self.lbld3 = QtWidgets.QLabel(self.centralwidget)
        self.lbld3.setScaledContents(True)       
        self.lbld4 = QtWidgets.QLabel(self.centralwidget)
        self.lbld4.setScaledContents(True)       
        self.lbld5 = QtWidgets.QLabel(self.centralwidget)
        self.lbld5.setScaledContents(True)   
        self.lbld6 = QtWidgets.QLabel(self.centralwidget)   
        self.lbld6.setScaledContents(True)       
        self.lbld7 = QtWidgets.QLabel(self.centralwidget)
        self.lbld7.setScaledContents(True)       
        self.lbld8 = QtWidgets.QLabel(self.centralwidget)
        self.lbld8.setScaledContents(True)       
        self.lbld9 = QtWidgets.QLabel(self.centralwidget)
        self.lbld9.setScaledContents(True)       
        self.lbld10 = QtWidgets.QLabel(self.centralwidget)
        self.lbld10.setScaledContents(True)       
        self.lbld11 = QtWidgets.QLabel(self.centralwidget)
        self.lbld11.setScaledContents(True)       
        self.lbld12 = QtWidgets.QLabel(self.centralwidget)
        self.lbld12.setScaledContents(True)       
        self.lbld13 = QtWidgets.QLabel(self.centralwidget)
        self.lbld13.setScaledContents(True)       
        self.lbld14 = QtWidgets.QLabel(self.centralwidget)
        self.lbld14.setScaledContents(True)       
        self.lbld15 = QtWidgets.QLabel(self.centralwidget)
        self.lbld15.setScaledContents(True)       
        self.lbld16 = QtWidgets.QLabel(self.centralwidget)
        self.lbld16.setScaledContents(True)       
        self.lbld17 = QtWidgets.QLabel(self.centralwidget)
        self.lbld17.setScaledContents(True)       
        self.lbld18 = QtWidgets.QLabel(self.centralwidget)
        self.lbld18.setScaledContents(True)        



        #------MENU ENCABEZADO DE OPCIONES-------

        #Parametros barra de menu
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")

        #Parametros barra de menu AYUDA
        self.menuAyuda = QtWidgets.QMenu(self.menubar)
        self.menuAyuda.setObjectName("menuAyuda")
        MainWindow.setMenuBar(self.menubar)

        #Parametros barra de menu STATUS
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Parametros barra de menu ARCHIVO NUEVO
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")

        #Parametros barra de menu ABRIR
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")

        #Parametros barra de menu GUARDAR
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")

        #Parametros barra de menu SALIR
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")

        #Parametros sesion ayuda Souter
        self.actionAyuda_en_Souter = QtWidgets.QAction(MainWindow)
        self.actionAyuda_en_Souter.setObjectName("actionAyuda_en_Souter")
        self.actionInformaci_n_del_programa = QtWidgets.QAction(MainWindow)
        self.actionInformaci_n_del_programa.setObjectName("actionInformaci_n_del_programa")

        #Misc 
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAyuda_en_Souter)
        self.menuAyuda.addAction(self.actionInformaci_n_del_programa)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #---------DICCIONARIO PARA LOS SIMBOLOS DE LAS NOTAS------
        self.simbolo={
            1: "imagenes/elementos/redondamuy.png",
            2: "imagenes/elementos/redondasosmuy.png",
            3: "imagenes/elementos/redondasos.png",
            4: "imagenes/elementos/redonda.png",
            5: "imagenes/elementos/blancamuy.png",
            6: "imagenes/elementos/blancahh.png",
            7: "imagenes/elementos/blancahhmuy.png",
            8: "imagenes/elementos/blancasosmuy.png",
            9: "imagenes/elementos/blancasoshhmuy.png",
            10: "imagenes/elementos/blancasoshh.png",
            11: "imagenes/elementos/blanca.png",
            12: "imagenes/elementos/blancasos.png",
            13: "imagenes/elementos/negrahh.png",
            14: "imagenes/elementos/negramuy.png",
            15: "imagenes/elementos/negrahhmuy.png",
            16: "imagenes/elementos/negrasosmuy.png",
            17: "imagenes/elementos/negrasoshh.png",
            18: "imagenes/elementos/negrasoshhmuy.png",
            19: "imagenes/elementos/negra.png",
            20: "imagenes/elementos/negrasos.png",
            21: "imagenes/elementos/corchea.png",
            22: "imagenes/elementos/corcheahh.png",
            23: "imagenes/elementos/corcheamuy.png",
            24: "imagenes/elementos/corcheasos.png",
            25: "imagenes/elementos/corcheahhmuy.png",
            26: "imagenes/elementos/corcheasosmuy.png",
            27: "imagenes/elementos/corcheasoshhmuy.png",
            28: "imagenes/elementos/corcheasoshh.png",
            29: "imagenes/elementos/semicorchea.png",
            30: "imagenes/elementos/semicorcheahh.png",
            31: "imagenes/elementos/semicorcheahhmuy.png",
            32: "imagenes/elementos/semicorcheasosmuy.png",
            33: "imagenes/elementos/semicorcheasoshhmuy.png",
            34: "imagenes/elementos/semicorcheasoshh.png",
            35: "imagenes/elementos/semicorcheamuy.png",
            36: "imagenes/elementos/semicorcheasos.png",
            37: "imagenes/elementos/silentfusa.png",
            38: "imagenes/elementos/silentnegra.png",
            39: "imagenes/elementos/silentcorchea.png",
            40: "imagenes/elementos/silentsemicorchea.png",
            41: "imagenes/elementos/fincompas.png",
            42: "imagenes/elementos/ligaduradown.png",
            43: "imagenes/elementos/cuadro.png",
            44: "imagenes/elementos/semicorcheasosextrhhmuy.png",
            45: "imagenes/elementos/semicorcheahhextrmuy.png",
            46: "imagenes/elementos/semicorcheasoshhextr.png",
            47: "imagenes/elementos/semicorcheahhextr.png",
            48: "imagenes/elementos/corcheahhextrmuy.png",
            49: "imagenes/elementos/corcheahhsosextr.png",
            50: "imagenes/elementos/corcheahhextr.png",
            51: "imagenes/elementos/corcheahhsosextrmuy.png",
            52: "imagenes/elementos/negrahhextr.png",
            53: "imagenes/elementos/negrahhextrmuy.png",
            54: "imagenes/elementos/negrahhsosextr.png",
            55: "imagenes/elementos/negrahhsosextrmuy.png",
            56: "imagenes/elementos/blancahhmuyextr.png",
            57: "imagenes/elementos/blancasoshhextr.png",
            58: "imagenes/elementos/blancahhextr.png",
            59: "imagenes/elementos/blancahhsosextrmuy.png",
            60: "imagenes/elementos/redondahhextr.png",
            61: "imagenes/elementos/redondahhextrmuy.png",
            62: "imagenes/elementos/redondahhsosextrmuy.png",
            63: "imagenes/elementos/redondahhsosextr.png",
            64: "imagenes/elementos/redondahh.png",
            65: "imagenes/elementos/redondahhsos.png",
            66: "imagenes/elementos/redondahhmuy.png",
            67: "imagenes/elementos/redondasoshhmuy.png",
            68: "imagenes/elementos/cuadrored.png",
            69: "imagenes/elementos/ligaduraup.png"
        }

        self.postono={
            'C6':-12,
            'C#6':-12,
            'B#5':-6,
            'B5':-6,
            'A5':0,
            'A#5':0,
            'G5':7,
            'G#5':7,
            'F5':13,
            'F#5':13,
            'E5':19,
            'E#5':19,
            'D5':24,
            'D#5':24,
            'C5':29,
            'C#5':29,
            'B4':35,
            'B#4':35,
            'A4':6,
            'A#4':6,
            'G4':11,
            'G#4':11,
            'F4':16,
            'F#4': 16,
            'E4':22,
            'E#4': 22,
            'D4':27,
            'D#4': 27,
            'C4':32,
            'C#4': 32,
            'KK':19
           }



    #-----FUNCION PARA CREAR LA FIGURA MUSICAL --------

    def FiguraMusical(self,note,tono):
        
        if self.posx==1:
            self.lbla1.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla1.setGeometry(QtCore.QRect(105, 40+self.postono[tono], 68, 71))
            self.lbla1.show()
        elif self.posx==2:
            self.lbla2.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla2.setGeometry(QtCore.QRect(150, 40+self.postono[tono], 68, 71))
            self.lbla2.show()
        elif self.posx==3:
            self.lbla3.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla3.setGeometry(QtCore.QRect(200, 40+self.postono[tono], 68, 71))
            self.lbla3.show()
        elif self.posx==4:
            self.lbla4.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla4.setGeometry(QtCore.QRect(250, 40+self.postono[tono], 68, 71))
            self.lbla4.show()
        elif self.posx==5:
            self.lbla5.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla5.setGeometry(QtCore.QRect(300, 40+self.postono[tono], 68, 71))
            self.lbla5.show()
        elif self.posx==6:
            self.lbla6.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla6.setGeometry(QtCore.QRect(350, 40+self.postono[tono], 68, 71))
            self.lbla6.show()
        elif self.posx==7:
            self.lbla7.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla7.setGeometry(QtCore.QRect(400, 40+self.postono[tono], 68, 71))
            self.lbla7.show()
        elif self.posx==8:
            self.lbla8.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla8.setGeometry(QtCore.QRect(450, 40+self.postono[tono], 68, 71))
            self.lbla8.show() 
        elif self.posx==9:
            self.lbla9.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla9.setGeometry(QtCore.QRect(500, 40+self.postono[tono], 68, 71))
            self.lbla9.show()
        elif self.posx==10:
            self.lbla10.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla10.setGeometry(QtCore.QRect(550, 40+self.postono[tono], 68, 71))
            self.lbla10.show()
        elif self.posx==11:
            self.lbla11.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla11.setGeometry(QtCore.QRect(600, 40+self.postono[tono], 68, 71))
            self.lbla11.show()
        elif self.posx==12:
            self.lbla12.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla12.setGeometry(QtCore.QRect(650, 40+self.postono[tono], 68, 71))
            self.lbla12.show()
        elif self.posx==13:
            self.lbla13.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla13.setGeometry(QtCore.QRect(700, 40+self.postono[tono], 68, 71))
            self.lbla13.show()
        elif self.posx==14:
            self.lbla14.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla14.setGeometry(QtCore.QRect(750, 40+self.postono[tono], 68, 71))
            self.lbla14.show()
        elif self.posx==15:
            self.lbla15.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla15.setGeometry(QtCore.QRect(800, 40+self.postono[tono], 68, 71))
            self.lbla15.show()
        elif self.posx==16:
            self.lbla16.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla16.setGeometry(QtCore.QRect(850, 40+self.postono[tono], 68, 71))
            self.lbla16.show()
        elif self.posx==17:
            self.lbla17.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla17.setGeometry(QtCore.QRect(900, 40+self.postono[tono], 68, 71))
            self.lbla17.show()
        elif self.posx==18:
            self.lbla18.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbla18.setGeometry(QtCore.QRect(950, 40+self.postono[tono], 68, 71))
            self.lbla18.show()
        

        elif self.posx==19:
            self.lblb1.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb1.setGeometry(QtCore.QRect(105, 146 + self.postono[tono], 68, 71))
            self.lblb1.show()
        elif self.posx==20:
            self.lblb2.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb2.setGeometry(QtCore.QRect(150, 146 + self.postono[tono], 68, 71))
            self.lblb2.show()
        elif self.posx==21:
            self.lblb3.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb3.setGeometry(QtCore.QRect(200, 146 + self.postono[tono], 68, 71))
            self.lblb3.show()
        elif self.posx==22:
            self.lblb4.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb4.setGeometry(QtCore.QRect(250, 146 + self.postono[tono], 68, 71))
            self.lblb4.show()
        elif self.posx==23:
            self.lblb5.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb5.setGeometry(QtCore.QRect(300, 146 + self.postono[tono], 68, 71))
            self.lblb5.show()
        elif self.posx==24:
            self.lblb6.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb6.setGeometry(QtCore.QRect(350, 146 + self.postono[tono], 68, 71))
            self.lblb6.show()
        elif self.posx==25:
            self.lblb7.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb7.setGeometry(QtCore.QRect(400, 146 + self.postono[tono], 68, 71))
            self.lblb7.show()
        elif self.posx==26:
            self.lblb8.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb8.setGeometry(QtCore.QRect(450, 146 + self.postono[tono], 68, 71))
            self.lblb8.show() 
        elif self.posx==27:
            self.lblb9.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb9.setGeometry(QtCore.QRect(500, 146 + self.postono[tono], 68, 71))
            self.lblb9.show()
        elif self.posx==28:
            self.lblb10.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb10.setGeometry(QtCore.QRect(550, 146 + self.postono[tono], 68, 71))
            self.lblb10.show()
        elif self.posx==29:
            self.lblb11.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb11.setGeometry(QtCore.QRect(600, 146 + self.postono[tono], 68, 71))
            self.lblb11.show()
        elif self.posx==30:
            self.lblb12.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb12.setGeometry(QtCore.QRect(650, 146 + self.postono[tono], 68, 71))
            self.lblb12.show()
        elif self.posx==31:
            self.lblb13.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb13.setGeometry(QtCore.QRect(700, 146 + self.postono[tono], 68, 71))
            self.lblb13.show()
        elif self.posx==32:
            self.lblb14.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb14.setGeometry(QtCore.QRect(750, 146 + self.postono[tono], 68, 71))
            self.lblb14.show()
        elif self.posx==33:
            self.lblb15.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb15.setGeometry(QtCore.QRect(800, 146 + self.postono[tono], 68, 71))
            self.lblb15.show()
        elif self.posx==34:
            self.lblb16.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb16.setGeometry(QtCore.QRect(850, 146 + self.postono[tono], 68, 71))
            self.lblb16.show()
        elif self.posx==35:
            self.lblb17.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb17.setGeometry(QtCore.QRect(900, 146 + self.postono[tono], 68, 71))
            self.lblb17.show()
        elif self.posx==36:
            self.lblb18.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblb18.setGeometry(QtCore.QRect(950, 146 + self.postono[tono], 68, 71))
            self.lblb18.show()
        
         
        elif self.posx==37:
            self.lblc1.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc1.setGeometry(QtCore.QRect(105, 260+self.postono[tono], 68, 71))
            self.lblc1.show()
        elif self.posx==38:
            self.lblc2.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc2.setGeometry(QtCore.QRect(150, 260+self.postono[tono], 68, 71))
            self.lblc2.show()
        elif self.posx==39:
            self.lblc3.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc3.setGeometry(QtCore.QRect(200, 260+self.postono[tono], 68, 71))
            self.lblc3.show()
        elif self.posx==40:
            self.lblc4.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc4.setGeometry(QtCore.QRect(250, 260+self.postono[tono], 68, 71))
            self.lblc4.show()
        elif self.posx==41:
            self.lblc5.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc5.setGeometry(QtCore.QRect(300, 260+self.postono[tono], 68, 71))
            self.lblc5.show()
        elif self.posx==42:
            self.lblc6.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc6.setGeometry(QtCore.QRect(350, 260+self.postono[tono], 68, 71))
            self.lblc6.show()
        elif self.posx==43:
            self.lblc7.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc7.setGeometry(QtCore.QRect(400, 260+self.postono[tono], 68, 71))
            self.lblc7.show()
        elif self.posx==44:
            self.lblc8.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc8.setGeometry(QtCore.QRect(450, 260+self.postono[tono], 68, 71))
            self.lblc8.show() 
        elif self.posx==45:
            self.lblc9.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc9.setGeometry(QtCore.QRect(500, 260+self.postono[tono], 68, 71))
            self.lblc9.show()
        elif self.posx==46:
            self.lblc10.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc10.setGeometry(QtCore.QRect(550, 260+self.postono[tono], 68, 71))
            self.lblc10.show()
        elif self.posx==47:
            self.lblc11.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc11.setGeometry(QtCore.QRect(600, 260+self.postono[tono], 68, 71))
            self.lblc11.show()
        elif self.posx==48:
            self.lblc12.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc12.setGeometry(QtCore.QRect(650, 260+self.postono[tono], 68, 71))
            self.lblc12.show()
        elif self.posx==49:
            self.lblc13.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc13.setGeometry(QtCore.QRect(700, 260+self.postono[tono], 68, 71))
            self.lblc13.show()
        elif self.posx==50:
            self.lblc14.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc14.setGeometry(QtCore.QRect(750, 260+self.postono[tono], 68, 71))
            self.lblc14.show()
        elif self.posx==51:
            self.lblc15.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc15.setGeometry(QtCore.QRect(800, 260+self.postono[tono], 68, 71))
            self.lblc15.show()
        elif self.posx==52:
            self.lblc16.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc16.setGeometry(QtCore.QRect(850, 260+self.postono[tono], 68, 71))
            self.lblc16.show()
        elif self.posx==53:
            self.lblc17.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc17.setGeometry(QtCore.QRect(900, 260+self.postono[tono], 68, 71))
            self.lblc17.show()
        elif self.posx==54:
            self.lblc18.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lblc18.setGeometry(QtCore.QRect(950, 260+self.postono[tono], 68, 71))
            self.lblc18.show()
        

        elif self.posx==55:
            self.lbld1.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld1.setGeometry(QtCore.QRect(105, 374+self.postono[tono], 68, 71))
            self.lbld1.show()
        elif self.posx==56:
            self.lbld2.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld2.setGeometry(QtCore.QRect(150, 374+self.postono[tono], 68, 71))
            self.lbld2.show()
        elif self.posx==57:
            self.lbld3.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld3.setGeometry(QtCore.QRect(200, 374+self.postono[tono], 68, 71))
            self.lbld3.show()
        elif self.posx==58:
            self.lbld4.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld4.setGeometry(QtCore.QRect(250, 374+self.postono[tono], 68, 71))
            self.lbld4.show()
        elif self.posx==59:
            self.lbld5.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld5.setGeometry(QtCore.QRect(300, 374+self.postono[tono], 68, 71))
            self.lbld5.show()
        elif self.posx==60:
            self.lbld6.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld6.setGeometry(QtCore.QRect(350, 374+self.postono[tono], 68, 71))
            self.lbld6.show()
        elif self.posx==61:
            self.lbld7.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld7.setGeometry(QtCore.QRect(400, 374+self.postono[tono], 68, 71))
            self.lbld7.show()
        elif self.posx==62:
            self.lbld8.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld8.setGeometry(QtCore.QRect(450, 374+self.postono[tono], 68, 71))
            self.lbld8.show() 
        elif self.posx==63:
            self.lbld9.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld9.setGeometry(QtCore.QRect(500, 374+self.postono[tono], 68, 71))
            self.lbld9.show()
        elif self.posx==64:
            self.lbld10.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld10.setGeometry(QtCore.QRect(550, 374+self.postono[tono], 68, 71))
            self.lbld10.show()
        elif self.posx==65:
            self.lbld11.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld11.setGeometry(QtCore.QRect(600, 374+self.postono[tono], 68, 71))
            self.lbld11.show()
        elif self.posx==66:
            self.lbld12.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld12.setGeometry(QtCore.QRect(650, 374+self.postono[tono], 68, 71))
            self.lbld12.show()
        elif self.posx==67:
            self.lbld13.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld13.setGeometry(QtCore.QRect(700, 374+self.postono[tono], 68, 71))
            self.lbld13.show()
        elif self.posx==68:
            self.lbld14.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld14.setGeometry(QtCore.QRect(750, 374+self.postono[tono], 68, 71))
            self.lbld14.show()
        elif self.posx==69:
            self.lbld15.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld15.setGeometry(QtCore.QRect(800, 374+self.postono[tono], 68, 71))
            self.lbld15.show()
        elif self.posx==70:
            self.lbld16.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld16.setGeometry(QtCore.QRect(850, 374+self.postono[tono], 68, 71))
            self.lbld16.show()
        elif self.posx==71:
            self.lbld17.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld17.setGeometry(QtCore.QRect(900, 374+self.postono[tono], 68, 71))
            self.lbld17.show()
        elif self.posx==72:
            self.lbld18.setPixmap(QtGui.QPixmap(self.simbolo[note]))
            self.lbld18.setGeometry(QtCore.QRect(950, 374+self.postono[tono], 68, 71))
            self.lbld18.show()
        self.posx+=1

    def LimpiaLabel(self):
        
        self.lbla1.setPixmap(QtGui.QPixmap())
        self.lbla2.setPixmap(QtGui.QPixmap())
        self.lbla3.setPixmap(QtGui.QPixmap())
        self.lbla4.setPixmap(QtGui.QPixmap())
        self.lbla5.setPixmap(QtGui.QPixmap())
        self.lbla6.setPixmap(QtGui.QPixmap())
        self.lbla7.setPixmap(QtGui.QPixmap())
        self.lbla8.setPixmap(QtGui.QPixmap())
        self.lbla9.setPixmap(QtGui.QPixmap())
        self.lbla10.setPixmap(QtGui.QPixmap())
        self.lbla11.setPixmap(QtGui.QPixmap())
        self.lbla12.setPixmap(QtGui.QPixmap())
        self.lbla13.setPixmap(QtGui.QPixmap())
        self.lbla14.setPixmap(QtGui.QPixmap())
        self.lbla15.setPixmap(QtGui.QPixmap())
        self.lbla16.setPixmap(QtGui.QPixmap())
        self.lbla17.setPixmap(QtGui.QPixmap())
        self.lbla18.setPixmap(QtGui.QPixmap())
        self.lblb1.setPixmap(QtGui.QPixmap())
        self.lblb2.setPixmap(QtGui.QPixmap())
        self.lblb3.setPixmap(QtGui.QPixmap())
        self.lblb4.setPixmap(QtGui.QPixmap())
        self.lblb5.setPixmap(QtGui.QPixmap())
        self.lblb6.setPixmap(QtGui.QPixmap())
        self.lblb7.setPixmap(QtGui.QPixmap())
        self.lblb8.setPixmap(QtGui.QPixmap())
        self.lblb9.setPixmap(QtGui.QPixmap())
        self.lblb10.setPixmap(QtGui.QPixmap())
        self.lblb11.setPixmap(QtGui.QPixmap())
        self.lblb12.setPixmap(QtGui.QPixmap())
        self.lblb13.setPixmap(QtGui.QPixmap())
        self.lblb14.setPixmap(QtGui.QPixmap())
        self.lblb15.setPixmap(QtGui.QPixmap())
        self.lblb16.setPixmap(QtGui.QPixmap())
        self.lblb17.setPixmap(QtGui.QPixmap())
        self.lblb18.setPixmap(QtGui.QPixmap())
        self.lblc1.setPixmap(QtGui.QPixmap())
        self.lblc2.setPixmap(QtGui.QPixmap())
        self.lblc3.setPixmap(QtGui.QPixmap())
        self.lblc4.setPixmap(QtGui.QPixmap())
        self.lblc5.setPixmap(QtGui.QPixmap())
        self.lblc6.setPixmap(QtGui.QPixmap())
        self.lblc7.setPixmap(QtGui.QPixmap())
        self.lblc8.setPixmap(QtGui.QPixmap())
        self.lblc9.setPixmap(QtGui.QPixmap())
        self.lblc10.setPixmap(QtGui.QPixmap())
        self.lblc11.setPixmap(QtGui.QPixmap())
        self.lblc12.setPixmap(QtGui.QPixmap())
        self.lblc13.setPixmap(QtGui.QPixmap())
        self.lblc14.setPixmap(QtGui.QPixmap())
        self.lblc15.setPixmap(QtGui.QPixmap())
        self.lblc16.setPixmap(QtGui.QPixmap())
        self.lblc17.setPixmap(QtGui.QPixmap())
        self.lblc18.setPixmap(QtGui.QPixmap())
        self.lbld1.setPixmap(QtGui.QPixmap())
        self.lbld2.setPixmap(QtGui.QPixmap())
        self.lbld3.setPixmap(QtGui.QPixmap())
        self.lbld4.setPixmap(QtGui.QPixmap())
        self.lbld5.setPixmap(QtGui.QPixmap())
        self.lbld6.setPixmap(QtGui.QPixmap())
        self.lbld7.setPixmap(QtGui.QPixmap())
        self.lbld8.setPixmap(QtGui.QPixmap())
        self.lbld9.setPixmap(QtGui.QPixmap())
        self.lbld10.setPixmap(QtGui.QPixmap())
        self.lbld11.setPixmap(QtGui.QPixmap())
        self.lbld12.setPixmap(QtGui.QPixmap())
        self.lbld13.setPixmap(QtGui.QPixmap())
        self.lbld14.setPixmap(QtGui.QPixmap())
        self.lbld15.setPixmap(QtGui.QPixmap())
        self.lbld16.setPixmap(QtGui.QPixmap())
        self.lbld17.setPixmap(QtGui.QPixmap())
        self.lbld18.setPixmap(QtGui.QPixmap())
        self.lbla1.show()
        self.lbla2.show()
        self.lbla3.show()
        self.lbla4.show()
        self.lbla5.show()
        self.lbla6.show()
        self.lbla7.show()
        self.lbla8.show()
        self.lbla9.show()
        self.lbla10.show()
        self.lbla11.show()
        self.lbla12.show()
        self.lbla13.show()
        self.lbla14.show()
        self.lbla15.show()
        self.lbla16.show()
        self.lbla17.show()
        self.lbla18.show()
        self.lblb1.show()
        self.lblb2.show()
        self.lblb3.show()
        self.lblb4.show()
        self.lblb5.show()
        self.lblb6.show()
        self.lblb7.show()
        self.lblb8.show()
        self.lblb9.show()
        self.lblb10.show()
        self.lblb11.show()
        self.lblb12.show()
        self.lblb13.show()
        self.lblb14.show()
        self.lblb15.show()
        self.lblb16.show()
        self.lblb17.show()
        self.lblb18.show()
        self.lblc1.show()
        self.lblc2.show()
        self.lblc3.show()
        self.lblc4.show()
        self.lblc5.show()
        self.lblc6.show()
        self.lblc7.show()
        self.lblc8.show()
        self.lblc9.show()
        self.lblc10.show()
        self.lblc11.show()
        self.lblc12.show()
        self.lblc13.show()
        self.lblc14.show()
        self.lblc15.show()
        self.lblc16.show()
        self.lblc17.show()
        self.lblc18.show()
        self.lbld1.show()
        self.lbld2.show()
        self.lbld3.show()
        self.lbld4.show()
        self.lbld5.show()
        self.lbld6.show()
        self.lbld7.show()
        self.lbld8.show()
        self.lbld9.show()
        self.lbld10.show()
        self.lbld11.show()
        self.lbld12.show()
        self.lbld13.show()
        self.lbld14.show()
        self.lbld15.show()
        self.lbld16.show()
        self.lbld17.show()
        self.lbld18.show()

    def Crearnota (self, duracion , tono):
        
        if duracion >= 0 and  duracion < 0.19:
            tiempo=2
        elif duracion >= 0.19 and  duracion < 0.32:
            tiempo=4
        elif duracion >= 0.32 and  duracion < 0.44:
            tiempo=6
        elif duracion >= 0.44 and  duracion < 0.63:
            tiempo=8
        elif duracion >= 0.63 and  duracion < 0.86:
            tiempo=12
        elif duracion >= 0.86 and  duracion < 1.25:
            tiempo=16
        elif duracion >= 1.25 and  duracion < 1.75:
            tiempo=28
        elif duracion >= 1.75 and  duracion < 2.5:
            tiempo=32
        elif duracion >= 2.5:
            tiempo=48
            
        #---------NOTAS NATURALES---------------
        if tono=='A4' or tono=='D4' or tono=='E4' or tono=='F4' or tono=='G4':
            if tiempo==2:
                self.FiguraMusical(29,tono)
            elif tiempo==4:
                self.FiguraMusical(21,tono)
            elif tiempo==6:
                self.FiguraMusical(21,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(29,tono)                    
            elif tiempo==8:
                self.FiguraMusical(19,tono)
            elif tiempo==12:
                self.FiguraMusical(19,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(21,tono) 
            elif tiempo==16:
                self.FiguraMusical(11,tono)
            elif tiempo==28:
                self.FiguraMusical(11,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(19,tono) 
            elif tiempo==32:
                self.FiguraMusical(4,tono)
            elif tiempo==48:
                self.FiguraMusical(4,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(11,tono) 
                    
        elif tono=='F5' or tono=='G5' or tono=='B4' or tono=='C5' or tono=='D5' or tono=='E5':
            if tiempo==2:
                self.FiguraMusical(30,tono)
            elif tiempo==4:
                self.FiguraMusical(22,tono)
            elif tiempo==6:
                self.FiguraMusical(22,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(30,tono)  
            elif tiempo==8:
                self.FiguraMusical(13,tono)
            elif tiempo==12:
                self.FiguraMusical(13,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(22,tono)  
            elif tiempo==16:
                self.FiguraMusical(6,tono)
            elif tiempo==28:
                self.FiguraMusical(6,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(13,tono)  
            elif tiempo==32:
                self.FiguraMusical(64,tono)
            elif tiempo==48:
                self.FiguraMusical(64,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(6,tono)  
                 
        elif tono=='C4':
            if tiempo==2:
                self.FiguraMusical(35,tono)
            elif tiempo==4:
                self.FiguraMusical(23,tono)
            elif tiempo==6:
                self.FiguraMusical(23,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(35,tono)  
            elif tiempo==8:
                self.FiguraMusical(14,tono)
            elif tiempo==12:
                self.FiguraMusical(14,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(23,tono)  
            elif tiempo==16:
                self.FiguraMusical(5,tono)
            elif tiempo==28:
                self.FiguraMusical(5,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(14,tono)  
            elif tiempo==32:
                self.FiguraMusical(1,tono)
            elif tiempo==48:
                self.FiguraMusical(1,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(5,tono)  

        elif tono=='B5':
            if tiempo==2:
                self.FiguraMusical(47,tono)
            elif tiempo==4:
                self.FiguraMusical(50,tono)
            elif tiempo==6:
                self.FiguraMusical(50,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(47,tono)  
            elif tiempo==8:
                self.FiguraMusical(52,tono)
            elif tiempo==12:
                self.FiguraMusical(52,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(50,tono)  
            elif tiempo==16:
                self.FiguraMusical(58,tono)
            elif tiempo==28:
                self.FiguraMusical(58,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(52,tono)  
            elif tiempo==32:
                self.FiguraMusical(60,tono)
            elif tiempo==48:
                self.FiguraMusical(60,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(58,tono)  

        elif tono=='C6':
            if tiempo==2:
                self.FiguraMusical(45,tono)
            elif tiempo==4:
                self.FiguraMusical(48,tono)
            elif tiempo==6:
                self.FiguraMusical(48,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(45,tono)
            elif tiempo==8:
                self.FiguraMusical(53,tono)
            elif tiempo==12:
                self.FiguraMusical(53,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(48,tono)
            elif tiempo==16:
                self.FiguraMusical(56,tono)
            elif tiempo==28:
                self.FiguraMusical(56,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(53,tono)
            elif tiempo==32:
                self.FiguraMusical(61,tono)
            elif tiempo==48:
                self.FiguraMusical(61,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(56,tono)

        elif tono=='A5':
            if tiempo==2:
                self.FiguraMusical(31,tono)
            elif tiempo==4:
                self.FiguraMusical(25,tono)
            elif tiempo==6:
                self.FiguraMusical(25,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(31,tono)  
            elif tiempo==8:
                self.FiguraMusical(15,tono)
            elif tiempo==12:
                self.FiguraMusical(15,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(25,tono)  
            elif tiempo==16:
                self.FiguraMusical(7,tono)
            elif tiempo==28:
                self.FiguraMusical(7,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(15,tono)  
            elif tiempo==32:
                self.FiguraMusical(66,tono)
            elif tiempo==48:
                self.FiguraMusical(66,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(7,tono)  

        #------------NOTAS ALTERADAS-------------
        elif tono=='A#4' or tono=='D#4' or tono=='E#4' or tono=='F#4' or tono=='G#4':
            if tiempo==2:
                self.FiguraMusical(36,tono)
            elif tiempo==4:
                self.FiguraMusical(24,tono)
            elif tiempo==6:
                self.FiguraMusical(24,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(36,tono)  
            elif tiempo==8:
                self.FiguraMusical(20,tono)
            elif tiempo==6:
                self.FiguraMusical(20,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(24,tono)  
            elif tiempo==16:
                self.FiguraMusical(12,tono)
            elif tiempo==6:
                self.FiguraMusical(12,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(20,tono)  
            elif tiempo==32:
                self.FiguraMusical(3,tono)
            elif tiempo==6:
                self.FiguraMusical(3,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(12,tono)  
                    
        elif tono=='F#5' or tono=='G#5' or tono=='B#4' or tono=='C#5' or tono=='D#5' or tono=='E#5':
            if tiempo==2:
                self.FiguraMusical(34,tono)
            elif tiempo==4:
                self.FiguraMusical(28,tono)
            elif tiempo==6:
                self.FiguraMusical(28,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(34,tono)  
            elif tiempo==8:
                self.FiguraMusical(17,tono)
            elif tiempo==6:
                self.FiguraMusical(17,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(28,tono)  
            elif tiempo==16:
                self.FiguraMusical(10,tono)
            elif tiempo==6:
                self.FiguraMusical(10,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(17,tono)  
            elif tiempo==32:
                self.FiguraMusical(65,tono)
            elif tiempo==6:
                self.FiguraMusical(65,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(10,tono)  
                 
        elif tono=='C#4':
            if tiempo==2:
                self.FiguraMusical(32,tono)
            elif tiempo==4:
                self.FiguraMusical(26,tono)
            elif tiempo==6:
                self.FiguraMusical(26,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(32,tono)  
            elif tiempo==8:
                self.FiguraMusical(16,tono)
            elif tiempo==6:
                self.FiguraMusical(16,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(26,tono)  
            elif tiempo==16:
                self.FiguraMusical(8,tono)
            elif tiempo==6:
                self.FiguraMusical(8,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(16,tono)  
            elif tiempo==32:
                self.FiguraMusical(2,tono)
            elif tiempo==6:
                self.FiguraMusical(2,tono)
                self.FiguraMusical(42,tono)
                self.FiguraMusical(8,tono)  

        elif tono=='B#5':
            if tiempo==2:
                self.FiguraMusical(46,tono)
            elif tiempo==4:
                self.FiguraMusical(49,tono)
            elif tiempo==6:
                self.FiguraMusical(49,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(46,tono)  
            elif tiempo==8:
                self.FiguraMusical(54,tono)
            elif tiempo==6:
                self.FiguraMusical(54,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(49,tono)  
            elif tiempo==16:
                self.FiguraMusical(57,tono)
            elif tiempo==6:
                self.FiguraMusical(57,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(54,tono)  
            elif tiempo==32:
                self.FiguraMusical(63,tono)
            elif tiempo==6:
                self.FiguraMusical(63,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(57,tono)  

        elif tono=='C#6':
            if tiempo==2:
                self.FiguraMusical(44,tono)
            elif tiempo==4:
                self.FiguraMusical(51,tono)
            elif tiempo==6:
                self.FiguraMusical(51,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(44,tono)  
            elif tiempo==8:
                self.FiguraMusical(55,tono)
            elif tiempo==6:
                self.FiguraMusical(55,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(51,tono)  
            elif tiempo==16:
                self.FiguraMusical(59,tono)
            elif tiempo==6:
                self.FiguraMusical(59,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(55,tono)  
            elif tiempo==32:
                self.FiguraMusical(62,tono)
            elif tiempo==6:
                self.FiguraMusical(62,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(59,tono)  

        elif tono=='A#5':
            if tiempo==2:
                self.FiguraMusical(33,tono)
            elif tiempo==4:
                self.FiguraMusical(27,tono)
            elif tiempo==6:
                self.FiguraMusical(27,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(33,tono)  
            elif tiempo==8:
                self.FiguraMusical(18,tono)
            elif tiempo==6:
                self.FiguraMusical(18,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(27,tono)  
            elif tiempo==16:
                self.FiguraMusical(9,tono)
            elif tiempo==6:
                self.FiguraMusical(9,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(18,tono)  
            elif tiempo==32:
                self.FiguraMusical(67,tono)
            elif tiempo==6:
                self.FiguraMusical(67,tono)
                self.FiguraMusical(69,tono)
                self.FiguraMusical(9,tono)  

        #------SILENCIOS-------------        
        elif tono=='KK':
            if tiempo==2:
                self.FiguraMusical(40,tono)
            elif tiempo==4:
                self.FiguraMusical(39,tono)
            elif tiempo==8:
                self.FiguraMusical(38,tono)
            elif tiempo==16:
                self.FiguraMusical(43,tono)
            elif tiempo==32:
                self.FiguraMusical(68,tono)            

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Souter"))

        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAyuda.setTitle(_translate("MainWindow", "Ayuda"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionNuevo.setStatusTip(_translate("MainWindow", "Crea un Archivo Nuevo"))
        self.actionNuevo.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionAbrir.setStatusTip(_translate("MainWindow", "Abrir un Archivo "))
        self.actionAbrir.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar.setStatusTip(_translate("MainWindow", "Guardar Archivo"))
        self.actionGuardar.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setStatusTip(_translate("MainWindow", "Salir de Souter"))
        self.actionAyuda_en_Souter.setText(_translate("MainWindow", "Ayuda en Souter"))
        self.actionInformaci_n_del_programa.setText(_translate("MainWindow", "Información del programa"))
    


#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())


