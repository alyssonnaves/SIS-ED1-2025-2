def imprimir(mat):
    # imprime em forma de matriz
    print("--------------------------")
    total_linhas = len(mat)
    for lin in range(total_linhas):
        linha_atual = matriz[lin]
        print(linha_atual)

n_linhas = 3
n_colunas = 5
matriz = []
for i in range(n_linhas):
    linha = []
    for j in range(n_colunas):
        elemento = i + j
        linha.append(elemento)
    matriz.append(linha)

# imprimir
imprimir(matriz)
matriz[2][2] = matriz[2][2]*10
imprimir(matriz)