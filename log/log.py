#Logfile
#Bitacora de eventos del sistema

import sys
from time import gmtime, strftime

def evento(linea=""):
    try:
        with open("bitacora.txt","a") as archLog:
            hf = strftime("%H:%M:%S",gmtime())
            archLog.write(hf + " | " + linea + "\n")
        archLog.close()
        print("envento: {}").format(linea)
    except OSError:
        print("No se puede abrir el archivo bitacora.txt",sys.exc_info()[0])
        print(sys.exc_info()[0],"Nuevo archivo creado")
        with open("bitacora"+gmtime()+".txt","a") as archLog:
            hf = strftime("%H:%M:%S",gmtime())
            archLog.write(hf + " | " + linea + "\n")
        archLog.close()
