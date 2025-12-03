import json

# ============================
# 1) Carregar dados do JSON
# ============================

def carregar_dados():
    """Carrega o arquivo livros.json.  
       COMPLETE A FUNÇÃO."""
    pass


# ============================
# 2) Listar todos os livros
# ============================

def listar(livros):
    """Exibe a lista completa de livros da livraria."""
    pass


# ============================
# 3) Buscar livro por título
# ============================

def buscar(livros, titulo):
    """Retorna o dicionário do livro cujo título coincide (case insensitive)."""
    pass


# ============================
# 4) Calcular valor total em estoque
# ============================

def valor_total(livro):
    """Retorna o valor total em estoque (quantidade × preço)."""
    pass


# ============================
# 5) Livro mais caro da livraria
# ============================

def livro_mais_caro(livros):
    """Retorna o título e o preço do livro mais caro."""
    pass


# ============================
# 6) Menu principal
# ============================

def menu():
    livros = carregar_dados()

    while True:
        print("\n===== MENU LIVRARIA =====")
        print("1. Listar todos os livros")
        print("2. Buscar livro por título")
        print("3. Mostrar livro mais caro")
        print("4. Sair")

        op = input("Escolha: ")

        if op == "1":
            listar(livros)

        elif op == "2":
            titulo = input("Título: ")
            livro = buscar(livros, titulo)
            if livro:
                print("Encontrado:", livro)
                print("Valor total em estoque: R$", valor_total(livro))
            else:
                print("Livro não encontrado.")

        elif op == "3":
            titulo, preco = livro_mais_caro(livros)
            print(f"Livro mais caro: {titulo} - R${preco:.2f}")

        elif op == "4":
            print("Encerrando…")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()