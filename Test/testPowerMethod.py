import sys
sys.path.insert(0, '..')

import numpy as np
import Power_met

# Declaramos los vectores correspondientes para los casos de prueba.
vector = np.array([1, 1]) #Dimensión 2.
vector1 = np.array([1, 2, 0]) #Dimensión 3.
vector2 = np.array([1, 1, 1, 1]) #Dimensión 4.

#Casos de prueba: declaramos un diccionario con las matrices de prueba.

test = {"A": np.array([[2, 1], [3, 4]]),
       "B": np.array([[3, 2], [3, 4]]),
       "C": np.array([[2, 3], [1, 4]]),
       "D": np.array([[1, 1, 2], [2, 1, 1],[1, 1, 3]]),
       "E": np.array([[1, 1, 2], [2, 1, 3],[1, 1, 1]]),
       "F": np.array([[2, 1, 2], [1, 1, 3],[1, 1, 1]]),
       "G": np.array([[1, 1, 1, 2], [2, 1, 1, 1],[3, 2, 1, 2],[2, 1, 1, 4]]),
        "H": np.array([[1, 2, 1, 2], [2, 1, 1, 1],[3, 2, 1, 2],[2, 1, 1, 4]])}

for name, matriz in test.items(): # Iteramos sobre el diccionario con su respectiva clave y valor.
    dimension : int = matriz.shape[0] # Obtenemos la dimensión de cada matriz del diccionario.
    if dimension == 2: # Matrices de dimensión 2.
        print(# Retornamos el correspondiente valor dominante a cada matriz, con su vector propio.
            f"El valor propio dominante asociado a la matriz {name} es: {Power_met.Power_method(matriz, vector, tolerance=1e-5, max_number_iter=10)[0]}"
              f" y su vector propio asociado es: {Power_met.Power_method(matriz, vector, tolerance=1e-5, max_number_iter=10)[-1]}")
    if dimension == 3: # Matrices de dimensión 3.
        print( # Retornamos el correspondiente valor dominante a cada matriz, con su vector propio.
            f"El valor propio dominante asociado a la matriz {name} es: {Power_met.Power_method(matriz, vector1, tolerance=1e-12, max_number_iter=20)[0]}"
            f" y su vector propio asociado es: {Power_met.Power_method(matriz, vector1, tolerance=1e-10, max_number_iter=20)[-1]}")
    if dimension == 4: # Matrices de dimensión 4.
        print( # Retornamos el correspondiente valor dominante a cada matriz, con su vector propio.
            f"El valor propio dominante asociado a la matriz {name} es: {Power_met.Power_method(matriz,vector2 , tolerance=1e-5, max_number_iter=10)[0]}"
            f" y su vector propio asociado es: {Power_met.Power_method(matriz, vector2, tolerance=1e-5, max_number_iter=10)[-1]}")
