def altera_valor(idade):
    print(f"inicio da funcao: {idade}")
    idade = idade*10
    print(f"termino da funcao: {idade}")

idade = 5
print(f"fora da funcao (antes): {idade}")
altera_valor(idade)
print(f"fora da funcao (depois): {idade}")
