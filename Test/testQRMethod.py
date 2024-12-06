import sys
sys.path.insert(0, '..')

import numpy as np
import QR_met

#casos de prueba
test = {"A": np.array([[2, 1], [3, 4]]),
       "B": np.array([[3, 2], [3, 4]]),
       "C": np.array([[2, 3], [1, 4]]),
       "D": np.array([[1, 1, 2], [2, 1, 1],[1, 1, 3]]),
       "E": np.array([[1, 1, 2], [2, 1, 3],[1, 1, 1]]),
       "F": np.array([[2, 1, 2], [1, 1, 3],[1, 1, 1]]),
       "G": np.array([[1, 1, 1, 2], [2, 1, 1, 1],[3, 2, 1, 2],[2, 1, 1, 4]]),
        "H": np.array([[1, 2, 1, 2], [2, 1, 1, 1],[3, 2, 1, 2],[2, 1, 1, 4]])}

for nombre, matriz in test.items(): #Creamos un ciclo que recorre el diccionario y va probando cada caso
  print(f"Los valores propios de la matriz {nombre} son:")
  print(QR_met.QRDecomposition(matriz)) #Utilizamos la funcion QRDecomposition e imprimimos cada valor propio
  print()
