# IMPORTANTE: Para importar estas clases en otro archivo (que se encuentre en la misma carpeta), escribir:
# from matricesRalas import MatrizRala, GaussJordan 

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
        # COMPLETAR:
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
        if self.shape != other.shape:
            raise ValueError("los tamaños no son iguales")
        
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
                res += str(self[i,j]) + ' '
            
            res += ']\n'

        res += '])'

        return res

def GaussJordan( A, b ):
    # Hallar solucion x para el sistema Ax = b
    # Devolver error si el sistema no tiene solucion o tiene infinitas soluciones, con el mensaje apropiado
    pass





