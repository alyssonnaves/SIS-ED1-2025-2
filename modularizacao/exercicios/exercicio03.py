def visor(valor):
    print("-"*10)
    print(valor)
    print("-"*10)

def menu():
    print("Opções:")
    print("(1) Somar")
    print("(2) Subtrair")
    print("(3) Multiplicar")
    print("(4) Dividir")
    print("(5) Limpar memória")
    print("(6) Sair do programa")
    print("Qual opção você deseja?")
    opcao = input(">>> ")
    return opcao

def soma(a, b):
    r = a + b
    return r

def subtracao(a, b):
    return a-b

def multiplicacao(a, b):
    return a*b

def divisao(a, b):
    if b != 0:
        return a/b
    else:
        print("Alerta!!! divisao por 0")
        return a # manter valor da memoria

def limpar_tela():
    import os
    #os.system("cls") # wind
    os.system("clear") # linux

if __name__ == "__main__":
    memoria = 0
    op = "0"
    while op != "6":
        limpar_tela()
        visor(memoria)
        op = menu()
        if op == "6":
            print("encerrando")
        elif op in ["1", "2", "3", "4"]:
            numero = float(input("digite valor: "))
            if op == "1":
                memoria = soma(memoria, numero)
            elif op == "2":
                memoria = subtracao(memoria, numero)
            elif op == "3":
                memoria = multiplicacao(memoria, numero)
            elif op == "4":
                memoria = divisao(memoria, numero)
        elif op == "5":
            memoria = 0
        else:
            print("opcao incorreta")