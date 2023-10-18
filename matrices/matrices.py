import numpy as np
misArrays = np.array(([1,2,3],[4,5,6]))
#print(misArrays)
#ejemplo 3
#print(misArrays[1,2])
#ejemplo 4 matriz 4x5 que sus elementos son cero
"""arrayCeros = np.zeros((4,5))
print(arrayCeros)"""

#ej 5 matriz cualquier orden y todos sus elementos unos
"""arrayUnos = np.ones((4,4))
print(arrayUnos)"""

#ej 6  matriz cualquier orden y sus elementos son random
"""arrayRandom = np.random.random((4,6))
print(arrayRandom)"""

#ej7 una matriz de cualquier orden y todos sus elementos sean igual a 7
"""iguales = np.full((3,3),7)
print(iguales)"""
#ej8 una matriz que empiece en 5 y vaya hasta 200 en saltos de a 10
#sintaxis de arange np.arange(inicio,fin,salto)
"""saltando = np.arange(5,200,10)
print(saltando)"""
#ej9 np.linspace(inicio, fin, n) : Crea y devuelve una referencia a un array de una dimensión cuyos elementos son la secuencia de n valores equidistantes desde inicio hasta fin.
"""matriz = np.linspace(0,2,5)
print(matriz) tira los numeros entre 0 y 2 con saltos de a 5"""

#ej10 matriz identidad 
"""identidad = np.eye(4,4)
print(identidad)"""
#ej11 presentar una matriz identidad en pantalla y su dimension
"""identidad = np.eye(2,3)
print(identidad.ndim) tira la dimension no el orden"""
#ej12 presentar una matriz 4x4 y tirar su tamano y forma
"""matriz = np.eye(4,4)
print(matriz)
print(matriz.size)  #   filas
print(matriz.shape) #   columnas
"""
#ej14 imprimir una matriz y mostrar los elementos de su primera columnna 
"""A = np.array(([5,6,7],[8,9,10],[11,15,13],[14,15,16]))
print(A[:,2])"""
#eje 15 Dada la matriz A presente en pantalla el mayor, el menor y la suma de todos sus elementos
"""A = np.array(([5,6,7],[8,9,10],[11,15,13],[14,15,16]))
print(A.max())
print(A.min())
print(A.sum())"""