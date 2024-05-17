# IMPORTANTE: Para importar estas clases en otro archivo (que se encuentre en la misma carpeta), escribir:
# from matricesRalas import MatrizRala, GaussJordan 
import numpy as np
import csv 

class ListaEnlazada:
    
    def __init__( self ):
        """Inicializa una lista enlazada
        """
        self.raiz = None
        self.longitud = 0
        
        self.current = self.Nodo(None, self.raiz)

    def insertarFrente( self, valor ):
        
        # Inserta un elemento al inicio de la lista
        if len(self) == 0:
            return self.push(valor)    
    
        nuevoNodo = self.Nodo( valor, self.raiz )
        self.raiz = nuevoNodo
        self.longitud += 1

        return self

    def insertarDespuesDeNodo( self, valor, nodoAnterior ):
        # Inserta un elemento tras el nodo "nodoAnterior"
        nuevoNodo = self.Nodo( valor, nodoAnterior.siguiente)
        nodoAnterior.siguiente = nuevoNodo

        self.longitud += 1
        return self

    def insertarAntesDeNodo( self, valor, nodoPosterior, nodoActual ):
        # Inserta un elemento detras el nodo "nodoactual"
        if nodoPosterior == None:
            self.insertarFrente(valor)
        
        else:
            nuevoNodo = self.Nodo( valor, nodoActual)
            nodoPosterior.siguiente = nuevoNodo
            self.longitud += 1
        return self

    def push( self, valor ):
        # Inserta un elemento al final de la lista
        if self.longitud == 0:
            self.raiz = self.Nodo( valor, None )
        else:      
            nuevoNodo = self.Nodo( valor, None )
            ultimoNodo = self.nodoPorCondicion( lambda n: n.siguiente is None )
            ultimoNodo.siguiente = nuevoNodo

        self.longitud += 1
        return self
    
    def pop( self ):
        # Elimina el ultimo elemento de la lista
        if len(self) == 0:
            raise ValueError("La lista esta vacia")
        elif len(self) == 1:
            self.raiz = None
        else:
            anteUltimoNodo = self.nodoPorCondicion( lambda n: n.siguiente.siguiente is None )
            anteUltimoNodo.siguiente = None
        
        self.longitud -= 1

        return self

    def nodoPorCondicion( self, funcionCondicion ):
        # Devuelve el primer nodo que satisface la funcion "funcionCondicion"
        if self.longitud == 0:
            raise IndexError('No hay nodos en la lista')
        
        nodoActual = self.raiz
        while not funcionCondicion( nodoActual ):
            nodoActual = nodoActual.siguiente
            if nodoActual is None:
                raise ValueError('Ningun nodo en la lista satisface la condicion')
            
        return nodoActual
        
    def setValue( self, valor, columna ):
        if self.longitud == 0:
            self.raiz = self.Nodo( (columna,valor), None )
            self.longitud += 1
        else:
            currentNode = self.raiz
            while currentNode and currentNode.valor[0] < columna:
                currentNode = currentNode.siguiente
            # Currentnode.coluna es <= indice
            sig_node = currentNode.siguiente
            currentNode.siguiente = self.Nodo((columna,valor),sig_node)
            self.longitud += 1 

    def __len__( self ):
        return self.longitud

    def __iter__( self ):
        self.current = self.Nodo( None, self.raiz )
        return self

    def __next__( self ):
        if self.current.siguiente is None:
            raise StopIteration
        else:
            self.current = self.current.siguiente
            return self.current.valor
    
    def __repr__( self ):
        res = 'ListaEnlazada([ '

        for valor in self:
            res += str(valor) + ' '

        res += '])'

        return res

    class Nodo:
        def __init__( self, valor, siguiente ):
            #valor es una tupla que (c,n) : c = numero de columna y n= numero de la matriz en la posici´on f, c.
            self.valor = valor
            self.siguiente = siguiente


class MatrizRala:

    def __init__( self, M, N ):
        self.filas = {}
        self.shape = (M, N)

    def __getitem__( self, Idx ):
        # Esta funcion implementa la indexacion ( Idx es una tupla (m,n) ) -> A[m,n]
        # se indexa a traves de un diccionario la clave de cada fila es su ´ındice y el valor almacenado es la lista enlazada.
        
        # tupla dada por la funcion m= filas y n = columnas
        m,n = Idx

        if m >= self.shape[0] or n >= self.shape[1]:
            raise IndexError('Index fuera de rango')

        #si la fila pasada por parametro existe en el diccionario
        if m in self.filas:
            #obtenemos la lista enlazada para esa fila
            fila = self.filas[m]
            #ponemos un nodo en la raiz de esta fila y recorremos columnas
            nodo = fila.raiz
            #recorremos la lista enlazada hatsa el final 
            while nodo is not None:
                #entramos en la tupla que es una valor (c,n): c=columna y n=valor de la matriz rala 
                if nodo.valor[0] == n:
                    return nodo.valor[1]
                #avanzamos en la lista 
                nodo = nodo.siguiente
        #0 es que el elemento no esta presente en la matrix
        return 0
    
    def __setitem__( self, Idx, v ):
        
        # Esta funcion implementa la asignacion durante indexacion ( Idx es una tupla (m,n) ) -> A[m,n] = v
        m,n = Idx
        
        if m >= self.shape[0] or n >= self.shape[1]:
            raise IndexError('Index fuera de rango')
        
        # si la fila no esta existe
        if m not in self.filas:
            self.filas[m] = ListaEnlazada()
            self.filas[m].push((n,v))
            return
        
        
        fila = self.filas[m]
        nodo_actual = fila.raiz
        nodo_anterior = None
        
        while nodo_actual is not None:
            #si ya existita un (m,n) lo updeteamos 
            if nodo_actual.valor[0] == n:
                nodo_actual.valor = (n,v)
                return 
          
            # recorri la lista y ya me pasee del valor de columna entonces tengo que meter el nodo atras del nodo actual
            elif nodo_actual.valor[0] > n:
                #inserto un nuevo nodo con siguietne nodo acctua
                fila.insertarAntesDeNodo((n,v),nodo_anterior, nodo_actual)
                return 
            
            #avanzar en la lista
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
        
        #si el numero de columna mas grande es mas chico que el  numero de columna que yo busco entonces uso push
        self.filas[m].push((n,v))
        
                            
    def __mul__( self, k ):
        
        # Esta funcion implementa el producto matriz-escalar -> A * k
        
        resultado = MatrizRala(self.shape[0],self.shape[1])
        #recorro todas las filas y todas las columnas 
        for i in self.filas:
            fila = self.filas[i]
            nodo = fila.raiz
            while nodo is not None:
                if nodo.valor[1] != 0:
                    res = nodo.valor[1] * k
                    col = nodo.valor[0]
                    resultado[i,col] = res
                
                nodo = nodo.siguiente
                
        return resultado
      
    def __rmul__( self, k ):
        # Esta funcion implementa el producto escalar-matriz -> k * A
        return self * k

    def __add__( self, other):
        # Esta funcion implementa la suma de matrices -> A + B
        
        if self.shape[0] != other.shape[0]:
            raise ValueError("los tamaños no son iguales")
        
        resultado = MatrizRala(self.shape[0],self.shape[1])
        # para cada fila ver que onda para cuando es nxn - nx1
        #if other.shape[1] == 1:
            # for i in range(self.shape[0]):
            #     for j in range(self.shape[1]):
            #         suma = self[i,j] + other[i,1]
            #         if suma != 0:
            #             resultado[i,j] = suma
   
        for i in range(self.shape[0]):
            #para cada columna
            for j in range(self.shape[1]):
                #sumar la posiciones
                suma = self[i, j] + other[i, j]
                if suma != 0:
                    resultado[i, j] = suma
        return resultado
   
    def __sub__( self, other ):
        # Esta funcion implementa la resta de matrices (pueden usar suma y producto) -> A - B
        
        if self.shape != other.shape:
            raise ValueError("los tamaños de las filas no son iguales")
        
        resultado = MatrizRala(self.shape[0],self.shape[1])
        B = other.__rmul__(-1)
        resultado = self.__add__(B)
        
        return resultado

    def __repr__( self ):
        res = 'MatrizRala([ \n'
        for i in range( self.shape[0] ):
            res += '    [ '
            for j in range( self.shape[1] ):
                res += str(self[i,j]) + '  '
            
            res += ']\n'

        res += '])'

        return res

    # def __matmul__( self, other ):

    #     if self.shape[1] != other.shape[0]:
    #         raise ValueError("Matrices no compatibles")
    #     resultado = MatrizRala(self.shape[0],other.shape[1])
    #     other_t = other.t()
    #     # print("Ya hice la transouesta")
    #     cantFilas = len(self.filas)
    #     cont_i = 0
    #     for i in self.filas:
    #         cont_i +=1
    #         print(f"\r Progreso: {(cont_i/cantFilas)*100}%",end="")
    #         filaA:ListaEnlazada = self.filas[i]
    #         for j in other_t.filas:
    #             colB:ListaEnlazada = other_t.filas[j]
    #             pi = MatrizRala.productoInterno(filaA,colB)
    #             if pi != 0:
    #                 resultado[i,j] = pi
    #     return resultado
    

    def __matmul__( self, other ):
        # Esta funcion implementa el producto matricial (notado en Python con el operador "@" ) -> A @ B
        
        if self.shape[1] != other.shape[0]:
            raise ValueError("los tamaños no se pueden multiplicar")
        
        resultado = MatrizRala(self.shape[0],other.shape[1])
        cantFilas = len(self.filas)
        cont_i = 0
        #para todas las filas de self 
        for current_i in self.filas: #valor de m
            cont_i += 1
            print(f"\r Progreso: {(cont_i/cantFilas)*100}%",end="")
            #agarro el raiz de la fila 
            fila = self.filas[current_i]
            if fila.raiz:
                rootNode_self = fila.raiz
                for j in range(other.shape[1]):
                    currentNode = rootNode_self
                    suma = 0
                    while currentNode is not None:
                        
                        current_j = currentNode.valor[0]
                        suma += currentNode.valor[1] * other[current_j,j]
                        currentNode = currentNode.siguiente

                    resultado[current_i,j] = suma
            # else:
            #     resultado[current_i,j] = 0


    
    def getD(self):
        resultado = MatrizRala(self.shape[0],self.shape[1])

        for i in self.filas:
            fila = self.filas[i]
            # nodo = fila.raiz

                
            if len(fila) != 0:
                resultado[i,i] = 1/len(fila)
            else:
                resultado[i,i] = 1
           
            
        return resultado
    
    def mul_daig(self,D):
        resultado = MatrizRala(self.shape[0], self.shape[1])
    
        for i in self.filas:
            current_row = ListaEnlazada()
            fila = self.filas[i]
            nodo = fila.raiz
            
            while nodo is not None:
              
                columna_curr = nodo.valor[0]
                res = nodo.valor[1] * D[columna_curr,columna_curr]
                current_row.push((columna_curr, res))
           
                    
                nodo = nodo.siguiente
            
            if current_row.raiz is not None:  
                resultado.filas[i] = current_row
        return resultado
    
    def mul_con_vec_col(self,b):
        if self.shape[1] !=  b.shape[0]:
            raise ValueError("nanana no son los tamaños bro, sabes multiplicar matrices")
        
        if b.shape[1] != 1:
            raise ValueError("bro esta no es la funcion para vos")
        
        resultado = MatrizRala(self.shape[0],1)
        
        for i in self.filas:
            res = 0
            fila = self.filas[i]
            nodo = fila.raiz
            while nodo is not None:
                res += nodo.valor[1] * b[i,0]
                nodo = nodo.siguiente
                
            resultado[i,0] = res
            
        return resultado 
        
    def __copy__(self):
        resultado = MatrizRala(self.shape[0],self.shape[1])
        for i in self.filas:
            
            fila = self.filas[i]
            nodo = fila.raiz
            #si hay algo en la lista
            if nodo is not None:
                
                #creo una lista enlazada 
                resultado.filas[i] = ListaEnlazada.Nodo(nodo.valor, None)  
                #guardo la posicion del nodo nuevo
                nuevo_nodo = resultado.filas[i]
                #voy al proximo elemento de la lista que estoy copiando
                nodo_actual = nodo.siguiente
                while nodo_actual is not None:
                    #el push agrega el valor del sigueinte nodo en la lista al final de la lista 
                    nuevo_nodo.push(nodo_actual.valor)  
                    #voy al siguiente nodo que se acaba de guarda
                    nuevo_nodo = nuevo_nodo.siguiente
                    #acanzo uno mas en la lissta og 
                    nodo_actual = nodo_actual.siguiente
        
                
        return resultado
  
    def return_fila_entera(self,numero_fila):
        nodo = None
        if numero_fila in self.filas:
            nodo = self.filas[numero_fila].raiz
        return nodo
    
    def sum(self):
        suma = 0
        for i in self.filas:
            # fila = self.filas[i]
            nodo = self.filas[i].raiz
            while nodo:
                suma += nodo.valor[1]
                nodo = nodo.siguiente
            # suma += self[i,0]
            # suma += fila.longitud

        return suma
    
    def inversa(self):
        if self.shape[0] != self.shape[1]:
            raise ValueError("la matriz no es cuadrada")
            
        identidad = MatrizRala.One(self.shape[0])
        resultado = MatrizRala(self.shape[0],self.shape[0])
            
        for i in range(self.shape[0]):
            for j in range(self.shape[0]):
                resultado[i,j] = self[i,j]
            
        for i in range(self.shape[0]):
            factor = 1.0 / self[i,i]
                
            for j in range(self.shape[0]):
                resultado[i,j] *= factor
                identidad[i,j] *= factor
                    
            for k in range(self.shape[0]):
                if k!=i:
                    factor = resultado[k,i]
                        
                    for j in range(self.shape[0]):
                        resultado[k,j] -= factor*resultado[i,j]
                        identidad[k,j] -= factor*identidad[i,j]
                            
        return identidad   

    def toNumpy(self):
        m,n = self.shape
        res = np.zeros((m,n))
        for i in self.filas:
            fila = self.filas[i]
            currentNode = fila.raiz
            while currentNode is not None:
                j = currentNode.valor[0]
                res[i,j] = currentNode.valor[1]
                currentNode = currentNode.siguiente
        return res

    @staticmethod
    def One(n:int):
        M = MatrizRala(n,n)
        for i in range(n):
            M[i,i] = 1
        return M
    
    @staticmethod
    def getW(paperPath:str,citasPath:str):
        #tengo que tener agarrar la primer columna entera de papers csv 
        #cada posicion me da el nuumero del paper = paper + 1
        #ahora tengo que linkear cada con citas csv para crear la matriz
        #pj cita a pi id1 cita a id2 => W{id2,id1} =  1
        #1. crear matriz rala con dimension numero max de citas.csv m y n el mismo numero
        #2. recorrer citas csv por cada row ponerle set item (id2,id1) v=1
        
        #despues seria sobre len(ids)
        N = 0 
        with open(paperPath,newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
              
            N = sum(1 for row in reader)
            csvfile.close()


        print(f"N: = {N}")
        W = MatrizRala(N,N)
        W_t = MatrizRala(N,N)

        with open(citasPath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) #skipping the header
            # print("HOLA")
            for row in reader:
                # print(row)
                # print("1")
                #ai existe el 0
                to_ = int(row[1])
                from_ = int(row[0])
                #print(f" from_ = {from_}, to_ = {to_}")
                # pass
                W[to_,from_] = 1
                W_t[from_,to_]=1
            csvfile.close()

                
        return W, W_t

    @staticmethod
    def getVectorOne(n):
        unos = MatrizRala(n,1)

        for i in range(n):
            unos[i,0] = 1

        return unos
    
    @staticmethod
    def diffVectors(v1,v2):
        """Agarra dos matricesRalas que son de 1 columna y compara su diferencia absoluta 
        por cada posicion y suma todas las diferencias

        Args:
            A (MatrizRala): Matriz de nx1
            B (MatrizRala): matriz de nx1

        Raises:
            ValueError: si las matrices no tienen la misma cantidad de filas

        Returns:
            int: Devuelve la sumatoria de las diferencias posicion a posicion
        """
        # Verificar que los vectores tengan la misma longitud
        if v1.shape[0] != v2.shape[0]:
            raise ValueError("Los vectores deben tener la misma longitud.")
        
        # Calcular la norma L1 de la diferencia entre los vectores
        dif = 0
        for i in v1.filas:
            diferencia_absoluta = abs(v1[1,0]-v1[1,0])
            dif += diferencia_absoluta
            
            
        # for i in range(v1.shape[0]):
        #     diferencia_absoluta = abs(v1[i,0] - v2[i,0])
        #     dif += diferencia_absoluta
        
        return dif

    @staticmethod
    def fromNumpy(A):
        m,n = A.shape
        res = MatrizRala(m,n)
        for i in range(m):
            for j in range(n):
                res[i,j] = A[i,j]
        return res
    

#ejercicio 2    
def GaussJordan( A, b ):
    # Hallar solucion x para el sistema Ax = b
    # Devolver error si el sistema no tiene solucion o tiene infinitas soluciones, con el mensaje apropiado
    
    M, N = A.shape
    
    #Asegúrate de que b es del tamaño adecuado
    if M != b.shape[0]:
        raise ValueError("Las dimensiones de A y b no coinciden")
    
    #Si hay mas columnas que filas el sistema va a tener variables libres 
    if M < N:
        raise ValueError("El sistema tiene infinitas soluciones")
    
    #Si b no es una columna
    if b.shape[1] != 1:
        raise ValueError("b no es un vector columna")


#--------Crear la matriz extendida con A y b----------

    mat_aumentada = MatrizRala(M, N + 1)
    for i in range(M):
        for j in range(N):
            mat_aumentada[i, j] = A[i, j]
        mat_aumentada[i, N] = b[i,0]
   
    # print(mat_aumentada)
    
#---------------Eliminación por debajo --------------
    
    for i in range(M):
        pivot = mat_aumentada[i, i]
        
        if pivot == 0:
            raise ValueError("El sistema tiene infinitas soluciones")
            
        #para todas las filas debajo de i 
        for j in range(i+1, M):
        
            #agarro el elemento debajo del pivot
            factor = mat_aumentada[j,i]
            
            #si ya hay un cero debajo del 
            if factor == 0: 
                continue
            
            #para todas las columnas 
            for k in range(mat_aumentada.shape[1]):
                
                #para la fila debajo del pvito
                fila_debajo = mat_aumentada[j,k] * pivot 
                
                #la fila del pivot actual que estamos calculando 
                fila_pivot = mat_aumentada[i,k] * factor
                
                mat_aumentada.__setitem__((j,k),fila_debajo - fila_pivot)
         
     
    # print(mat_aumentada)   
    
#----------------------Eliminacion hacia arriba---------------

    for i in range(1,M):
        
        pivot = mat_aumentada[i, i]
        
        if pivot == 0:
            continue
    
        #para todas las filas sobre i 
        for j in range(i-1, -1, -1):
           
            #agarro el elemento arriba del pivot
            factor = mat_aumentada[j,i]
            
            #si ya hay un cero debajo del pivot no hago el for k 
            if factor == 0: 
                continue
            
            #para todas las columnas 
            for k in range(mat_aumentada.shape[1]):
                
                #para la fila debajo del pvito
                fila_debajo = mat_aumentada[j,k] * pivot 
                #la filadel pivot actual que estamos calculando 
                fila_pivot = mat_aumentada[i,k] * factor
                mat_aumentada.__setitem__((j,k),fila_debajo - fila_pivot)
    
    # print(mat_aumentada)
    
#-------------------------Chequeo si es inconsistente-----------------
    
    for i in range(M):
        
        contador0 = 0   
        
        for j in range(mat_aumentada.shape[1]):
            if mat_aumentada[i,j] == 0:
                contador0 += 1
                
        # print(mat_aumentada[i,mat_aumentada.shape[1]-1] )
        # print(contador0)
        # print(A.shape[0])
        
        if mat_aumentada[i,mat_aumentada.shape[1]-1] != 0 and contador0 == N:
            sol = "El sistema es incosistente, no tiene solucion"
            return sol
        
    # print(mat_aumentada)
    
#--------------------Hacer unos en los pivots-----------------
   
    
    for i in range(A.shape[0]):
        #para cada columnas agarrar el pivot como factor 
        factor = mat_aumentada[i,i]
        
        if factor != 0:
            for j in range(mat_aumentada.shape[1]):
                #si el elemento a dividirn es diferente de cero
                if mat_aumentada[i,j] != 0:
                    #cambio la fila entera
                    res = mat_aumentada[i,j]/factor
                    mat_aumentada.__setitem__((i,j),res)
                else:
                    mat_aumentada.__setitem__((i,j),0.0)
                    
    matriz_sol = MatrizRala(A.shape[0],1)  
    
    
#-----------Si tiene sol unica---------------

    for i in range(A.shape[0]):
        #en realidad es tipo todos deberian se runos pero weno
        valor = mat_aumentada[i,mat_aumentada.shape[1]-1]
        matriz_sol[i,0] = valor
    
    return matriz_sol    


def GaussVerification(A,b,x):
    # Verificar que x sea solución del sistema Ax = b
    # Devolver True si es solución, False si no lo es
    # Asegúrate de que x sea del tamaño adecuado
    if A.shape[1] != x.shape[0]:
        raise ValueError("Las dimensiones de A y x no coinciden")   
    # Asegúrate de que b sea del tamaño adecuado
    if A.shape[0] != b.shape[0]:
        raise ValueError("Las dimensiones de A y b no coinciden")
    # Asegúrate de que b sea un vector columna
    if b.shape[1] != 1:
        raise ValueError("b no es un vector columna")
    # Verificar que Ax = b
    Ax = A @ x
    for i in range(Ax.shape[0]):
        if Ax[i,0] != b[i,0]:
         return False
    return True

