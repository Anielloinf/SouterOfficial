import math
import numpy as np 
import matplotlib.pyplot as plt 
import scipy.io.wavfile as waves
import DamianAniello as daan


def TransFuriel(SonidoATransf):
	fft_data = np.fft.fft(SonidoATransf)
	normalization_data = np.abs(fft_data)/len(fft_data)
        
	MagEnFrecuencia = normalization_data[range(len(fft_data)//2)] # Arreglo de magnitudes en el espectro de frecuencias positivas
        
	frecEje =  np.arange(len(fft_data)//2) * muestreo/len(fft_data)
	return MagEnFrecuencia,frecEje

def Ventana(ArregloASegmentar,InicioDeVent,largoDeVentana):

	return ArregloASegmentar[InicioDeVent:InicioDeVent+largoDeVentana]


def AnalizarAudio(sonido,largoDeVentana, muestreo,archivoGenerado,umbralRuido=50,variacionDeCambioNota=200,factorDeApreciacion=0.7,noise_level=5):
	sonidoAux=np.asarray(sonido[[range(len(sonido)-len(sonido)%largoDeVentana)]])
	print("sonidoAux1 " +str(len(sonido)))
	sonidoAux=np.split(sonidoAux,len(sonidoAux)/largoDeVentana)
	print("sonidoAux2 " +str(len(sonidoAux)))
	print("elemento sonidoAux "+str(len(sonidoAux[0])))

	senalConNota=np.asarray([])
	notaExtraida='KK'



	umbralRuido=umbralRuido	#umbralRuido es el valor que determina cuando la señal deja o no de ser silencio

	variacionDeCambioNota=variacionDeCambioNota #variacionDeCambioNota es el cambio de magnitud que determina cuando una nota empieza a tocarse despues de haber tocado una anteriormente
	

	factorDeApreciacion=factorDeApreciacion		#factorDeApreciacion define la relacion máxima que tiene la magnitud mas alta del espectro de frecuencia con respecto a la magnitud que corresponde a la frecuencia de la nota tocada
	
	noise_level=noise_level		#noise_level es el valor mínimo en el espectro de frecuencia que se considera como posible pico de la frecuencia representativa de la señal


	Ventana0RMS=0
	Ventana0FFT=np.zeros(largoDeVentana//2)
	Ventana0Pico=np.ones(largoDeVentana//2)

	EmpezoDescenso=False

	momento=0


	#archivo = open(carpeta+ archivoGenerado+"PartituraTexto Fa "+str(factorDeApreciacion)+".txt", 'w')
	archivo = open(carpeta+ archivoGenerado+"PartituraTexto La mero mera.txt", 'w')
	for Ventana in sonidoAux:


		Ventana=Ventana
		VentanaRMS=daan.encontrarRMS(Ventana)

		#print("VentanaRMS ### "+ str(VentanaRMS))
		'''
		if VentanaRMS >umbralRuido:
			VentanaFFT=np.fft.fft(Ventana)
			VentanaFFT=np.abs(VentanaFFT)
			#print('nota '+ str(VentanaRMS))
			VentanaFFT=VentanaFFT[range(len(VentanaFFT)//2)]/len(VentanaFFT) # arreglo con la parte positiva del espectro en frecuencia
			#print("Ventana0RMS 0 "+str(Ventana0RMS))
		else:
			VentanaRMS=0
			VentanaFFT=np.zeros(len(Ventana)//2)
			#print('silencio '+ str(max(Ventana)))
			#print(len(Ventana))
		'''

		
		 
		 
		#if max((VentanaFFT-Ventana0FFT)*Ventana0Pico)>variacionDeCambioNota or (Ventana0RMS==0 and VentanaRMS!=0) or (Ventana0RMS!=0 and VentanaRMS==0):


			#print("##########################################################################################################################################################")
		VariacionRMS=(VentanaRMS-Ventana0RMS)
		tNota=len(senalConNota)/muestreo

		cambioNotaASilencio	=	(VariacionRMS	>	variacionDeCambioNota) 	and 	EmpezoDescenso
		cambioSilencioANota =	(Ventana0RMS 	<	umbralRuido) 			and 	VentanaRMS>=umbralRuido
		cambioNotaANota		=	(Ventana0RMS 	>=	umbralRuido)			and 	VentanaRMS<umbralRuido



		if (cambioNotaASilencio or cambioSilencioANota or cambioNotaANota):

			
			
			if tNota>0.0625:
				#print("Ventana0RMS "+str(Ventana0RMS))
				print("Hola por aqui"+ str(momento))
				if Ventana0RMS<umbralRuido:
					nota="KK"
				else:
					nota,magnitudes=daan.EncontrarNotaEnSenal(senalConNota,muestreo,factorDeApreciacion=factorDeApreciacion,noise_level=noise_level)


				archivo.write("Nota 	"+ str(nota)+ "	Duración	"+ str(tNota).ljust(18,'0')+ "	Momento s	"
					+ str(momento*len(Ventana)/muestreo).ljust(18,'0')+" 	Momento muestras	" +str(momento)+"\n")



				senalConNota=Ventana
				


                    #self.ui.Crearnota(self.tNota, self.nota)
				#print('Nota ######################  '+ str(nota)+'  Tiempo ##########   '+str(tNota))
			else:
				senalConNota=np.append(senalConNota,Ventana)
			

			#print("Nota "+ str(nota)+ " Duración "+ str(tNota)+ " Momento en s "+ str(momento*1024/muestreo)+"\n")
			EmpezoDescenso=False


			
		else:
			#print("AJAAAA")
			senalConNota=np.append(senalConNota,Ventana)
			
			
			if tNota>0.0625 and VariacionRMS<0:
				EmpezoDescenso=True 
				


		Ventana0RMS=VentanaRMS
		'''Ventana0FFT=VentanaFFT*1
		
		Ventana0Pico=(Ventana0FFT<max(Ventana0FFT))'''
		momento=momento+1 
	archivo.close()
''' 
en sig0Pico el elemento de posición paralela al pico mas alto de sig0FFT se hace 0 
                y el resto de los elementos valen 1 '''
		


#carpeta ='C:/Users/Damian E Sanz M/Documents/UcDamian/TesisDocumentos2/Clon Proyecto/SouterOfficial'

#carpeta='C:/Users/Damian E Sanz M/Documents/UcDamian/TesisDocumentos2/Solfeo/'
carpeta="C:/Users/Damian E Sanz M/Desktop/Prof Wilmer/Resultados 50 200 0.7 50/"

#archivo = 'Ejercicio2 Whatsapp.wav'			#Ejercicio2 Whatsapp

archivo="Ejer 1 SonidoCaptadoPorSoutersys.wav"
#archivo='F4.wav'


archivoGenerado=archivo[:len(archivo)-4]
muestreo, sonido = waves.read(carpeta+archivo)
if type(sonido[100])==np.ndarray:
	sonido=np.average(sonido,1)	

print(len(sonido))
print('Tipo de variable de sonido'+ str(type(sonido)))
print('sonido[100] = '+ str(sonido[100]))#-4051 -11831
print('tipo de sonido[20000] = '+ str(type(sonido[100])))
print(muestreo)



largoDeVentana=1024


AnalizarAudio(sonido,largoDeVentana, muestreo,archivoGenerado,umbralRuido=50,variacionDeCambioNota=200,factorDeApreciacion=0.6,noise_level=50)


Inicio1=478*largoDeVentana
largoDeVentana1=(492)*largoDeVentana-Inicio1

SonidoATransf1=Ventana(sonido,Inicio1,largoDeVentana1)
MagEnFrecuencia1,frecEje1=TransFuriel(SonidoATransf1)

frecEje1,MagEnFrecuencia1=daan.EncontrarPicos(MagEnFrecuencia1,50)
frecEje1*=muestreo/(largoDeVentana1)
Med1=daan.encontrarRMS(SonidoATransf1)




Inicio2=657*largoDeVentana
largoDeVentana2=(681)*largoDeVentana-Inicio2

SonidoATransf2=Ventana(sonido,Inicio2,largoDeVentana2)
MagEnFrecuencia2,frecEje2=TransFuriel(SonidoATransf2)
Med2=daan.encontrarRMS(SonidoATransf2)


Inicio3=Inicio2+largoDeVentana
SonidoATransf3=Ventana(sonido,Inicio3,largoDeVentana)
MagEnFrecuencia3,frecEje3=TransFuriel(SonidoATransf3)

Med3=daan.encontrarRMS(SonidoATransf3)



plt.figure(archivo+" Ventanas de "+ str(largoDeVentana))


plt.subplot(221)    
plt.ylabel('MagEnFrec'+ str(Inicio1//largoDeVentana))
plt.xlabel('frecuencia '+ str(Med1))
#plt.plot(t,FResultante)
#plt.plot(np.arange(len(MagRms)),MagRms)
print("Largo de MagEnFrecuencia "+str(len(MagEnFrecuencia1)) )

#plt.plot(np.arange(len(MagRms)),daan.AplanarEnvolvente(MagRms,5000)[0]*MagRms)

plt.plot(frecEje1,MagEnFrecuencia1, 'pr')



plt.subplot(222)    
plt.ylabel('MagEnFrec'+ str(Inicio2//largoDeVentana))
plt.xlabel('frecuencia '+ str(Med1))
#plt.plot(t,FResultante)
#plt.plot(np.arange(len(MagRms)),MagRms)
print("Largo de MagEnFrecuencia "+str(len(MagEnFrecuencia1)) )

#plt.plot(np.arange(len(MagRms)),daan.AplanarEnvolvente(MagRms,5000)[0]*MagRms)

plt.plot(frecEje2,MagEnFrecuencia2, 'pb')


'''
plt.subplot(231)    
plt.ylabel('MagEnFrec'+ str(Inicio1))
plt.xlabel('frecuencia '+ str(Med1))
#plt.plot(t,FResultante)
#plt.plot(np.arange(len(MagRms)),MagRms)
print("Largo de MagEnFrecuencia "+str(len(MagEnFrecuencia1)) )

#plt.plot(np.arange(len(MagRms)),daan.AplanarEnvolvente(MagRms,5000)[0]*MagRms)

plt.plot(frecEje1,MagEnFrecuencia1/Med1, 'pg')

plt.subplot(232)    
plt.ylabel('MagEnFrec'+ str(Inicio2))
plt.xlabel('frecuencia '+ str(Med2))
#plt.plot(t,FResultante)
#plt.plot(np.arange(len(MagRms)),MagRms)
print("Largo de MagEnFrecuencia "+str(len(MagEnFrecuencia2)) )

plt.plot(frecEje2,MagEnFrecuencia2/Med2,'xb')


plt.subplot(233)    
plt.ylabel('MagEnFrec'+ str(Inicio3))
plt.xlabel('frecuencia '+ str(Med3))
#plt.plot(t,FResultante)
#plt.plot(np.arange(len(MagRms)),MagRms)
print("Largo de MagEnFrecuencia "+str(len(MagEnFrecuencia3)) )

plt.plot(frecEje3,MagEnFrecuencia3/Med3,'xr')
'''



'''
#plt.subplot(212)    
plt.ylabel('MagEnElTiempo')
plt.xlabel('tiempo')
#plt.plot(range(len(Funcion2)),Funcion2,'k')

plt.plot(np.arange(len(sonido)),sonido,'g')

#plt.plot(np.arange(len(sonido))/muestreo,sonido,'g')

############################
#plt.subplot(211)    
plt.ylabel('MagEnElTiempo')
plt.xlabel('tiempo')
#plt.plot(range(len(Funcion2)),Funcion2,'k')

plt.plot(np.arange(len(sonido)-1),np.diff(sonido),'b')

############################
'''

print("Largo de sonido"+ str(len(sonido)))
sonidoAux=np.asarray(sonido[[range(len(sonido)-len(sonido)%largoDeVentana)]])
print("Largo de sonidoAux"+ str(len(sonidoAux)))
sonidoAux=np.split(sonidoAux,len(sonidoAux)/largoDeVentana)
sonidoProm=np.asarray([])

for Ventana in sonidoAux:
	Ventana=Ventana*1
	VentanaRMS=daan.encontrarRMS(Ventana)
	sonidoProm=np.append(sonidoProm,VentanaRMS)


plt.subplot(212)
plt.ylabel('MagEnElTiempo')
plt.xlabel('tiempo')
#plt.plot(range(len(Funcion2)),Funcion2,'k')

plt.plot(np.arange(len(sonidoProm)),sonidoProm,'g')

print("Largo de sonidoProm"+ str(len(sonidoProm)))
print("Largo de sonidoAux"+ str(len(sonidoAux)))

#plt.plot(np.arange(len(sonido))/muestreo,sonido,'g')

############################
'''plt.subplot(211)    
plt.ylabel('MagEnElTiempo')
plt.xlabel('tiempo')'''
#plt.plot(range(len(Funcion2)),Funcion2,'k')

plt.plot(np.arange(len(sonidoProm)-1),np.diff(sonidoProm),'xb')


plt.plot(np.arange(len(sonidoProm)-1),np.ones(len(sonidoProm)-1)*200,'r')

plt.plot(np.arange(len(sonidoProm)-1),np.ones(len(sonidoProm)-1)*50,'r')

plt.plot(np.arange(len(sonidoProm)-1),np.ones(len(sonidoProm)-1)*0,'k')


plt.show()

