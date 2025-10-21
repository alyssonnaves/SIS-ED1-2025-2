# lista = [9, 2, 5, 7, 1]
def  selection_sort(lista):
    for i in range(len(lista)-1):  # i = 0
        i_menor = i                # i_menor = 0, 1, 4
        for j in range(i+1,len(lista)): # j = 1, 2, 3, 4
            if lista[j] < lista[i_menor]:
                i_menor = j
        # troca elementos da posicao i com i_menor
        temp = lista[i]
        lista[i] = lista[i_menor]
        lista[i_menor] = temp

if __name__ == "__main__":
    lista = [9, 2, 5, 7, 1]
    print(f"desordenada: {lista}")
    selection_sort(lista)
    print(f"ordenada: {lista}")