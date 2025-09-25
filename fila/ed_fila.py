def enfileirar(fila, elemento):
    fila.append(elemento)

def desenfileirar(fila):
    # retira o primeiro elemento da fila
    if len(fila)>0:
        return fila.pop(0) 
    return None

def menu():
    print("-"*15)
    print("1- Adicionar na fila")
    print("2- Retirar da fila")
    print("3- Imprimir fila")
    print("4- Sair")
    opcao = int(input("Escolha a opcao: "))
    return opcao

if __name__ == "__main__":
    opcao = 0
    ed_fila = []
    while opcao != 4:
        opcao = menu() 
        if opcao == 1:
            elem = input("Digite o nome pra inserir: ")
            enfileirar(ed_fila, elem)
        elif opcao == 2:
            retirou = desenfileirar(ed_fila)
            print("---------")
            if retirou != None:
                print(f"Atendido {retirou}")
            else:
                print("Ninguem pra ser atendido")
        elif opcao == 3:
            print("---------")
            print(ed_fila)
        elif opcao == 4:
            print("Encerrando")
        else:
            print("Opcao incorreta")