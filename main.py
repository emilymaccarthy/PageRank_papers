from matricesRalas import ListaEnlazada, MatrizRala

def main():
    ##probando con listas enlazadas
    # Crear una lista enlazada
    lista = ListaEnlazada()

    # Insertar elementos
    lista.insertarFrente(1)
    lista.push(2)
    lista.push(3)
    lista.push(4)
    lista.insertarDespuesDeNodo(5, lista.nodoPorCondicion(lambda n: n.valor == 3))

    # Imprimir la lista
    print("Lista original:", lista)

    # Eliminar el último elemento
    lista.pop()
    print("Lista después de eliminar el último elemento:", lista)

    # Iterar sobre la lista
    print("Elementos de la lista:")
    for elemento in lista:
        print(elemento)
        
    ##ejercicio 1
    #crear matriz
    A = MatrizRala(3, 3)
    print("Matriz incial:")
    print(A)
    
    #get item 
    c = A[0,1]
    print(f"Get item matriz: {c}")
    
    A[1, 2] = 2
    c = A[1,2]
    print(f"Get item con otro valor que no sea 0: {c}")
    
    #set item
    A[0, 0] = 1
    A[2, 1] = 3
    
    print("Set items en matriz:")
    print(A)
    
    #multiplicar por escalar
    escalar = 3
    B = A * escalar
    print("Multiplicar por un escalar 1:")
    print(B)
    
    B = escalar * A
    print("Multiplicar por un escalar 2:")
    print(B)
    
    #suma
    C = MatrizRala(3, 3)
    C[0,0]=1
    C[1,1] = 2
    C[2,2]= 0
    C[2,1] = 10
    C[2,2] =5
    D = C + A
    print("Suma dos matrices")
    print(f"{A} + {C} = {D}" )
    
    #resta
    F = MatrizRala(2, 2)
    F[0,0] = 1
    F[1,1] = 2
    
    G = MatrizRala(2,2)
    G[0,0] = 2
    G[0,1] = 1
    G[1,0] = 4
    
    #multiplicacion o resta de matrices
    H = F * G
    print(H)
    
    
    
    
    
    

if __name__ == "__main__":
    main()
