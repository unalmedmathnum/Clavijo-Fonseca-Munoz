import numpy as np #importamos la librería numpy que utilizaremos para trabajar con matrices

#La siguiente función toma como parámetros una Lista de tamaño nxn, un número máximo de iteraciones opcional,
#que por defecto será 100, y una tolerancia numérica, también opcional
def QRDecomposition(A, maxIteraciones = 1000, tol = 1e-10):
    A_n = np.array(A) #Convertimos la lista en un array de numpy para operar con el fácilmente

    for i in range(maxIteraciones): #Comenzamos a iterar el método

        #Cuando i es par:
        if i%2 == 0:
            Q_n,R_n = np.linalg.qr(A_n) #Descomposición QR de la matriz usando la función integrada de numpy

        #Cuando i es impar
        if i%2 == 1:
            A_n = R_n@Q_n

    """Sabemos que en este método los valores que convergen a los valores propios están ubicados
     sobre la diagonal de la matriz A_n, entonces vamos a recorrer esa diagonal y guardarlos en una lista"""

    valoresPropios = [] #Creamos la lista
    for i in range(A_n.shape[0]): #.shape[0] es para contar el número de filas, el cual será igual al numero de valores en la diagonal
                                  #dado que la matriz es cuadrada
        valoresPropios.append(A_n[i,i]) #Ingresamos los valores con índice [i,i] en la diagonal

    return valoresPropios
