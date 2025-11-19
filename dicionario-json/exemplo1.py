# dicionario!!

def produto_estoque(nome, valor, quantidade):
    return {
        "nome_prod": nome,
        "valor_prod": valor,
        "qtd_prod": quantidade
    }

def teste_inicial():
    lapis_dic = produto_estoque("lapis", 2.0, 50)
    print(lapis_dic)
    print(type(lapis_dic))
    print("chaves")
    print(lapis_dic.keys())
    print("valores")
    print(lapis_dic.values())
    print("itens (par chave-valor)")
    print(lapis_dic.items())
    print(f"NOME: {lapis_dic["nome_prod"]}")

if __name__ == "__main__":    
    teste_inicial()