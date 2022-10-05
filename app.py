import time
import sys
import numpy as np

class bcolors:  # TEXT COLORS
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def slowprint(s):  # SLOW TEXT
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./1000)


slowprint(f""" {bcolors.OKGREEN}
______  __                              ________       ______                
___  / / /______ ______________ _       __  ___/______ ___  /______ _________
__  /_/ / _  __ \__  ___/_  __ `/       _____ \ _  __ \__  / _  __ `/__  ___/
_  __  /  / /_/ /_  /    / /_/ /        ____/ / / /_/ /_  /  / /_/ / _  /    
/_/ /_/   \____/ /_/     \__,_/         /____/  \____/ /_/   \__,_/  /_/     
                                                                             
""")

#LATITUD
latitud_str = input ('INSERTE LATITUD: ')
latitud = float(latitud_str)
print('SET')
print('')

#DIA
data_str = input('INSERTE DIA DEL AÑO: ') 
data = int(data_str)
print('SET')
print('')

#GRADOS
hora_str = input('INSERTE HORA ACTUAL: ')
hora = int(hora_str)
print('')
minutos_str = input('INSERTE MINUTOS ACTUALES: ')
minutos = int(minutos_str)
print('')
segundos_str = input('INSERTE SEGUNDOS ACTUALES: ')
segundos = int(segundos_str)
print('SET')
print('')

#DECLINACION
declinacion_str = 23.45*(np.sin(np.radians((360/365)*(data+284))))
declinacion = float(declinacion_str)
print(f'{bcolors.ENDC}{bcolors.BOLD}DECLINACION DE LA TIERRA: {bcolors.ENDC}{bcolors.WARNING}{declinacion_str}º{bcolors.ENDC}')
print('')

#HORA SOLAR
hora_solar_str = (15*(hora-12))+(minutos/4)+(segundos/240)
hora_solar = float(hora_solar_str)
print(f'{bcolors.ENDC}{bcolors.BOLD}HORA SOLAR: {bcolors.ENDC}{bcolors.WARNING}{hora_solar_str}º{bcolors.ENDC}')
print('')

#ALÇADA SOLAR
alçada_solar_str = np.arccos((np.sin(np.radians(latitud)))*np.sin(np.radians(declinacion))+np.cos(np.radians(latitud))*np.cos(np.radians(hora_solar)))
alçada_solar = float(alçada_solar_str)
print(f'{bcolors.ENDC}{bcolors.BOLD}ALÇADA SOLAR: {bcolors.ENDC}{bcolors.WARNING}{alçada_solar_str}º{bcolors.ENDC}')
print('')

#AZIMUT
azimut_str = np.arccos((np.cos(np.radians(latitud))*np.cos(np.radians(hora_solar))-np.sin(np.radians(alçada_solar))*np.cos(np.radians(latitud))/(np.cos(np.radians(alçada_solar))*np.sin(np.radians(latitud))))))
azimut = float(azimut_str)
print('')
print(f'{bcolors.ENDC}{bcolors.BOLD}AZIMUT: {bcolors.ENDC}{bcolors.WARNING}{azimut_str}º{bcolors.ENDC}')
