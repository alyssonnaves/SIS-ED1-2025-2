def imprimir(mat):
    # imprime em forma de matriz
    print("--------------------------")
    total_linhas = len(mat)
    for lin in range(total_linhas):
        linha_atual = mat[lin]
        print(linha_atual)