
# parametro valores do tipo list (lista)
def media(valores):
    m = sum(valores) / len(valores)
    return round(m, 2)

def menor(valores):
    m = valores[0]
    for i in range(len(valores)):
        if valores[i] < m:
            # atualiza o m
            m = valores[i]
    return m    #  min(valores)

def maior(valores):
    return max(valores)


def le_temperaturas():
    dias = ["dom","seg","ter","qua","qui","sex","sab"]
    temp = []
    for dia in dias:
        t = float(input(f"Temperatura - {dia}: "))
        temp.append(t)
    return temp

if __name__ == "__main__":
    temperaturas = le_temperaturas()
    med_temp = media(temperaturas)
    temp_min = menor(temperaturas)
    temp_max = maior(temperaturas)
    print("-----------------------")
    print(temperaturas)
    print(f"temperatura media: {med_temp} °C")
    print(f"temperatura minima: {temp_min} °C")
    print(f"temperatura maxima: {temp_max} °C")