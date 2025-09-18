import os

def limpar_tela():
    #os.system("cls") # wind
    os.system("clear") # linux

def exibir_grade(grd):
    limpar_tela()
    for i in range(len(grd)):
        for j in range(len(grd[i])):
            cont = grd[i][j]
            if j != 2:
                print(f"{cont:^3}", end='|')
            else:
                print(f"{cont:^3}")
        if i !=2:
            print("---|---|---")

def grade():
    matriz = []
    dimensao = 3
    for i in range(dimensao):
        linha = ["","",""]
        matriz.append(linha)
    return matriz

def insercao(grd):
    ok = False
    while not ok:
        linha = int(input("digite a linha desejada: "))
        coluna = int(input("digite a coluna desejada: "))
        if grd[linha][coluna]=="":
            jogada = input("Digite X ou O: ")
            grd[linha][coluna] = jogada
            return True
        else:
            print("posicao preenchida ou invalida, escolha outra")


if __name__ == "__main__":
    grd = grade()
    for i in range(9):
        exibir_grade(grd)
        insercao(grd)
    exibir_grade(grd)


def exibir_grade(grd):