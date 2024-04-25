# IMPORTANTE: Para importar estas clases en otro archivo (que se encuentre en la misma carpeta), escribir:
# from matricesRalas import MatrizRala, GaussJordan 
import numpy as np

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
        # si la fila no esta computada 
        if m not in self.filas:
            self.filas[m] = ListaEnlazada()
            
        fila = self.filas[m]
        nodo_actual = fila.raiz
        nodo_anterior = None
        
        while nodo_actual is not None:
            #si ya existita un (m,n) lo updeteamos 
            if nodo_actual.valor[0] == n:
                nodo_actual.valor = (n, v)
                return 
          
            #si recorro la lista y me paso en el valor de n ya tengo el nodo que va depsues del que tengo que crear
            elif nodo_actual.valor[0] > n:
                #creo un nuevo nodo que apunta al nodo actual
                nuevo_nodo = ListaEnlazada.Nodo((n,v), nodo_actual)
                #si estoy en el principio de la lista solo hago que el nuevo nodo sea la raiz y que apunte al acutal
                if nodo_anterior is None:
                    fila.raiz = nuevo_nodo
                #sino es el primero conecto el nodo anterior con el nuevo nodo
                else:
                    nodo_anterior.siguiente = nuevo_nodo
                return 
            
            #avanzar en la lista
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente
        #si no entre al while porque no hay lista para esa fila creo la raiz   
        if nodo_anterior is None:
            fila.raiz = ListaEnlazada.Nodo((n,v), None)
        #si entro al while pero el n es mayor que todos los nodos a encontrar
        else:
            nodo_anterior.siguiente = ListaEnlazada.Nodo((n,v), None)
                    
        
    def __mul__( self, k ):
        
        # Esta funcion implementa el producto matriz-escalar -> A * k
        
        resultado = MatrizRala(self.shape[0],self.shape[1])
        #recorro todas las filas y todas las columnas 
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                valor_actual = self[i, j]
                valor_producto = valor_actual * k

                if valor_producto != 0:
                    resultado[i, j] = valor_producto

        return resultado
    
    
    def __rmul__( self, k ):
        # Esta funcion implementa el producto escalar-matriz -> k * A
        return self * k

    def __add__( self, other ):
        # Esta funcion implementa la suma de matrices -> A + B
        
        if self.shape != other.shape:
            raise ValueError("los tamaños no son iguales")
        
        resultado = MatrizRala(self.shape[0],self.shape[1])
        # para cada fila
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
        
        if self.shape[0] != other.shape[0]:
            raise ValueError("los tamaños de las filas no son iguales")
        
        resultado = MatrizRala(self.shape[0],self.shape[1])
        B = other.__rmul__(-1)
        resultado = self.__add__(B)
        
        return resultado
    
    def __matmul__( self, other ):
        # Esta funcion implementa el producto matricial (notado en Python con el operador "@" ) -> A @ B
        if self.shape[1] != other.shape[0]:
            raise ValueError("los tamaños no se pueden multiplicar")
        resultado = MatrizRala(self.shape[0],other.shape[1])
        #para todas las filas de self 
        for i in range(self.shape[0]): #valor de m
            #para todas las comlunas de other
            for j in range(self.shape[1]): #valor de n 
                suma = 0
                #recorre las columnas de self y las filas de other 
                for k in range(self.shape[1]):
                    suma += self[i,k]*other[k,j]
                
                resultado[i,j]=suma
               
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
    
    def mod_fila_entera(self,numero_fila,valores):
        for i in range(self.shape[1]):
            self[numero_fila,i] = valores[i]
            
    def return_fila_entera(self,numero_fila):
        resultado = []
        for i in range(self.shape[1]):
            resultado.append(self.__getitem__((numero_fila,i)))
        return resultado
    
    def generar_idt(self):
        if self.shape[0] != self.shape[1]:
            raise ValueError("la matriz no es cuadrada")
        
        for i in self.shape[0]:
            self.__setitem__((i,i),1)
       

        
    def generar_inv(self):
       
        if self.shape[0] != self.shape[1]:
            raise ValueError("la matriz no es cuadrada")
        
        identidad = MatrizRala(self.shape[0],self.shape[0])
        resultado = MatrizRala(self.shape[0],self.shape[0])
        
        for i in range(self.shape[0]):
            for j in range(self.shape[0]):
                resultado[i,j] = self[i,j]
                
        identidad.generar_idt()
        
        for i in range(self.shape[0]):
            factor = 1.0 / self[i,i]
            for j in range(self.shape[0]):
                resultado.__setitem__((i,j),resultado[i,j]*factor)
                identidad.__setitem__((i,j),identidad[i,j]*factor)
            for k in range(self.shape[0]):
                if k!=i:
                    factor = self[k,i]
                    for j in range(self.shape[0]):
                        res = resultado[k,j] - (factor*resultado[i,j])
                        res2 = identidad[k,j] - (factor*identidad[i,j])
                        resultado.__setitem__((k,j),res)
                        identidad.__setitem__((k,j),res2)
                        
        return identidad
    
    def __copy__(self):
        resultado = MatrizRala(self.shape[0],self.shape[1])
        for i in range(self.shape[0]):
            for j in range(self.shape[0]):
                resultado[i,j] = self[i,j]
                
        return resultado
                        
        
                
        
#ejerciciio2
def GaussJordan( A, b ):
    # Hallar solucion x para el sistema Ax = b
    # Devolver error si el sistema no tiene solucion o tiene infinitas soluciones, con el mensaje apropiado
    sol = "el sistema tieene sol"
    M, N = A.shape
    #Asegúrate de que b es del tamaño adecuado
    if A.shape[0] != b.shape[0]:
        sol = "el sistema no tiene sol"
        return sol
        
    
    if A.shape[0] < A.shape[1]:
        sol = "tiene infinitas soluciones"
        return sol

    #Crear la matriz extendida con A y b
    mat_aumentada = MatrizRala(M, N + 1)
    for i in range(M):
        for j in range(N):
            mat_aumentada[i, j] = A[i, j]
        mat_aumentada[i, N] = b[i,0]
    
    
    #Eliminación por debajo 
    
    #para todas las filas
    for i in range(A.shape[0]):
        pivot = mat_aumentada[i, i]
        if pivot == 0:
            #raise ValueError("El sistema no tiene solución única")
            sol = "el sistema no tiene sol unica"
            continue
    
        #para todas las filas debajo de i 
        for j in range(i+1, A.shape[0]):
        
            #agarro el elemento debajo del pivot
            factor = mat_aumentada[j,i]
            
            #si ya hay un cero debajo del 
            if factor == 0: 
                continue
            #para todas las columnas 
            for k in range(mat_aumentada.shape[1]):
                
                #para la fila debajo del pvito
                fila_debajo = mat_aumentada[j,k] * pivot 
                #la filadel pivot actual que estamos calculando 
                fila_pivot = mat_aumentada[i,k] * factor
                mat_aumentada.__setitem__((j,k),fila_debajo - fila_pivot)
         
    contador0 = 0       
    #eliminacion hacia arriba
    for i in range(1,A.shape[0]):
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
    #chequeo si es inconsistente            
    for i in range(A.shape[0]):
        for j in range(mat_aumentada.shape[1]):
            if mat_aumentada[i,j] == 0:
                contador0 += 1

        if mat_aumentada[i,mat_aumentada.shape[1]-1] != 0 and contador0 == A.shape[1]:
            sol = "sistema es incosistente, no tiene solucion"
            return sol
        
    #hacer unos en los pivots 
   
    #para cada fila 
    for i in range(A.shape[0]):
        #para cada columnas
        factor = mat_aumentada[i,i]
        if factor != 0:
            for j in range(mat_aumentada.shape[1]):
                if mat_aumentada[i,j] != 0:
                    res = mat_aumentada[i,j]/factor
                    mat_aumentada.__setitem__((i,j),res)
                else:
                    mat_aumentada.__setitem__((i,j),0.0)
                    
    
                
    return sol

def crear_W(data_csv):
    return 


def crear_D(W):
    resultado = MatrizRala(W.shape)
    contador = 0
    for i in W.shape[0]:
        for j in W.shape[1]:
            if W[i,j] == 1:
                contador += 1
        resultado[i,i] = contador