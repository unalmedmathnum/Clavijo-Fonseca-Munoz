import sys
sys.path.insert(0, '..')
import numpy as np
import polynomial_met
from polynomial_met import f


#Casos de prueba: declaramos un diccionario con las matrices de prueba.
def testPolynomialMethod():
    test = {"A": np.array([[2, 1], [3, 4]]),
       "B": np.array([[3, 2], [3, 4]]),
       "C": np.array([[2, 3], [1, 4]]),
       "D": np.array([[1, 1, 2], [2, 1, 1],[1, 1, 3]]),
       "E": np.array([[1, 1, 2], [2, 1, 3],[1, 1, 1]]),
       "F": np.array([[2, 1, 2], [1, 1, 3],[1, 1, 1]]),
       "G": np.array([[1, 1, 1, 2], [2, 1, 1, 1],[3, 2, 1, 2],[2, 1, 1, 4]]),
        "H": np.array([[1, 2, 1, 2], [2, 1, 1, 1],[3, 2, 1, 2],[2, 1, 1, 4]])}
    
    valor_inicial = 0
    for name, matriz in test.items(): # iteramos sobre el diccionario con su respectiva clave y valor.
        #Utilizamos el metodo de Newton e imprimimos cada valor propio, correspondiente al valor inicial que se la haya pasado como parámetro.
        print(f"La matriz {name} tiene el siguiente valor propio: {polynomial_met.Newton_method(f(matriz),valor_inicial)} correspondiente al valor inicial {valor_inicial} ")
        valor_inicial += 1

if __name__ == "__main__":
    testPolynomialMethod()