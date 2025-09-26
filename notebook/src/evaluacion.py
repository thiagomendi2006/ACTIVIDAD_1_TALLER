"""
Contiene funciones para calcular puntajes y determinar el mejor equipo de una ronda.
"""


def calcular_puntaje(datos_equipo: dict):
    puntaje = datos_equipo['innovacion']*3 + datos_equipo['presentacion']*1 + ( -1 if datos_equipo['errores'] else 0)
    return puntaje

#Entrada: diccionario acum con innovacion,presentacion,errores
#Salida: puntaje (int)

def mejor_equipo_ronda(ronda: dict):
    mejor_nombre = 'a'
    mejor_puntaje = 0
#inicializamos variables en 0 para despues compararlas

    for nombre in ronda:      #recorremos cada equipo en la ronda
        datos = ronda[nombre] # guardamos en datos el diccionario del equipo actual para usar en calcular_puntaje
        puntaje = calcular_puntaje(datos)
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_nombre = nombre
    return mejor_nombre
    
#Entrada: diccionario de todos los equipos en una ronda
#Salida: El mejor equipo de la ronda
