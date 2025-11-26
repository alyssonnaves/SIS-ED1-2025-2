import json

def calc_media(lista):
    qtd = len(lista)
    if qtd != 0:
        return sum(lista)/qtd
    else: 
        return 0

def relatorio(produtos):
    itens = produtos.get("itens",[])  # get - pegar
    print("_"*36)
    print(f"{'ID':<6}\t|{'Descricao':<10}\t|{'Preco medio':<8}")
    if produtos != None:
        for cafe in itens:
            id = cafe.get("id","-")
            desc = cafe.get("descricao","-")
            precos = cafe.get("precos",[])
            media = calc_media(precos)
            print(f"{id:<6}\t|{desc:<10}\t|R$ {media:<8.2f}")
    else:
        print("sem dados para exibir")

def importar_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as f:  # f - file
            dados = json.load(f)
        return dados
    except Exception as e:
        print(f"Falha na carga dos dados: {nome_arquivo}")
        print(f"\tMotivo: {e}")
        return None

if __name__ == "__main__":
    itens = importar_arquivo("./bd/precos.json")
    relatorio(itens)

