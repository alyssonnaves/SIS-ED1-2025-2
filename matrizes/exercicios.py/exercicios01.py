import random as rnd

def inicializa_matriz(mat, n, m):
    for i in range(n):
        linha = []
        for j in range(m):
            ele = rnd.randint(0,100)
            linha.append(ele)   
        mat.append(linha) 

def imprimir(mat):
    # imprime em forma de matriz
    print("--------------------------")
    total_linhas = len(mat)
    for lin in range(total_linhas):
        linha_atual = mat[lin]
        print(linha_atual)


if __name__ ==  "__main__":
    dimensao = int(input("dimensao da matriz: "))
    matriz = []
    inicializa_matriz(matriz, dimensao, dimensao)
    imprimir(matriz)