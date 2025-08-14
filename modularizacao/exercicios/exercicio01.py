
def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        r = 1
        for i in range(1,numero+1):
            r = r*i
        
        return r

def combinacao(n, m):
    c = fatorial(n)/(fatorial(m) * fatorial(n-m))
    return c

if __name__ == "__main__":
    total = int(input("total alunos: "))
    parte = int(input("num. de alunos no grupo: "))
    possibilidades = combinacao(total, parte)
    print(f"Temos {possibilidades} combinações")