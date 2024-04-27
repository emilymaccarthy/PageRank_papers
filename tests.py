# Para correr los tests:
#   1- Instalar pytest: ("pip install pytest")
#   2- Correr en la terminal "pytest tests.py"

import pytest
from matricesRalas import *
import numpy as np

class TestIndexacionMatrices:
    def test_indexarCeros( self ):
        A = MatrizRala(3,3)
        
        assert np.allclose( np.zeros(9), [A[i,j] for i in range(3) for j in range(3)] )

    def test_asignarValor( self ):
        A = MatrizRala(3,3)
        A[0,0] = 1

        assert A[0,0] == 1

    def test_asignarDejaCeros(self):
        A = MatrizRala(3,3)
        A[0,0] = 1

        assert np.allclose( np.zeros(9), [A[i,j] if (i != j and i != 0) else 0 for i in range(3) for j in range(3)] )

    def test_asignarEnMismaFila( self ):
        A = MatrizRala(3,3)
        A[0,1] = 2
        A[0,0] = 1

        assert A[0,1] == 2 and A[0,0] == 1

    def test_reasignar( self ):
        A = MatrizRala(3,3)
        A[1,0] = 1
        A[1,0] = 3

        assert A[1,0] == 3

    def test_asignarEnMismaColumna( self ):
        A = MatrizRala(3,3)
        A[0,0] = 1
        A[1,0] = 2

        assert A[0,0] == 1 and A[1,0] == 2

    def test_asignarIndiceInvalido( self ):
        A = MatrizRala(3,3)
        with pytest.raises(IndexError) as e_info:
            A[3,3] = 1

    def test_indexarIndiceInvalido( self ):
        A = MatrizRala(3,3)
        with pytest.raises(IndexError) as e_info:
            a = A[3,3]

class TestSumaMatrices:
    def test_distintasDimensiones( self ):
        A = MatrizRala(2,3)
        B = MatrizRala(3,3)
        with pytest.raises(Exception) as e_info:
            C = A + B
        
    def test_sumaCorrectamente( self ):
        A = MatrizRala(3,3)
        B = MatrizRala(3,3)

        A[0,0]=1
        A[0,2]=3
        A[2,2]=4

        B[0,2]=3
        B[1,1]=2

        C = A+B
        assert C[0,0] == 1 and C[0,2] == 6 and C[2,2] == 4 and C[1,1] == 2

    def test_sumaNula( self ):
        A = MatrizRala(2,2)
        B = MatrizRala(2,2)

        A[0,0] = 1
        A[0,1] = 1
        A[1,0] = 1
        A[1,1] = 1

        C = A + B

        assert np.allclose( np.zeros(4) + 1, [C[i,j] for i in range(2) for j in range(2)] )

    def test_sumaOpuestos( self ):
        A = MatrizRala(2,2)
        B = MatrizRala(2,2)

        A[0,0] = 1
        A[0,1] = 1
        A[1,0] = 1
        A[1,1] = 1

        B[0,0] = -1
        B[0,1] = -1
        B[1,0] = -1
        B[1,1] = -1

        C = A + B

        assert np.allclose( np.zeros(4), [C[i,j] for i in range(2) for j in range(2)] )

class TestProductoPorEscalar:
    def test_escalaCorrectamente( self ):
        A = MatrizRala(3,3)
        A[0,0]=1
        A[0,2]=3
        A[2,2]=4

        C = A * 13
        assert C[0,0] == (1*13) and C[0,2] == (3*13) and C[2,2] == (4*13)

    def test_escalaPorCero( self ):
        A = MatrizRala(2,2)

        A[0,0] = 1
        A[0,1] = 1
        A[1,0] = 1
        A[1,1] = 1

        C = A * 0
        assert np.allclose( np.zeros(4), [C[i,j] for i in range(2) for j in range(2)] )

    def test_escalaPorUno( self ):
        A = MatrizRala(2,2)

        A[0,0] = 1
        A[0,1] = 1
        A[1,0] = 1
        A[1,1] = 1

        C = A * 1
        assert np.allclose( np.zeros(4) + 1, [C[i,j] for i in range(2) for j in range(2)] )



class TestProductoMatricial:
    def test_dimensionesEquivocadas(self):
        A = MatrizRala(2,3)
        B = MatrizRala(4,3)
        with pytest.raises(Exception) as e_info:
            C = A @ B

    def test_productoPorUnidad(self):
        A = MatrizRala(3,3)
        B = MatrizRala(3,3)

        A[0,0] = 1
        A[0,1] = 0
        A[0,2] = 0
        A[1,0] = 0
        A[1,1] = 1
        A[1,2] = 0
        A[2,0] = 0
        A[2,1] = 0
        A[2,2] = 1

        B[0,0] = 1
        B[0,1] = 2
        B[0,2] = 3
        B[1,0] = 4
        B[1,1] = 5
        B[1,2] = 6
        B[2,0] = 7
        B[2,1] = 8
        B[2,2] = 9

        C = A @ B

        assert np.allclose( [B[i,j] for i in range(3) for j in range(3)], [C[i,j] for i in range(3) for j in range(3)] )

    def test_productoPorCero(self):
        A = MatrizRala(3,3)
        B = MatrizRala(3,3)

        A[0,0] = 1
        A[0,1] = 2
        A[0,2] = 3
        A[1,0] = 4
        A[1,1] = 5
        A[1,2] = 6
        A[2,0] = 7
        A[2,1] = 8
        A[2,2] = 9

        B[0,0] = 0
        B[0,1] = 0
        B[0,2] = 0
        B[1,0] = 0
        B[1,1] = 0
        B[1,2] = 0
        B[2,0] = 0
        B[2,1] = 0
        B[2,2] = 0

        C = A @ B

        assert np.allclose( np.zeros(9), [C[i,j] for i in range(3) for j in range(3)] )

    def test_productoAndaBien(self):
        A = MatrizRala(2,3)
        B = MatrizRala(3,3)
        RES = MatrizRala(2,2)

        A[0,0]=1
        A[0,2]=3
        A[1,2]=4

        B[2,0]=3
        B[1,1]=2

        RES[0,0] = 9
        RES[1,0] = 12

        C = A @ B

        assert np.allclose( [RES[i,j] for i in range(2) for j in range(2)], [C[i,j] for i in range(2) for j in range(2)] )

    def test_productoPorIdentidad( self ):
        A = MatrizRala(3,3)
        Id = MatrizRala(3,3)

        A[0,0]=1
        A[0,2]=3
        A[1,2]=4

        Id[0,0] = 1
        Id[1,1] = 1
        Id[2,2] = 1

        C1 = A @ Id
        C2 = Id @ A
        assert C1[0,0] == 1 and C1[0,2] == 3 and C1[1,2] == 4 and C2[0,0] == 1 and C2[0,2] == 3 and C2[1,2] == 4 and C1.shape == C2.shape and C1.shape == A.shape

    def test_productoPorCero( self ):
        A = MatrizRala(3,3)
        B = MatrizRala(3,3)

        A[0,0]=1
        A[0,2]=3
        A[1,2]=4

        B[0,0] = 0
        B[1,1] = 0
        B[2,2] = 0

        # C = A @ B

        assert 1 == 1

        # assert np.allclose( np.zeros(9), [C[i,j] for i in range(3) for j in range(3)] )

    def test_heavy_metal(self):
        A = MatrizRala(3,3)
        B = MatrizRala(3,3)
        res = MatrizRala(3,3)

        A[0,0] = 1
        A[0,1] = 2
        A[0,2] = 3  
        A[1,0] = 4
        A[1,1] = 5
        A[1,2] = 6
        A[2,0] = 7
        A[2,1] = 8
        A[2,2] = 9

        B[0,0] = 1
        B[0,1] = 2
        B[0,2] = 3
        B[1,0] = 4
        B[1,1] = 5
        B[1,2] = 6
        B[2,0] = 7
        B[2,1] = 8
        B[2,2] = 9

        C = A @ B
        
        res[0,0] = 30
        res[0,1] = 36
        res[0,2] = 42
        res[1,0] = 66
        res[1,1] = 81
        res[1,2] = 96
        res[2,0] = 102
        res[2,1] = 126
        res[2,2] = 150


        assert np.allclose( [res[i,j] for i in range(3) for j in range(3)], [C[i,j] for i in range(3) for j in range(3)] )



class TestGaussJordan:
    def setup_method(self):
        self.A = MatrizRala(3,3)

        self.A[0,0] = 1
        self.A[0,1] = 0
        self.A[0,2] = 0
        self.A[1,0] = 0
        self.A[1,1] = 1
        self.A[1,2] = 0
        self.A[2,0] = 0
        self.A[2,1] = 0
        self.A[2,2] = 1

        self.b = MatrizRala(3,1)

    def test_soltrivial(self):

        self.b[0,0] = 1
        self.b[1,0] = 2
        self.b[2,0] = 3

        x = GaussJordan(self.A, self.b)
        print([self.b[i,0] for i in range(3)])
        print([x[i,0] for i in range(3)] )

        assert np.allclose( [self.b[i,0] for i in range(3)], [x[i,0] for i in range(3)] )
    
    def test_no_posibilidad(self):
        A = MatrizRala(3,1)
        b = MatrizRala(2,1)
        
        with pytest.raises(Exception) as e_info:
            x = GaussJordan(A,b)
            
        assert "Las dimensiones de A y b no coinciden" in str(e_info.value)
        
    def test_mat_2x2_solunica(self):
        A = MatrizRala(2,2)
        b = MatrizRala(2,1)
        ## opcion 1: sol unica
        A[0,0] = 5
        A[0,1] = 2
        A[1,0] = -3
        A[1,1] = 3
       
        b[0,0] = 3
        b[1,0] = 15
        
        x = GaussJordan(A,b) 
        
        assert np.allclose([-1,4],[x[i,0] for i in range(2)])

    def test_mat_2x2_infsol(self):
        A = MatrizRala(2,2)
        b = MatrizRala(2,1)
        #opcion 2: sol infinitas
        A[0,0] = 3
        A[0,1] = -1
        A[1,0] = -6
        A[1,1] = 2
        
        b[0,0] = 2
        b[1,0] = -4
        
        with pytest.raises(Exception) as e_info:
            x = GaussJordan(A,b)
            
        assert "El sistema tiene infinitas soluciones" in str(e_info.value)
        
    def test_mat_2x3_infsol(self):
        A = MatrizRala(2,3)
        b = MatrizRala(2,1)
        ## opcion 1: sol unica
        A[0,0] = 3
        A[0,1] = -1
        A[0,2] = 7
       
        A[1,0] = 6
        A[1,1] = 0
        A[1,2] = 1
      
       
        b[0,0] = 1
        b[1,0] = 2
       
        
        with pytest.raises(Exception) as e_info:
            x = GaussJordan(A,b)
            
        assert "El sistema tiene infinitas soluciones" in str(e_info.value)
            
    def test_mat_3x3_solunica(self):
        A = MatrizRala(3,3)
        b = MatrizRala(3,1)
        ## opcion 1: sol unica
        A[0,0] = 5
        A[0,1] = 2
        A[0,2] = 0
        
        A[1,0] = 2
        A[1,1] = 1
        A[1,2] = -1
        
        A[2,0] = 2
        A[2,1] = 3
        A[2,2] = -1
       
        b[0,0] = 2
        b[1,0] = 0
        b[2,0] = 3
        
        x = GaussJordan(A,b) 
        
        assert np.allclose([-0.2,1.5,1.1],[x[i,0] for i in range(3)])
        
    def test_mat_2x1(self):
        A = MatrizRala(2,1)
        b = MatrizRala(2,1)
        ## opcion 1: sol unica
        A[0,0] = 0
    
        
        A[1,0] = 3
       
        
       
        b[0,0] = 5
        b[1,0] = 1
      
        
        with pytest.raises(Exception) as e_info:
            x = GaussJordan(A,b)
            
        assert "El sistema tiene infinitas soluciones" in str(e_info.value)
             
    def test_mat_1x2(self):
        A = MatrizRala(1,2)
        b = MatrizRala(1,1)
        ## opcion 1: sol unica
        A[0,0] = 1
    
        
        A[0,1] = 3
       
        
       
        b[0,0] = 5
    
      
        
        with pytest.raises(Exception) as e_info:
            x = GaussJordan(A,b)
            
        assert "El sistema tiene infinitas soluciones" in str(e_info.value)
        
    
    
    

       


