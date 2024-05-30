import pandas as pd
from matricesRalas import *
import csv
from tabulate import tabulate

def generarIDs(paper):
    ids = []
    nombres = []
    
    with open(paper, newline='',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            # ids.append(row[0])
            nombres.append(row[1])
            # cada posicion de ids nos dice la citacion que vamos a hacer en W
    
    return nombres

def P_it(d,N,W,D):
    d = 0.85

    epsilon = 0.0000001
        
    N = W.shape[0]
        
    #distribucion equiprobable 
    p_t = MatrizRala.getVectorOne(N) * (1/ N)

    #matriz de unos
    unos = MatrizRala.getVectorOne(N)
        
    diff_abs = []
    contador = 0    
    diff = 1
    parte_div = (1 - d) / N
    WD = W @ D

    dWD = d * WD

    print("helo")
    i = 0
    while diff > epsilon:
    
        #caculos intermedios
        dWDP_t = dWD.xVector(p_t)
        
        p_t_mas1 = parte_div * unos + dWDP_t
        p_t = p_t_mas1
            
        #calcular la diferencia con p* osea seria entre p* o p_t
        diff = MatrizRala.diffVectors(p_t_mas1,p_t) 
        diff_abs.append(diff)
        contador +=1 
        return contador, diff_abs, p_t
   

def main():
    papers = 'papers/papers.csv'
    citas = 'papers/citas.csv'


    W = MatrizRala.getW(papers,citas)
    D:MatrizRala = W.getD()

    N = len(papers)
    d = 0.85
 

    t,diff,p_sol = P_it(d, N, W, D)

    p_solNumpy = p_sol.toNumpy()

    indices_mayor_menor = np.argsort(p_solNumpy, axis=0)[::-1]
    p_sol_mayor_menor = p_solNumpy[indices_mayor_menor]
    list10 = []
    listID = []
    listPX = []
    nombres = generarIDs(papers)
    for i in range(10):
        id:int = int(indices_mayor_menor[i])
        listID.append(id)
        list10.append(nombres[id])
        listPX.append(float(p_sol_mayor_menor[i]))
        
    data = []
    for i in range(10):
        data.append([listID[i], list10[i], listPX[i]])

    # Imprimir tabla
    print("Top 10 Papers con Mayor Impacto:")
    print(tabulate(data, headers=["ID", "Nombre", "Probabilidad"], tablefmt="grid"))

if __name__ == "__main__":
    main()