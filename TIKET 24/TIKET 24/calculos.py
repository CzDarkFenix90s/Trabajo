from datetime import datetime

def calcularEdad(anioNacimiento):
    anioActual = datetime.now().year
    
    if anioNacimiento < 0 or anioNacimiento > anioActual:
        return -1
    
    edad = anioActual - anioNacimiento
    return edad

