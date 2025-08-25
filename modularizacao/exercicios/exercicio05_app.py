from exercicio05 import *
# * para importar todas as funcoes
tipo = "figura"
print("1- Circulo")
print("2- Triangulo")
print("3- Retangulo")
opcao = int(input("Escolha figura: "))
if opcao == 1:
    tipo = "circulo"
    raio = float(input("digite raio: "))
    area = area_circulo(raio)
    perimetro = perimetro_circulo(raio)
elif opcao == 2:
    tipo = "triangulo"
    l1 = float(input("digite lado1: "))
    l2 = float(input("digite lado2: "))
    l3 = float(input("digite lado3: "))
    area = area_triangulo(l1,l2,l3)
    perimetro = perimetro_triangulo(l1,l2,l3)
elif opcao == 3:
    tipo = "retangulo"
    l1 = float(input("digite lado1: "))
    l2 = float(input("digite lado2: "))
    area = area_retangulo(l1, l2)
    perimetro = perimetro_retangulo(l1, l2)

print(f"Calculos - {tipo}")
print(f"Area calculada: {round(area, 1)}")
print(f"Perimetro: {round(perimetro,1)}")