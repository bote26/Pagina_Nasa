# Description: Este archivo contiene las funciones necesarias para comprobar si un planeta es habitable o no.
def lower_interval(y):
    return  .97 * (y ** (3.5/2)) 

def upper_interval(y):
    return 1.7 * (y ** (3.5/2))


def check_life(distancia, masa, temp):
    if distancia >= lower_interval(masa) and distancia <= upper_interval(masa) and temp >= 273 and temp <= 395:
        return True
    return False



