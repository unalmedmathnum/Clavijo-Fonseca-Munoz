import math
import numpy as np
from sympy import Matrix, symbols, diff

def f(A):
    # Convertimos la lista a un array de NumPy
    A = np.array(A)

    # Validamos si la matriz es cuadrada
    if A.shape[0] != A.shape[1]:
        raise ValueError("La matriz debe ser cuadrada para calcular el polinomio característico.")

    # Convertimos el array a una matriz de SymPy para usar métodos algebraicos
    A_sympy = Matrix(A)

    # Declaramos el símbolo lambda para el polinomio característico
    lambd = symbols('λ')

    # Calculamos el polinomio característico
    polinomio = A_sympy.charpoly(lambd).as_expr()

    return polinomio

def fdx(polinomio):
    # Declaramos el símbolo lambda para el polinomio característico
    lambd = symbols('λ')
    # Calculamos la derivada del polinomio
    derivada = diff(polinomio, lambd)

    return derivada


# función para evaluar un punto en el polinomio característico
def f_evaluada(polinomio, punto):
  # Declaramos el símbolo lambda para el polinomio característico
    lambd = symbols('λ')
  # Se retorna el valor del polinomio
    return polinomio.subs(lambd, punto)

# función para evaluar un punto en la derivada del polinomio característico
def fdx_evaluada(polinomio, punto):
  # Declaramos el símbolo lambda para el polinomio característico
    lambd = symbols('λ')
  # Se retorna el valor de la derivada del polinomio
    return fdx(polinomio).subs(lambd, punto)

# función que aproximará el valor propio, dado un un punto inicial
def Newton_method(polinomio, p_0: float, tolerancia: float = 0.001, max_number_iter:int = 10):
    i : int = 1 # Se inicia un contador para saber el número de iteraciones

    while i <= max_number_iter: # Se hacen las N iteraciones que se hayan declarado

        p = float(p_0 - f_evaluada(polinomio,p_0)/fdx_evaluada(polinomio,p_0)) # Se aproxima el valor de la nueva iteración
        if abs(p-p_0)<tolerancia: # Se verifica si la diferencia entre la nueva iteriacion y la anterior es menor a la tolerancia declarada
            return p # Si esto ocurre, se retorna el valor de la iteracion

        i += 1  #Se incrementa el contador por cada iteración
        p_0 = p # Se actualiza el valor de la iteración anterior, con el valor de la nueva iteración

    # Si el error no es menor que la tolerancia al cabo de las N, se retorna lo siguiente.
    return f"El método falló después de las {max_number_iter}"
