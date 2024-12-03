from datetime import datetime
def determinarResultadosIMC(nm1):
    if nm1 >= 0 and nm1< 16:
        return "Delgadez severa"
    elif nm1 >= 16 and nm1< 17:
        return "Delgadez moderada"
    elif nm1 >= 17 and nm1< 18.5:
        return "Delgadez leve"
    elif nm1 >= 18.5 and nm1< 25:
        return "Peso normal"
    elif nm1 >= 25 and nm1<30:
        return "Sobrepeso"
    elif nm1 >= 30 and nm1< 35:
        return "Obesidad Grado 1"
    elif nm1 >= 35 and nm1< 40:
        return "Obesidad Grado 2"
    elif nm1 >= 40:
        return "Obesidad Grado 3"
    else:
        return "IMC fuera de rango"
def calcularEdad(anioNacimiento):
    anioActual = datetime.now().year
    
    if anioNacimiento < 0 or anioNacimiento > anioActual:
        return -1
    
    edad = anioActual - anioNacimiento
    return edad

def encontrarMenor(l1, l2, l3, l4):
    menorActual = l1
    if l2 < menorActual:
        menorActual = l2
    if l3 < menorActual:
        menorActual = l3
    if l4 < menorActual:
        menorActual = l4
    return menorActual





