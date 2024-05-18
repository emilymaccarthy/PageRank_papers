    def __matmul2__( self, other ):

        if self.shape[1] != other.shape[0]:
            raise ValueError("los tamaños no se pueden multiplicar")

        resultado = MatrizRala(self.shape[0],other.shape[1])
        for i in self.fila:
            filaA = self.fila[i]
            currentNodoA = filaA.raiz

            k = 0
            
            while currentNodoA:
                j = currentNodoA.valor[0]
                v = currentNodoA.valor[1]

                                      
    def __matmul__( self, other ):
        # Esta funcion implementa el producto matricial (notado en Python con el operador "@" ) -> A @ B
        
        if self.shape[1] != other.shape[0]:
            raise ValueError("los tamaños no se pueden multiplicar")
        
        resultado = MatrizRala(self.shape[0],other.shape[1])
        
        #para todas las filas de self 
        for current_i in self.filas: #valor de m
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
                
        return resultado
        #self
        # [1,2,3]
        # [2,4,6]
        # [2,3,2]
        #other
        # [1,2,3]
        # [2,4,6]
        # [2,3,2]
        #para cada fila [0,1,2]
        for i in range(self.shape[0]):
            #para cada columna [0,1,2]
            if i in self.filas:
                nodo_self = self.shape[i].raiz
                columna_counter = 0
                while nodo_self is not None:
                    if columna_counter == nodo_self.valor[0]:
                        #si la fila existe en el otro
                        if nodo_self.valor[0] in other.filas:
                            #necesito lelgar hasta el nodo i 
                            fila = nodo.self.valor[0]
                            nodo_other = other.filas[fila].raiz
                            ########## est mal esta linea deberia ser otro for en alguna parte que buusque la combinacion ideal 
                            while nodo_other[0] != i and nodo_other is not None:
                                nodo_other = nodo_other.siguiente
                            #llegue a la columna y existe la ditchosa 
                            if nodo_other[0] == i:
                                sum += nodo_self.valor[1] * nodo_other.valor[1]
                            #nunca encontro la columna , no esta mapeada    
                            else:
                                sum += 0
                        #la fila no esta maappeada para es aposicion entonce sla columna no va a estar presenta
                        else:
                            sum += 0
                    else:
                        sum += 0
                    columna_counter += 1
                    nodo_self = nodo_self.siguiente
                #aca recorri toda la fila si estuviiese entera o no mismo con la columna de other 
                resultado[i]
            else:
                # enrealidad no se ahcce nada esta fila no existe
                # resultado[i]  = no existe 
                pass
                 
            for j in range(other.shape[1]):
                #Si la fila esta mappeada en self 
                #i = 0, exisiste 
                if i in self.filas:
                    #i = 0, existe 
                    if i in other.filas:
                        
                        nodo_self = self.filas[i].raiz
                        while nodo_self is not None:
                            #si la columna que visite existe en la fila del otro
                            #nodo.valor[0] = 0
                            if nodo.valor[0] in other.filas:
                                contar_nodos = 0 #me da el numero de la columan 
                                
                                nodo_other = other.filas[nodo.valor[0]].raiz
                                #llego a la columna que necesito 
                                while contar_nodos != nodo.valor[0]:
                                    nodo_other = nodo_other.siguiente
                                    
                                sum += nodo_self.valor[1] * nodo_other.valor[1]
                                    
                    #hago normal recorro la lista y multiplico 
                else:
                    resultado[i,j] = 0
        # if self.shape[1] != other.shape[0]:
        #     raise ValueError("los tamaños no se pueden multiplicar")
        # result = MatrizRala(self.shape[0],other.shape[1])
        
        
        suma 
        self[1,0] * other[0,2]
        self[1,1] * other[1,2]
        self[1,2] * other[2,2]
        self[1,3] * other[3,2]
        
        # for i in self.filas:
        #     if i not in self.filas:
        #         continue  # This row is entirely zeros

        #     # Initialize the new row in the result matrix
        #     current_row = ListaEnlazada()

        #     # We need to calculate each element C[i, j]
        #     for j in range(other.shape[1]):  # other.shape[1] is the number of columns in B
        #         sum_product = 0
        #         nodoA = self.filas[i].raiz
        #         while nodoA:
        #             k = nodoA.valor[0]  # column index of A
        #             # We need the element B[k, j], check if k is a row in B
        #             if k in other.filas:
        #                 nodoB = other.filas[k].raiz
        #                 while nodoB:
        #                     if nodoB.valor[0] == j:
        #                         sum_product += nodoA.valor[1] * nodoB.valor[1]
        #                         break
        #                     nodoB = nodoB.siguiente
        #             nodoA = nodoA.siguiente

        #         if sum_product != 0:
        #             current_row.push((j, sum_product))  # Assume push method takes a tuple (column_index, value)

        #     if current_row.raiz is not None:
        #         result.filas[i] = current_row

        # return result
        # # #para todas las filas de self 
        # # contado2 = 0
        # # self_fila = 0
        # # other_columna = 0
        # # donde = self_fila, other_columna
        
        # # #recorro todo el diccionario
        # # for current_i in self.filas: #valor de m
        # #     sum = 0
        # #     fila = self.filas[current_i]
        #     nodo_self = fila.raiz
        #     contador = 0
        #     #si estoy yendo fila por fila en self
        #     if current_i == contado2:
        #         #recorro todos los nodoss
        #         while nodo_self is not None:
        #             #si mabas matrice estan completamente llenas el contador siempre igualerse a la columna del nodo self 
        #             #tambien el numero del contador deberia estar en el diccionario de las otras filas 
                    
        #             #si la fila del contador existe en other
        #             if contador in other.filas:
        #                 #si la columna en self existe ;fila de self y coulmna de other mismo numero igual
        #                 if nodo_self.valor[0] == contador:
        #                     fila2 = other.filas[contador]
        #                     nodo_other = fila2.raiz
        #                     #ahora tengo que verififcar que la columna de ese key existe 
        #                     while nodo_other is not None:
        #                         #existe la columna que estamos buscaando 
        #                         if nodo_other.valor[0] == current_i:
        #                             sum += nodo_self.valor[1] * nodo_other.valor[1]  
        #                         nodo_other = nodo_other.siguiente
                                
        #                     #si terino esta iteracion significa que no encontro la columna que buscaba en other
        #                     sum += 0
        #                 #me skippie un nodo osea es un cero en  esa fila columan de self
        #                 else:
        #                     sum += 0
        #             #si no existe la fila en other 
        #             else:
        #                 sum += 0
                        
        #             nodo_self = nodo_self.siguiente
        #             contador += 1
        #     else:
        #         #la fila es toda de 0 osea va a ser 0 todo 
        #         sum += 0
                
        #     resultado[self_fila,]
        #     contado2 += 1
        #     self_fila+= 1
        #     #termino una fila 
                
                    
        
    
        #         #si no existe la key t4endria que no multiplicar esa fila ?
        #         else:
                    
    

                


            #para todas las comlunas de other
        #     for j in range(other.shape[1]): #valor de n     1 0 0 1        1 0  =    0 0
        #         #                                           0 1 0 0        0 1       0 0 
        #         #                                                          1 0       
        #         #                                                          1 1       
        #         suma = 0
        #         #recorre las columnas de self y las filas de other 
                
        #         for k in range(self.shape[1]):
        #             index_k = currentNode.valor[0][1]
        #             suma += currentNode.valor[1] * other[index_k,j]
        #             currentNode.__next__()
                    
        #         resultado[i,j]=suma
               
        # return resultado
    

#parte de get D
 # nodo = fila.raiz
            # while nodo is not None:
            #     if nodo.valor[1] == 1:
            #         cantidad_1s += 1
            #     nodo = nodo.siguiente
            
            # if cantidad_1s != 0:
            #     resultado[i,i] = 1/cantidad_1s
            #     # resultado.filas[i] = ListaEnlazada()
                # fila = resultado.filas[i]
                # fila.raiz = ListaEnlazada.Nodo((i,1/cantidad_1s), None)
                
        
        # for i in range(self.shape[0]):
        #     cantidad_1s = 0
        #     for j in range(self.shape[0]):
        #         if self[i,j] == 1:
        #             cantidad_1s += 1
        #     if cantidad_1s != 0:
        #         resultado[i,i] = 1/cantidad_1s



#parte de gauss verification 

    # if A.shape[0] != A.shape[1]:
    #     raise ValueError("la matriz no es cuadrada")
        
    # identidad = generar_idt(A)
    # resultado = MatrizRala(A.shape[0],A.shape[0])
        
    # for i in range(A.shape[0]):
    #     for j in range(A.shape[0]):
    #         resultado[i,j] = A[i,j]
        
    # for i in range(A.shape[0]):
    #     factor = 1.0 / A[i,i]
            
    #     for j in range(A.shape[0]):
    #         resultado[i,j] *= factor
    #         identidad[i,j] *= factor
                
    #     for k in range(A.shape[0]):
    #         if k!=i:
    #             factor = resultado[k,i]
                    
    #             for j in range(A.shape[0]):
    #                 resultado[k,j] -= factor*resultado[i,j]
    #                 identidad[k,j] -= factor*identidad[i,j]
                        
    # return identidad   
    
    
    
    # def __matmul__( self, other ):
    #     # Esta funcion implementa el producto matricial (notado en Python con el operador "@" ) -> A @ B
        
    #     if self.shape[1] != other.shape[0]:
    #         raise ValueError("los tamaños no se pueden multiplicar")
        
    #     resultado = MatrizRala(self.shape[0],other.shape[1])
    #     cantFilas = len(self.filas)
    #     cont_i = 0
    #     #para todas las filas de self 
    #     for current_i in self.filas: #valor de m
    #         cont_i += 1
    #         print(f"\r Progreso: {(cont_i/cantFilas)*100}%",end="")
    #         #agarro el raiz de la fila 
    #         fila = self.filas[current_i]
    #         if fila.raiz:
    #             rootNode_self = fila.raiz
    #             for j in range(other.shape[1]):
    #                 currentNode = rootNode_self
    #                 suma = 0
    #                 while currentNode is not None:
                        
    #                     current_j = currentNode.valor[0]
    #                     suma += currentNode.valor[1] * other[current_j,j]
    #                     currentNode = currentNode.siguiente

    #                 resultado[current_i,j] = suma
    #         # else:
    #         #     resultado[current_i,j] = 0

