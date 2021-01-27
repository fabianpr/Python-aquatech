#Logfile
#Bitacora de eventos del sistema

import sys
from time import gmtime, strftime
import csv


def event(line=""):
    try:
        with open("bitacora.txt", "a") as archLog:
            hf = strftime("%H:%M:%S", gmtime())
            archLog.write(hf + " | " + line + "\n")
        archLog.close()
        print(f"Evento: {line}")
    except OSError:
        print("No se puede abrir el archivo bitacora.txt",sys.exc_info()[0])
        print(sys.exc_info()[0], "Nuevo archivo creado")
        with open("bitacora"+gmtime()+".txt", "a") as archLog:
            hf = strftime("%H:%M:%S", gmtime())
            archLog.write(hf + " | " + line + "\n")
        archLog.close()


def registry(event_line="", temp=0, pump=0, waves=0):
    try:
        with open("actividad.csv", "w") as archcsv:
            esccsv = csv.writer(archcsv, delimiter=",")
            hf = strftime("%H:%M:%S", gmtime())
            esccsv.writerow([hf, event_line, temp, pump, waves])
        archcsv.close()
        print(f"envento guardado en registro: {hf, ',', event_line, ',', temp, ',', pump, ',', waves}")
    except OSError:
        print("No se puede abrir el archivo bitacora.txt", sys.exc_info()[0])

