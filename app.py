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
latitud = input ('INSERTE LATITUD: ')
print('SET')
print('')

#DIA
data = input('INSERTE DIA DEL AÑO: ') 
print('SET')
print('')

#GRADOS
hora = input('INSERTE HORA ACTUAL: ')
print('')
minutos = input('INSERTE MINUTOS ACTUALES: ')
print('')
segundos = input('INSERTE SEGUNDOS ACTUALES: ')
print('SET')
print('')

#DECLINACION
declinacion = 23.45*(np.sin(np.radians((360/365)*(data+284))))
print(f'{bcolors.ENDC}{bcolors.BOLD}DECLINACION DE LA TIERRA: {bcolors.ENDC}{bcolors.WARNING}{declinacion}º{bcolors.ENDC}')
print('')

#HORA SOLAR
hora_solar = (15*(hora-12))+(minutos/4)+(segundos/240)
print(f'{bcolors.ENDC}{bcolors.BOLD}HORA SOLAR: {bcolors.ENDC}{bcolors.WARNING}{hora_solar}º{bcolors.ENDC}')
print('')

#ALÇADA SOLAR
alçada_solar = np.arccos(np.sin(np.radians(latitud))*np.sin(np.radians(declinacion)+np.cos(np.radians(latitud)*np.cos(np.radians(hora_solar)))))
print(f'{bcolors.ENDC}{bcolors.BOLD}ALÇADA SOLAR: {bcolors.ENDC}{bcolors.WARNING}{alçada_solar}º{bcolors.ENDC}')
print('')

#AZIMUT
azimut = np.arccos((np.cos(np.radians(latitud))*np.cos(np.radians(hora_solar))-np.sin(np.radians(alçada_solar))*np.cos(np.radians(latitud))/(np.cos(np.radians(alçada_solar))*np.sin(np.radians(latitud)))))
print(f'{bcolors.ENDC}{bcolors.BOLD}ALÇADA SOLAR: {bcolors.ENDC}{bcolors.WARNING}{alçada_solar}º{bcolors.ENDC}')
print('')
