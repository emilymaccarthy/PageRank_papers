# Para correr los tests:
#   1- Instalar pytest: ("pip install pytest")
#   2- Correr en la terminal "pytest tests.py"

import pytest
from matricesRalas import MatrizRala, GaussJordan 
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
        RES[0,1] = 2

        C = A @ B

        assert np.allclose( [RES[i,j] for i in range(2) for j in range(2)], [C[i,j] for i in range(2) for j in range(2)] )
"""
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
"""
#class GaussJordan:
#    def test_soltrivial(self):
#        A = MatrizRala(3,3)
#        B = MatrizRala(3,1)
#        
#        assert 

"""
"""