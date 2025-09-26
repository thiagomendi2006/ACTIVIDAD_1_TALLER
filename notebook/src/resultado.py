"""
Funciones para ordenar y mostrar los resultados en forma de tabla.
"""

def ordenar_por_puntos(acum: dict)  -> list[tuple[str, dict]]:

#devuelve una lista de equipos ordenados por "total" descendente
    return sorted(acum.items(), key=lambda x: x[1]["total"], reverse=True)
    
def mostrar_tabla(acum: dict, ronda_nro: int, mejor: tuple[str,int]) -> None:

#Imprime la tabla con innovacion, presentacion,errores,mejores y puntos totales.
#Resalta el mejor equipo de esa ronda
    print(f"\nRonda {ronda_nro}")
    print(f"Mejor Equipo de la Ronda: {mejor}\n")
    print("Ranking Actualizado\n")

    print(f"{'Equipo':<10}{'Innovacion':<12}{'Presentacion':<14}"
          f"{'Errores':<8}{'Mejores Equipos':<16}{'Puntos Total':<12}")
    print("-"*70)

    ranking = ordenar_por_puntos(acum)
    for equipo, datos in ranking:
        print(f"{equipo:<10}{datos['innovacion']:<12}{datos['presentacion']:<14}"
              f"{datos['errores']:<8}{datos['mejores']:<16}{datos['total']:<12}")
