PI = 3.14

def area_circulo(raio):
    return PI*(raio**2)

def area_retangulo(lado1, lado2):
    return lado1*lado2

#Área = √(s * (s - a) * (s - b) * (s - c)) 
def area_triangulo(la1, la2, la3):
    sp = perimetro_triangulo(la1, la2, la3)/2
    fator = sp*(sp-la1)*(sp-la2)*(sp-la3)
    return fator**0.5

def perimetro_circulo(raio):
    return 2*PI*raio

def perimetro_retangulo(lado1, lado2):
    return 2*lado1+2*lado2

def perimetro_triangulo(lado1, lado2, lado3):
    return lado1+lado2+lado3