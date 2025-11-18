def produto_estoque(nome, valor, quantidade):
    return {
        "nome_prod": nome,
        "valor_prod": valor,
        "qtd_prod": quantidade
    }

def relatorio_estoque(estoque):
    print("_"*50)
    print("nome_prod\t|valor_prod\t|qtd_prod") #\t -> tab
    for i in range(len(estoque)):
        prod = estoque[i]
        # print(i)
        # print(prod)
        # nome = prod["nome_prod"]
        nome = prod.get("nome_prod","-") # valor padrao -
        valor = prod.get("valor_prod", "R$ 0.00")
        quantidade = prod.get("qtd_prod", 0)
        print(f"{nome:<15}\t|R$ {valor:<6.2f}\t|{quantidade}")

if __name__ == "__main__":
    estoque = []  # lista de produtos
    estoque.append(produto_estoque("lapis",2,50))
    estoque.append(produto_estoque("borracha",1.89,100))
    estoque.append(produto_estoque("caneta azul", 3.1, 35))
    print("-------")
    print(estoque)
    print("-------")
    relatorio_estoque(estoque)

