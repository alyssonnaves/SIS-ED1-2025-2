

def fat_iterativo(n):
    mult = 1
    for indice in range(n,0,-1):
        # print(indice)
        mult = mult*indice
        # print(mult)
    # print("----")
    # print(mult)
    return mult

def fat_recursivo(n):
    if n == 1 or n == 0: # caso base
        return 1
    else:
        return n*fat_recursivo(n-1)

if __name__ == "__main__":
    # r=fat_iterativo(1000)
    r=fat_recursivo(5)
--    print(r)