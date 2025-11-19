import json

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
        # nome = prod["nome_produto"]
        nome = prod.get("nome_prod","indefinido") # valor padrao -
        valor = prod.get("valor_prod", "R$ 0.00")
        quantidade = prod.get("qtd_prod", 0)
        print(f"{nome:<15}\t|R$ {valor:<6.2f}\t|{quantidade}")

def salvar_json(estoque):
    dados = {"registros": estoque}
    # w -  write
    with open("./bd/base_estoque.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    print("Arquivo salvo com sucesso")

def ler_json():
    # r - read
    with open("./bd/base_estoque.json", "r") as arquivo:
        dados = json.load(arquivo)
    return dados

def teste_escrita():
    estoque = []  # lista de produtos
    estoque.append(produto_estoque("lapis",2,50))
    estoque.append(produto_estoque("borracha",1.89,100))
    estoque.append(produto_estoque("caneta azul", 3.1, 35))
    print("-------")
    print(estoque)
    print("-------")
    relatorio_estoque(estoque)
    salvar_json(estoque)

if __name__ == "__main__":
#    teste_escrita()
    dados_estoque = ler_json()
    relatorio_estoque(dados_estoque.get("registros",[]))

