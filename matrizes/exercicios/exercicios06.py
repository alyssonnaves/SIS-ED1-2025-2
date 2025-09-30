import random as rnd
from utils import imprimir
def eh_igual(A, B):
    # verifica se num de linhas ou colunas de A e B sao diferentes
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return False
    
    for i in range(len(A)):
        linha = A[i]
        for j in range(len(linha)):
            if A[i][j] != B[i][j]: 
                # signifca que A e B sao diferentes
                return False
    return True # sao iguais

def gerar_matriz():
    A = []
    dimensao = 10
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            elemento = rnd.randint(0,1)
            linha.append(elemento)
        A.append(linha)
    return A

def selecionar_submatriz(A, i, j):
    matriz_parte = []
    if i+2 < 10 and j + 3 < 10:
        linha0 = A[i+0][j:j+3]
        linha1 = A[i+1][j:j+3]
        linha2 = A[i+2][j:j+3]
        matriz_parte.append(linha0)
        matriz_parte.append(linha1)
        matriz_parte.append(linha2)
        return matriz_parte
    return None

if __name__ == "__main__":
    matA = [[0,1,1],[1,1,1],[0,0,1]]
    original = gerar_matriz()  # 10 x 10
    
    for i in range(len(original)):
        for j in range(len(original[i])):
            parte = selecionar_submatriz(original, i, j)
            if parte == None:
                break
            else:
                if eh_igual(matA, parte):   
                    print(f"Mat A esta presente em original {i},{j}")
    
    # 
    imprimir(original)
    imprimir(matA)