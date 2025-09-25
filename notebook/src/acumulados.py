"""
Contiene funciones para inicializar y actualizar los acumulados por equipo.
"""

#Crea un diccionario base con los campos:
#{"innovacion": 0, "presentacion": 0, "errores": 0, "mejores": 0, "total": 0}.
def resetear_valores():
    return {"innovacion": 0, "presentacion": 0, "errores": 0, "mejores": 0, "total": 0}

#Utilicé lambda y map únicamente para ya asegurarnos de usarlos en algun lado,
#no es lo más eficiente, preguntar si lo hacemos así o con dict comprehension
def inicializar_acumulados(evaluaciones):   
    equipos = evaluaciones[0].keys()
    acumulados = dict(map(lambda equipo: (equipo, resetear_valores()), equipos))    #map recorre la lista de equipos(nombres), lambda recibe el argumento del nombre del equipo,
    return acumulados                                                               #y con el diccionario reseteado por la función, crea una tupla ("Nombre Equipo",{"innovacion":0,"errores":0,...}), luego esa lista de tuplas es dict()
                                                                                                                                                      
#En el programa principal se puede probar así:
#(recordar(import pprint) para imprimir lindo el diccionario)
#acum = inicializar_acumulados(evaluaciones)
#pprint.porint(acum)

#Suma innovacion,presentacion,errores,totales.
#Incrementa el contador de mejores equipos si corresponde
#O sea, en una sola pasada tiene que tocar todos los campos del acumulado.

def actualizar_acumulados(acum: dict, ronda: dict, mejor: str) -> dict: 
    for equipo in ronda:
        acum[equipo]["innovacion"] += ronda[equipo]["innovacion"]
        acum[equipo]["presentacion"] += ronda[equipo]["presentacion"]
        if (equipo == mejor):
            acum[equipo]["mejores"] += 1

        acum[equipo]["total"] += (ronda[equipo]["innovacion"]*3 + ronda[equipo]["presentacion"]*1)

        if ronda[equipo]["errores"]:
            acum[equipo]["errores"] += 1
            acum[equipo]["total"] -= 1


#    Devuelve (equipo, errores) del equipo con menos errores.#

def equipo_menos_errores(acum: dict) -> tuple[str, int]:
    
    return min(((equipo, datos["errores"]) for equipo, datos in acum.items()),
               key=lambda x: x[1])

#    Retorna {equipo: promedio} usando total acumulado / cantidad de rondas.#

def promedio_por_ronda(acum: dict, evaluaciones: list) -> dict:
   
    rondas_totales = len(evaluaciones)
    return {equipo: datos["total"] / rondas_totales for equipo, datos in acum.items()}