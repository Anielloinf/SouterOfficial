'''
Codigo funcional TESIS
Version 6.5    

GRABA Y ENTREGA NOTAS EN VIVO
IMPRIME EN CONSOLA CON UN ARRAY DEPENDIENDO DE LAS FRECUENCIAS DETECTADAS

OCTAVA DEL ERROR - ELIMINAO 
08/01/2020

'''

from numpy import array, diff, where, split
import numpy as np
from math import log2, pow
from scipy.stats import mode

import matplotlib.pyplot as plt

Fotas=['KK','C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1','A1', 'A#1', 'B1', 
'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2','A2', 'A#2', 'B2', 
'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3','A3', 'A#3', 'B3',  
'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4','A4', 'A#4', 'B4', 
'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5','A5', 'A#5', 'B5',  
'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6','A6', 'A#6', 'B6', 'A7' ]
#'A0', 'A#0', 'B0', 'C0', 'C#0', 'D0', 'D#0', 'E0', 'F0', 'F#0', 'G0', 'G#0',
#'A7', 'A#7', 'B7', 'C7', 'C#7', 'D7', 'D#7', 'E7', 'F7', 'F#7', 'G7', 'G#7']


BordesFotas=np.array([31.772199163987505, 33.66147244087802, 35.66308775290277, 37.78372530509745,
 40.03046252816015, 42.41079769871837, 44.93267496413025, 47.604510855337864, 50.43522237625692, 
 53.434256763448325, 56.61162301539206, 59.97792529658917, 63.54439832797501, 67.32294488175604, 
 71.32617550580554, 75.5674506101949, 80.06092505632031, 84.82159539743674, 89.86534992826049, 
 95.20902171067574, 100.87044475251383, 106.86851352689665, 113.22324603078411, 119.95585059317834, 
 127.08879665595005, 134.64588976351206, 142.65235101161107, 151.13490122038982, 160.1218501126406, 
 169.64319079487348, 179.730699856521, 190.41804342135146, 201.74088950502767, 213.73702705379333, 
 226.44649206156822, 239.91170118635668, 254.1775933119001, 269.2917795270241, 285.30470202322215, 
 302.26980244077964, 320.2437002252812, 339.28638158974695, 359.461399713042, 380.8360868427029, 
 403.48177901005533, 427.47405410758665, 452.8929841231366, 479.82340237271336, 508.35518662379997, 
 538.5835590540485, 570.6094040464443, 604.5396048815592, 640.4874004505626, 678.5727631794939, 
 718.9227994260838, 761.672173685406, 806.9635580201107, 854.948108215173, 905.7859682462732, 
 959.6468047454267, 1016.7103732475999, 1077.167118108097, 1141.2188080928886, 1209.0792097631183, 
 1280.9748009011253, 1357.1455263589878, 1437.8455988521675, 1523.344347370812, 1613.9271160402213, 
 1709.896216430346, 1811.5719364925465, 1919.2936094908534, 2033.4207464951999], dtype=float)


    
def pitching(freq):
    
	fotasBoole=BordesFotas>freq
	indFotas=np.where(fotasBoole)# indFotas, arreglo con los indices de BordesFotas cuyo valor es mayores a freq

	if len(indFotas[0])>0:
		q=indFotas[0][0]
	else:
		q=0

	nota=Fotas[q]

	return	nota #+' '+ str(freq)

# En funcion de las muestras, entrega el tiempo de duracion de las notas 
def encontrarRMS(signal):
	signalAux=signal/np.sqrt(len(signal)) 
	'''Se debe dividir por la raíz cuadrada del número de muestras para 
	que los valores de signal no se desborden mas adelante. **0.5'''

	rms2=np.sum(signalAux**2) #rms2 es el valor rms de signal elevado al cuadrado

	return np.sqrt(rms2) #Retorna el valor rms del arreglo signal, requiere que magnitudes haya sido normalizada


#Subrutina para filtrar ruido 
def EncontrarPicos(magnitude_values, noise_level):

	#el noise level es un valor que se ajusta manual e indica un filtro, a mayor noise level, menos valores quedaran vivos


	splitter = 0
	#arroja cero a las magnitudes de FFT filtrados por el noise level 
	magnitude_values = np.asarray(magnitude_values)        
	low_values_indices = magnitude_values < noise_level  # En donde los valores son menores que el noise level
	magnitude_values[low_values_indices] = 0  # Se vuelven cero todos los valores menores al noise level
   
	ArrIndDeSegmentos = []
	ArrDeSegmentos=[]
	flag_start_looking = False

	both_ends_indices = []

	length = len(magnitude_values)
	
	for i in range(length):
		
		if magnitude_values[i] != splitter:

			if not flag_start_looking:
				flag_start_looking = True
				both_ends_indices = [0, 0]
				both_ends_indices[0] = i

			if i==length-1 and flag_start_looking:
				
				both_ends_indices[1]=i
				
				SegMayorQ=np.asarray(magnitude_values[both_ends_indices[0]:both_ends_indices[1]+1])##### Se le suma uno para incluir el último valor
				ArrDeSegmentos.append(SegMayorQ)
				ArrIndDeSegmentos.append(np.arange(both_ends_indices[0],both_ends_indices[1]+1))
				
				




		else:

			if flag_start_looking:
				flag_start_looking = False
				both_ends_indices[1] = i
				
				SegMayorQ=np.asarray(magnitude_values[both_ends_indices[0]:both_ends_indices[1]])
				ArrDeSegmentos.append(SegMayorQ)	##### Se añade a SegMayorQ todos los valores mayores a noise_level
				ArrIndDeSegmentos.append(np.arange(both_ends_indices[0],both_ends_indices[1]))
	
	
	if len(ArrDeSegmentos)==0:		#se coloca este if para evitar errores al no encontrar valores superiores a noise_level
		ArrDeSegmentos,ArrIndDeSegmentos=[[0]],[[0]] 

	indices,magnitudes =EncontrarMaximos(ArrDeSegmentos,ArrIndDeSegmentos)


	''' indices es un arreglo de los indices que definen los
        segmentos cuya zona intermedia es mayor al noise_level'''
     
	return indices, magnitudes  

def EncontrarNotaEnSenal(signal,samplerate,noise_level=50,factorDeApreciacion=0.8):	###### Veririficar uso de factorDeApreciacion, borrar para version final
	# FFT calculation
    # Calculo de FFT a signal

	fft_data = np.fft.fft(signal)
	normalization_data = np.abs(fft_data)/len(signal)
        
	magnitude_values = normalization_data[range(len(fft_data)//2)] # Arreglo de magnitudes en el espectro de frecuencias positivas
        
	print("Largo magnitude_values "+str(len(magnitude_values)))


	indPicos,magPicos=EncontrarPicos(magnitude_values, noise_level=noise_level)
	print("Largo indPicos "+str(len(indPicos)))
	print("Largo magPicos "+str(len(magPicos)))
	

	
	indDeterminante,magnitudNota	=	DefinirIndiceDeNota(indPicos,magPicos,lSup=2**(1/24),lInf=2**(-1/24))
	freqExtraida	=	(indDeterminante)*samplerate/len(signal)
	print('freqExtraida '+ str(freqExtraida))
	print('\n'+'################################')
	notaExtraida	=	pitching(freqExtraida)


		
	
	return notaExtraida,magnitudNota



def DefinirIndiceDeNota(indices,arreglo,lSup=2**(1/24),lInf=2**(-1/24)):
	indMax=np.argmax(arreglo)
	indMax=indices[indMax]

	indNota=0
	picoNota=0

	salir=False
	i=0

	while (not salir) and i<len(arreglo)	:
		
		cociente=	indMax/(round(indMax/indices[i])*indices[i])

		if cociente<=lSup and cociente>=lInf:
			
			indNota=indices[i]
			picoNota=arreglo[i]
			salir=True
			# El metodo termina al encontrar el primer término porque se están inspeccionando los índices de menor a mayor
			print('indNota ######'+ str(indNota))
			print('picoNota '+ str(picoNota))
			print('indMax #######'+ str(indMax))

		i+=1
	return	indNota,	picoNota



def EncontrarMaximos(arregloDeArreglos, arregloDeIndices):
	arregloDeMaximos=[]
	arregloDeIndicesMaximos=[]
	for i in range(len(arregloDeArreglos)):
		arregloDeMaximos=np.append(arregloDeMaximos,np.max(arregloDeArreglos[i]))

		

		arregloDeIndicesMaximos=np.append(arregloDeIndicesMaximos,arregloDeIndices[i][np.argmax(arregloDeArreglos[i])])
		
	return	arregloDeIndicesMaximos,arregloDeMaximos


