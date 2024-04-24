from matricesRalas import *
import numpy as np

def main():
    # ##probando con listas enlazadas
    # # Crear una lista enlazada
    # lista = ListaEnlazada()

    # # Insertar elementos
    # lista.insertarFrente(1)
    # lista.push(2)
    # lista.push(3)
    # lista.push(4)
    # lista.insertarDespuesDeNodo(5, lista.nodoPorCondicion(lambda n: n.valor == 3))

    # # Imprimir la lista
    # print("Lista original:", lista)

    # # Eliminar el último elemento
    # lista.pop()
    # print("Lista después de eliminar el último elemento:", lista)

    # # Iterar sobre la lista
    # print("Elementos de la lista:")
    # for elemento in lista:
    #     print(elemento)
        
    # ##ejercicio 1
    # #crear matriz
    # A = MatrizRala(3, 3)
    # print("Matriz incial:")
    # print(A)
    
    # #get item 
    # c = A[0,1]
    # print(f"Get item matriz: {c}")
    
    # A[1, 2] = 2
    # c = A[1,2]
    # print(f"Get item con otro valor que no sea 0: {c}")
    
    # #set item
    # A[0, 0] = 1
    # A[2, 1] = 3
    
    # print("Set items en matriz:")
    # print(A)
    
    # #multiplicar por escalar
    # escalar = 3
    # B = A * escalar
    # print("Multiplicar por un escalar 1:")
    # print(B)
    
    # B = escalar * A
    # print("Multiplicar por un escalar 2:")
    # print(B)
    
    # #suma
    # C = MatrizRala(3, 3)
    # C[0,0]=1
    # C[1,1] = 2
    # C[2,2]= 0
    # C[2,1] = 10
    # C[2,2] =5
    # D = C + A
    # print("Suma dos matrices")
    # print(f"{A} + {C} = {D}" )
    
    # #resta
    # F = MatrizRala(2, 2)
    # F[0,0] = 1
    # F[1,1] = 2
    
    # G = MatrizRala(2,2)
    # G[0,0] = 2
    # G[0,1] = 1
    # G[1,0] = 4
    
    # #multiplicacion o resta de matrices
    # H = F * G
    # print(H)
    
    # D = MatrizRala(2,2)
    # D[0,0] = 1
    # D[0,1] = 2
    # D.mod_fila_entera(0,[2,4])
    # print(D)
    
    # #ejercicio 2
    # A = MatrizRala(3,3)
    # A[1,1] = 1
    # A[1,0] = 1
    # A[0,1] = 2
    # A[0,0] = 1
    # A[1,3] = 2
    # A[2,0] = 4
    # A[2,2] = 3
    # A[2,1] = 5
    # b = MatrizRala(3,1)
    # b[0,0] = 3
    # x = GaussJordan(A,b)
    # print(x)
    
    #W ∈ RN×N tal que Wij = 1 si pj cita a pi y Wij = 0 sino. A la matriz diagonal D ∈ RN×N condii = 1 /ci
   #Y siendo 1 el vector de RN de todos unos.
   
    #ejercicio 3 con numpy
    filas = [0,0,0,1,4,5,5,6,6,6,7,8,9]
    columnas = [2,3,4,0,10,6,0,7,8,0,9,5,8]
    #[A,B,C,D,E,F,G,H,I,J,K]
    #[0,1,2,3,4,5,6,7,8,9,10]
    # W ij = 1 , si pj cita a pi i: el citado j: el que cita 
    # [ac][ad][ae] [ba] [ek] [fg, fa] [gh,gi,ga] [hi] [if] [ji]
    # [0,0,0,1,4,5,5,6,6,6,7,8,9]
    # [2,3,4,0,10,6,0,7,8,0,9,5,8]
    # a es citado por c,d,e
    # b es citado por a
    # e es citado por k
    # f es citado po g,a
    # g es citado por h,i,a
    # h es citado por i
    # i es citado por f
    # j es citado por i
    #cj es la cantidad de trabajos citados por el paper pj
    W = np.zeros((11, 11))
    W[filas,columnas] = 1
    print(f"W:{W}")
    
    
    D = np.zeros((11, 11))
    for i in range(len(W)):
        cantidad_1s = np.sum(W[i, : ] == 1)
        if cantidad_1s != 0:
            D[i,i] = round((1/cantidad_1s),2)
    print(f"D:{D}")
    
    #p* = (1-d)(I)/N + (d)WDp*
    #p*: vector de probabilidades
    #N: tamaño de la matriz = cantidad de filas 
    #d = probabilidad aleatoria de continuar leyendo alguno de los trabajos citados 
    #W =  matriz qu eindic acual paper cito a otro 
    #D = matriz que en la diagonal indica la 1/cantidad de veces que ese paper fue citado
    #I: matri de unos con R^n
    #reordenado
    #A = (I - dWD)
    #x = p*
    #b = (1-d)I/N
    
    d = 0.85
    N = W.shape[0]
    I = np.ones((N,1))

    A = I - (d*(np.dot(W,D)))
    print(A)
    
    b = ((1-d)/N)*I
    
    p_star = np.linalg.solve(A,b)
    print(p_star)
    
    
    
    
    
    
    
    
    
    
    
    

if __name__ == "__main__":
    main()
