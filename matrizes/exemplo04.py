# criar uma matriz com valores 0
lin = int(input("Digite qtd de linhas: "))
col = int(input("Digite qtd de colunas: "))
valores = [] # minha matriz

for linha in range(lin):
    lista = []
    for coluna in range(col):
        lista.append(linha+coluna)
    valores.append(lista)

print(valores)
print("----------")
for linha in range(lin):
    for coluna in range(col):
        elem = valores[linha][coluna]
        print(elem, end="\t")
    # fim das colunas
    print() # pra dar ENTER
    