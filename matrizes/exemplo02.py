matriz = []
for i in range(3):
    linha = [] # variavel local
    for j in range(5):
        linha.append(f"{i},{j}")
    print(linha)
    # percorri todas as colunas da linha i
    matriz.append(linha)

# fora do for i
# print(matriz)
