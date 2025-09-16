import random as rnd
from utils import imprimir # import utils

def criar_matriz(n_linhas, n_colunas):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            elemento = rnd.randint(1,100)
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def espelhar_matriz(matriz):
    n_linhas = len(matriz)
    espelhada = []
    for i in range(n_linhas):
        n_colunas = len(matriz[i])
        linha = []
        for j in range(n_colunas-1,-1,-1):
            elem = matriz[i][j]
            linha.append(elem)
        # fim for j
        espelhada.append(linha)
    # fim for i
    return espelhada

if __name__ == "__main__":
    n = 3
    m = 4
    mat = criar_matriz(n,m)
    imprimir(mat)
    outra = espelhar_matriz(mat)
    imprimir(outra)