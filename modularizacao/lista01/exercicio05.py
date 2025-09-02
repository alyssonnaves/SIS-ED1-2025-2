
def verifica_separadores(doc):
    resultado = doc[3]=='.' and doc[7]=="." and doc[11]=="-"
    return resultado

def eh_digito(caracter):
    return caracter.isdigit()

def le_cpf():
    cpf = input("digite cpf como ###.###.###-##: ")
    cpf_digitos = cpf[0:3]+cpf[4:7]+cpf[8:11]+cpf[12:]
    if verifica_separadores(cpf) and eh_digito(cpf_digitos):
        print(f"respeita a regra: {cpf}")
    else:
        print(f"NAO respeita a regra: {cpf}")

if __name__ == "__main__":
    op = "sim"
    while op == "sim":
        le_cpf()        
        op = input("Deseja continuar? sim ou nao? ")
