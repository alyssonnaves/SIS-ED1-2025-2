n_linhas = 3    #poderia vir pelo input
n_colunas = 5
matriz = []

# incializar matriz com zeros
for i in range(n_linhas):
    linha = [i]*n_colunas
    matriz.append(linha)

# imprimir
print(matriz)
print("--------------------")
for i in range(n_linhas):
    print(matriz[i])

