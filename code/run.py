# Search methods

import search

ab = search.GPSProblem('M', 'F'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
print(search.depth_first_graph_search2(ab).path())
print(search.depth_first_graph_search3(ab).path())
# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
# No es lo mismo la información que la heurística, método informado es el que usa la heurística.
# Como podemos hacer que el algoritmo vea el camino como nosotros, añadiremos como heurística la distancia
# en linea recta entre ciudades.  El orden será Path_cost + heurística, véase + la distancia en linea recta. El coste no
# forma parte de lo que llamamos heurística.
#
# Ramificación y acotación con subestimación (siempre un valor menor o igual que el valor real), en este caso la
# distancia solo puede ser menor o igual, por lo tanto está bien.
#
# Si no fuera una subestimación, no exploaría por ahi, sería un valor mucho más por encima del valor real. Corremos el
# riesgo de que no nos vaya por el mejor camino.
