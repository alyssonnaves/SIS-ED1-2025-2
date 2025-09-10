from exemplo07 import imprimir

def inicia_matriz():
    nomes_idades = []

    for i in range(3):
        nome = input("Digite nome: ")
        idade = int(input("Digite idade: "))
        linha = [nome, idade]
        nomes_idades.append(linha)

    return nomes_idades

def encontra_mais_novo(tab):
    # idade0 = tab[0][1]
    menor_idade = 1000      #  valores inciais (sentinela) 
    linha_menor = -1        #
    for i in range(len(tab)): # len(tab) devolve num de linhas
        linha = tab[i]
        idade = linha[1]  # idade = tab[i][1]
        if idade < menor_idade:
            # encontrei uma idade menor - atualizar
            menor_idade = idade
            linha_menor = i
    # fim do for
    nome = tab[linha_menor][0]
    return nome

if __name__ == "__main__":
    tabela = inicia_matriz()
    imprimir(tabela)
    mais_novo = encontra_mais_novo(tabela)
    print(f"mais novo: {mais_novo}")