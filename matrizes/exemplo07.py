import random as rnd

def inicializa_matriz(mat, n, m):
    for i in range(n):
        linha = []
        for j in range(m):
            ele = rnd.randint(0,10)
            linha.append(ele)   # inserimos elemento na linha
        mat.append(linha) # anexamos a linha na matriz

def conta_pares(mat):
    n_linhas = len(mat)
    qtd = 0
    for i in range(n_linhas):
        linha = mat[i]
        n_colunas = len(linha)
        for j in range(n_colunas):
            e = mat[i][j]
            if e % 2 == 0:
                qtd = qtd + 1
    return qtd

def imprimir(mat):
    # imprime em forma de matriz
    print("--------------------------")
    total_linhas = len(mat)
    for lin in range(total_linhas):
        linha_atual = mat[lin]
        print(linha_atual)

if __name__ == "__main__":
    matriz = []
    n_linhas = int(input("Numero de linhas: "))
    n_colunas = int(input("Numero de colunas: "))
    inicializa_matriz(matriz, n_linhas, n_colunas)
    imprimir(matriz)
    quantidade = conta_pares(matriz)    
    print(f"tem {quantidade} de numeros pares")