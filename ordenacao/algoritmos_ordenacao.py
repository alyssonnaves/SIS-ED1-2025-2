# lista = [9, 2, 5, 7, 1]
def  selection_sort(lista, tipo="crescente"):
    comparacoes = 0
    for i in range(len(lista)-1):  # i = 0
        i_alvo = i                # i_menor = 0, 1, 4
        for j in range(i+1,len(lista)): # j = 1, 2, 3, 4
            comparacoes = comparacoes + 1
            if tipo == "crescente" and lista[j] < lista[i_alvo]:
                # encontrou um elemento menor
                i_alvo = j
            if tipo == "descrescente" and lista[j] > lista[i_alvo]:
                i_alvo = j
        # troca elementos da posicao i com i_menor
        # temp = lista[i]
        # lista[i] = lista[i_alvo]
        # lista[i_alvo] = temp
        
        print(lista)
        lista[i], lista[i_alvo] = lista[i_alvo], lista[i]
        
    print(f"comparacoes {comparacoes}")

def bubble_sort(lista):
    j = len(lista) - 1
    while j > 0:
        for i in range(0,j):
            print(lista)
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
            
        j = j - 1

def insertion_sort(lista):
    for i in range(1,len(lista)):
        j = i
        
        while j >= 1 and lista[j-1] > lista[j]:
            lista[j-1], lista[j] = lista[j], lista[j-1]
            
            j = j - 1
            print(lista)

if __name__ == "__main__":
    lista = ["batata", "uva", "limao", "macarrao", "abobora", "laranja"]
    # print(f"desordenada: {lista}")
    # selection_sort(lista)
    lista.sort()
    print(f"ordenada: {lista}")

    print()