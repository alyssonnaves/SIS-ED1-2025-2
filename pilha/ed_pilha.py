def empilhar(pilha, conteudo):
    pilha.append(conteudo)
    print(pilha)

def desempilhar(pilha):
    if len(pilha) > 0:
        return pilha.pop()
    else:
        return None

def topo(pilha):
    """
    Consulta o topo da pilha sem retirar
    """
    if len(pilha) > 0:
        return pilha[-1] # consulta ultimo elemento
    else:
        return None

if __name__ == "__main__":
    celulaX = []
    celulaY = []
    empilhar(celulaX,"A")
    empilhar(celulaX,"B")
    print("topo da pilha ", topo(celulaX))
    empilhar(celulaX, "C")
    print("topo da pilha ", topo(celulaX))
    print("----DESEMPILHAR----")
    retirou = desempilhar(celulaX)
    print("Y")
    empilhar(celulaY, retirou)
    # print("retirou: ", retirou)
    print("X")
    print(celulaX)
    retirou = desempilhar(celulaX)
    print("Y")
    empilhar(celulaY, retirou)
    print("X")
    print(celulaX)