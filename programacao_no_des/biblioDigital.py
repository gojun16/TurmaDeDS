class Livro:

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Páginas: {self.paginas}"


# Coleta de dados
titulo_input = input("Digite o título do livro: ")
autor_input = input("Digite o autor do livro: ")
paginas_input = int(input("Digite a quantidade de páginas: "))

# Instanciação e exibição
meu_livro = Livro(titulo_input, autor_input, paginas_input)
print(meu_livro)
