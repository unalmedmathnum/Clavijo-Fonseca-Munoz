#Importamos las librerías necesarias.
import numpy as np

#Declaramos la función que aproximará el valor propio dominante y su correspondiente vector propio.

def Power_method(matriz:np.array, vector:np.array, tolerance:float, max_number_iter:int):
    #La función tomará como parámetros una matriz nxn, un vector n, una tolerancia y un número máximo de iteraciones.
    k : int = 1 #Iniciamos un contador para saber el número de iteraciones que van hasta ese momento.
    p : int = np.linalg.norm(vector, np.inf) #Calculamos la norma infinito del vector.
    vector : np.array = vector / p  #Se divide cada valor del vector por la norma p y se toman como los nuevos valores del vector.
    while k <= max_number_iter: #Se hacen las N iteraciones que se hayan declarado.
        y : np.array = matriz.dot(vector) #Se multiplica la matriz por el vector correspondiente a esa iteración y se asigna ese
                                          #nuevo vector a la variable y.
        u : np.array = np.linalg.norm(y, np.inf) #A continuación, calculamos la norma infinito de ese nuevo vector para cada iteración.
        if u == 0:
            #Si la norma infinito de ese vector es cero, se retorna lo siguiente:
            return (f"Vector propio {vector}"
                    f" La matriz {matriz} tiene valor propio 0, seleccione un nuevo vector propio vector x y reinicie la ejecución ")

        new_vector : np.array = vector - (y/u)
        #Declaramos un nuevo vector correspondiente al vector del error entre la iteración anterior y la que se está ejecutando.
        Err : np.array = np.linalg.norm(new_vector, np.inf) #Calculamos la norma infinito de este nuevo vector.
        vector : np.array = y / u #Reemplazamos el valor de la iteración anterior por los valores de la nueva iteración.
        if Err < tolerance: #Si el error es menor a la tolerancia, retornamos el valor y vector propio dominantes.
            return u, vector
        k += 1 #Se incrementa el contador por cada iteración.
    #Si el error no es menor que la tolerancia al cabo de las N iteraciones, se retorna lo siguiente:
    return f"El número máximo de iteraciones se ha excedido"
