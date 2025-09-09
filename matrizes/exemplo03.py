matriz_letras = [
    ['A','B','C','D'],
    ['E','F','G','H'],
    ['I','J','K','L']
]

for coluna in range(4):
    for linha in range(3):
        elem = matriz_letras[linha][coluna]
        print(elem, end=',')
    # fim do for da coluna 
# fim do for da linha
print()
print("-----------------")


