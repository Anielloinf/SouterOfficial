'''
Codigo funcional TESIS
Version 6.5    

GRABA Y ENTREGA NOTAS EN VIVO
IMPRIME EN CONSOLA CON UN ARRAY DEPENDIENDO DE LAS FRECUENCIAS DETECTADAS

OCTAVA DEL ERROR - ELIMINAO 
08/01/2020

'''

from numpy import array, diff, where, split
import pyaudio
import soundfile
import numpy as np
from math import log2, pow
from scipy.stats import mode

import matplotlib.pyplot as plt

# Inicializa Pyaudio
p = pyaudio.PyAudio()

# Configura parametros del Stream 
buffer_size = 1024
pyaudio_format = pyaudio.paInt16
n_channels = 1
samplerate = 44100
stream = p.open(format=pyaudio_format,
                channels=n_channels,
                rate=samplerate,
                input=True,
                frames_per_buffer=buffer_size)


Fotas=['Nada','C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1','A1', 'A#1', 'B1', 
'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2','A2', 'A#2', 'B2', 
'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3','A3', 'A#3', 'B3',  
'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4','A4', 'A#4', 'B4', 
'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5','A5', 'A#5', 'B5',  
'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6','A6', 'A#6', 'B6',  ]
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


def fourierRMS(magnitudes):
	rmsFou=np.sum(magnitudes**2)

	return np.sqrt(rmsFou)


#Subrutina para filtrar ruido 
def findPeak(magnitude_values, noise_level):

	#el noise level es un valor que se ajusta manual e indica un filtro, a mayor noise level, menos valores quedaran vivos


	splitter = 0
	#arroja cero a las magnitudes de FFT filtrados por el noise level 
	magnitude_values = np.asarray(magnitude_values)        
	low_values_indices = magnitude_values < noise_level  # En donde los valores son menores que el noise level
	magnitude_values[low_values_indices] = 0  # Se vuelven cero todos los valores menores al noise level
   
	indices = []
	magnitudes=[]
	flag_start_looking = False

	both_ends_indices = []

	length = len(magnitude_values)
	for i in range(length):
		if magnitude_values[i] != splitter:
			if not flag_start_looking:
				flag_start_looking = True
				both_ends_indices = [0, 0]
				both_ends_indices[0] = i
		else:
			if flag_start_looking:
				flag_start_looking = False
				both_ends_indices[1] = i
				# add both_ends_indices in to indices
				indices.append(both_ends_indices)
				magnitud_prom=fourierRMS(magnitude_values[both_ends_indices[0]:both_ends_indices[1]])##### evaluar si conviene definir la magnitud resultante con algo distinto al promedio
				magnitudes.append(magnitud_prom)


	''' indices es un arreglo de los indices que definen los
        segmentos cuya zona intermedia es mayor al noise_level'''
     
	return indices, magnitudes  

def extraerFrecuenciaYMagnitud(indices, magnitudes, freq_bins, freq_threshold=2):
    
	extracted_freqs = []

	for index in indices:
		freqs_range = freq_bins[index[0]: index[1]]
		#avg_freq = round(np.average(freqs_range)) #Promedia y redondea la frecuencia freqs_range

		avg_freq = np.average(freqs_range) #Promedia la frecuencia freqs_range
		'''Al no redondear es posible que resulten valores muy parecidos cuando la oscilación sobre
		el noise_value sea de alta frecuencia
		'''
		if avg_freq not in extracted_freqs:
			extracted_freqs.append(avg_freq)
		
		# group extracted frequency by nearby=freq_threshold (tolerate gaps=freq_threshold)
	group_similar_values = split(extracted_freqs, where(diff(extracted_freqs) > freq_threshold)[0]+1 )

	# calculate the average of similar value
	extracted_freqs = []
	for group in group_similar_values:
		listfrec=(np.average(group))
		
		'''if listfrec>30 and listfrec<4000:
			extracted_freqs.append(pitching(listfrec))'''
		extracted_freqs.append(pitching(listfrec))
    
	#print("freq_components", extracted_freqs)
	#print("Magn_components", magnitudes)
	return extracted_freqs, magnitudes

def EncontrarNotaEnSenal(signal,number_samples,samplerate):
	# FFT calculation
    # Calculo de FFT a signal

	fft_data = np.fft.fft(signal)
	normalization_data = np.abs(fft_data)/number_samples
        
	magnitude_values = normalization_data[range(len(fft_data)//2)] # Arreglo de magnitudes en el espectro de frecuencias positivas
        
	freq_bins =  np.arange(number_samples//2) * samplerate/number_samples

    # list of possible frequencies bins
    #freq_bins, Lista de las frecuencias a las que se les calcula su magnitud con fft.fft(signal)

	indices, magnitudes = findPeak(magnitude_values=magnitude_values, noise_level=50)

#Arreglo con los indices de los segmentos mayores a noise_level y el promedio de la magnitudes de ese segmento

	notasExtraidas, magnitudes2 = extraerFrecuenciaYMagnitud(indices=indices, magnitudes=magnitudes, freq_bins=freq_bins)
	#frequencies tiene la frecuencia en el símbolo del segmento de nota que le corresponde
	return notasExtraidas,magnitudes2


arrgloNotacion=np.asarray([])
MagEnElTiempo=[]
arrNotasTocadas=["Silencio"]
sigRMS0=0
df=0
capNota=False
magnitudes=np.asarray([])
maDetallada=np.asarray([])
arrPuntoRojo=np.asarray([]) #Quitar sino funciona
#while len(MagEnElTiempo)<200:
while True:
	try:

		audiobuffer = stream.read(buffer_size)

		#audio_samples, sample_rate  = soundfile.read(audiobuffer, dtype='int16')
		signal = np.fromstring(audiobuffer, dtype=np.int16)
		number_samples = len(signal)
		sigRMS=encontrarRMS(signal)

		maDetallada=np.append(maDetallada,signal)


		df=sigRMS-sigRMS0
		if sigRMS<500 and capNota:
			#MostraNotas ANIELLO!!
			print(arrNotasTocadas)
			print(mode(arrNotasTocadas)[0][0])
			tNota=len(arrNotasTocadas)*buffer_size/samplerate
			print("\n"+"###########################  Largo de la nota "+ str(tNota)+" s  ###########################"+"\n")
			print("#####################       Comienza el silencio          ####################")
			capNota=False
			arrNotasTocadas=[]

		if df>500:
			#MostraNotas ANIELLO!!
			print(arrNotasTocadas)
			print(mode(arrNotasTocadas)[0][0])
			tNota=len(arrNotasTocadas)*buffer_size/samplerate
			print("\n"+"###########################  Largo de la nota "+ str(tNota)+" s  ###########################"+"\n")
			print("-----------------------     Cambio sin silencio          ---------------------")
			capNota=True
			arrNotasTocadas=[]



		if capNota:

			notasExtraidas,magnitudes=EncontrarNotaEnSenal(signal,number_samples,samplerate)
		#signalRMSfourier=fourierRMS(normalization_data)
			notaExtraida=notasExtraidas[0]
			

		else:
			notaExtraida="Silencio"
			

		arrNotasTocadas.append(notaExtraida)


		if sigRMS>500:
			sigRMS0=sigRMS
			#df0=df
		'''else:
			if abs(sigRMS0)<1:
				if sigRMS0==0:
					sigRMS0=sigRMS0/abs(sigRMS0)'''


		if df>0:
			if sigRMS0==0:
				sigRMS0=1
			puntoRojo=df/abs(sigRMS0)
		else:
			if sigRMS==0:
				sigRMS=1
			puntoRojo=df/abs(sigRMS)

		arrPuntoRojo=np.append(arrPuntoRojo,puntoRojo)


		#MagEnElTiempo.append(signalRMSfourier)
		MagEnElTiempo.append(sigRMS)
		'''if len(magnitudes)>0:
			arrgloNotacion.append(notasExtraidas[0])
			print(notasExtraidas[0])
			#print(signalRMSfourier)
			print(sigRMS)

		else:
			tNota=len(arrgloNotacion)*buffer_size/samplerate
			if tNota!=0:
				print("\n"+"###########################  Largo de la nota "+ str(tNota)+" s  ###########################"+"\n")
				arrgloNotacion=[]'''


	except KeyboardInterrupt:
		print("*** Ctrl+C pressed, exiting")
		break
print("MagEnElTiempo "+str(len(MagEnElTiempo)))
print("arrPuntoRojo "+ str(len(arrPuntoRojo)))

plt.figure(1)       # define la grafica
plt.suptitle('Envolvente en el tiempo')


t=np.arange(len(maDetallada))/samplerate
#plt.subplot(211)    # grafica de 3x2, subgrafica 4
plt.ylabel('MagEnElTiempo')
plt.xlabel('tiempo')
plt.plot(t,maDetallada,"k")
plt.grid()

t=np.arange(len(MagEnElTiempo))*number_samples/samplerate

#plt.subplot(211)    # grafica de 3x2, subgrafica 4
plt.ylabel('MagEnElTiempo')
plt.xlabel('tiempo')
plt.plot(t,MagEnElTiempo)
plt.grid()
#plt.show()

#plt.subplot(211)    # grafica de 2x1, subgrafica 2
plt.ylabel('derivada(magnitud)')
plt.xlabel(' tiempo')
t=np.delete(t,-1)
derivada=diff(MagEnElTiempo)
plt.plot(t,derivada,"og")
plt.grid()

MagEnElTiempo=np.delete(MagEnElTiempo,-1)
#plt.subplot(211)    # grafica de 2x1, subgrafica 2
plt.ylabel('derivada/magnitud')
plt.xlabel(' tiempo')
plt.plot(t,(derivada/MagEnElTiempo)*100,"or")
plt.grid()


t=np.arange(len(arrPuntoRojo))*number_samples/samplerate

plt.ylabel('derivada/magnitud condicional')
plt.xlabel(' tiempo')
plt.plot(t,arrPuntoRojo*100,"ob")
plt.grid()


plt.show()
print("*** done recording")

stream.stop_stream()
stream.close()
p.terminate()
