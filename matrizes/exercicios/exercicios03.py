from utils import imprimir

def criar_matriz_quadrada(dimensao):
    n_linhas = dimensao
    n_colunas = dimensao
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            ele = int(input(f"digite [{i},{j}]: "))
            linha.append(ele)
        matriz.append(linha)
    return matriz

def eh_simetrica(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != matriz[j][i]:
                print("nao eh simetrica")
                return False
    print("eh simetrica")
    return True

if __name__ == "__main__":
    matriz = criar_matriz_quadrada(4)
    imprimir(matriz)
    eh_simetrica(matriz)