def limpa_cpf(documento):
    return documento.replace("-","").replace(".","")

def cpf_para_lista(documento):
    lista = []
    for c in documento:
        lista.append(int(c))
    return lista

def multiplica(lista, final):
    inicio = 10 if final==8 else 11 # se final for 8 inicio vale 10 caso contrario inicio vale 11
    soma = 0 
    for i in range(final+1):
        # print(inicio*lista[i])
        soma += inicio*lista[i]
        inicio-=1
    return soma

def dv(soma):
    resto = soma%11
    if resto < 2:
        return 0
    else:
        return 11-resto

def valida_cpf(documento):
    #pass TRUE pra cpf valido e FALSE pra cpf invalido
    cpf_limpo = limpa_cpf(documento)
    cpf_lista = cpf_para_lista(cpf_limpo)
    soma_dv1 = multiplica(cpf_lista,8)
    dv1 = dv(soma_dv1)
    if dv1 != cpf_lista[9]:
        return False
    
    soma_dv2 = multiplica(cpf_lista,9)
    dv2 = dv(soma_dv2)
    if dv2 != cpf_lista[10]:
        return False

    return True

if __name__ == "__main__":
    cpf = "902.481.621-39"
    valido = valida_cpf(cpf)
    print(valido)