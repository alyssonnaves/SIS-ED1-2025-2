"""
funcoes de exemplo
"""
def calcula_media(v):
    """
    Funcao que calcula a media
    """
    soma = 0
    for e in v:
        soma = soma + e
    media = soma / len(v)
    return media

# print(">>> exemplo 01<<<")
# print(__name__)
if __name__=='__main__':
    resultado = calcula_media([9,8,5,10])
    print(f"media calculada = {resultado}")
    lista = list(range(10))
    print(lista)
    resultado = calcula_media(lista)
    print(f"media calculada para lista = {resultado}")