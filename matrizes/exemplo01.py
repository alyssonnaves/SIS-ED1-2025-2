notas = [[5.0, 4.5, 7.0, 5.2, 6.1],
         [2.1, 6.5, 8.0, 7.0],
         [8.6, 7.0, 9.1]]

cont = soma = 0
for i in range(len(notas)):
    n_cols = len(notas[i])
    print(f"num de colunas na linha {i}: {n_cols} ")
    for j in range(n_cols):
        print(f"{i},{j} = {notas[i][j]}")
        soma += notas[i][j]
        cont += 1
media = soma / cont
print(media)