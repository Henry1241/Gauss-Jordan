import numpy as np
from fractions import Fraction

def jordan(x1,x2,x3,y1,y2,y3,z1,z2,z3,X,Y,Z):

    A = np.array([[x1,x2,x3],
              [y1,y2,y3],
              [z1,z2,z3]])

    B = np.array([[X],
              [Y],
              [Z]])

    #Procedimiento
    casicero = 1e-15 # Considerar como 0

    # Evitar truncamiento en operaciones
    A = np.array(A,dtype=float) 

    # Matriz aumentada
    AB = np.concatenate((A,B),axis=1) #Concatena A & B para que la matriz este ordenada correctamente
    AB0 = np.copy(AB) #Copia el valor de A & B para usarlos

    # Pivoteo parcial por filas
    tamano = np.shape(AB) #Identifica la forma de la matriz de AB
    n = tamano[0] #Se usa para definir el tamaño de la fila
    m = tamano[1] #Se usa para definir el tamaño de la columna

    #Para cada fila
    for i in range (0, n - 1, 1):
    #Columna desde i en adelante
        columna = abs(AB[i:,i]) #Define el valor de la columna que debe usar al moverse por cada fila
        max = np.argmax(columna) #Define el valor maximo de la columna definida anteriormente

    #Si max no esta en diagonal
    if (max !=0):
        # intercambia filas
        temporal = np.copy(AB[i,:])
        AB[i,:] = AB[max+i,:]
        AB[max+i,:] = temporal
        
    AB1 = np.copy(AB) #Copia el resultado del pivoteo parcial por filas

    #Eliminación hacia adelante
    for i in range (0, n - 1, 1): #Usa el rango definido para realizar la eliminación hacia atras
        pivote = AB[i,i]
        adelante = i + 1
        for k in range(adelante, n, 1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:] * factor
    AB2 = np.copy(AB)

    #Eliminación hacia atras
    ultfila = n - 1
    ultcolumna = m - 1
    for i in range(ultfila,0-1,-1):
        pivote = AB[i,i]
        atras = i-1 
        resultados = []
        for k in range(atras,0-1,-1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
        # diagonal a unos
        AB[i,:] = AB[i,:]/AB[i,i]
    X = np.copy(AB[:,ultcolumna])
    X = np.transpose([X])
    resultados +=[
    ('x', '=', ((Fraction(AB[:,3][i])))),
    ('y', '=', ((Fraction(AB[:,3][i+1])))),
    ('z',  '=', ((Fraction(AB[:,3][i+2]))))]
    print(resultados[0])
    return resultados

#print('Matriz aumentada: ')
#print(AB0)
#print('Pivoteo parcial por filas')
#print(AB1)
#print('Eliminaición hacia adelante:')
#print(AB2)
#print('Eliminación hacia atras:')
#print(AB)
#print('solución de X: ')
#print((X))