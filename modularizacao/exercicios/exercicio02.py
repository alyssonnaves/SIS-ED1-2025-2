def status(nota):
    if nota >= 6:
        return "aprovado"
    elif nota >= 4 and nota < 6:
        return "verificacao suplementar"
    else:
        return "reprovado"
    
if __name__ == "__main__":
    valor_nota = float(input("Nota: "))
    resultado = status(valor_nota)
    print(f"Situacao: {resultado}")