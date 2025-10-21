def enfileirar(fila, fim, elemento):
    fila[fim] = elemento
    fim = fim + 1 
    return fim

def menu():
    print("---------------------")
    print("1- Enfileirar")
    print("2- Retirar da fila")
    print("3- Imprimir fila")
    print("4- Sair")
    opcao = int(input("opcao: "))
    return opcao

if __name__== "__main__":
    tamanho_fila = 6
    fila = [None]*tamanho_fila
    inicio = 0
    fim = 0
    opcao = -1
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            