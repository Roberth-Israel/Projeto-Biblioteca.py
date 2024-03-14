from livro.livro_buscar import buscarPorCodigo
from livro.livro_editar import editarLivro
from livro.livro_listar import listarLivros
from livro.livro_deletar import deletarLivro
from livro.livro_registrar import registrarLivro

def menu() -> None:
    while True:
    print("---- Bem Vindo ao Menu ----")
    print("1 = Adicionar livro")
    print("2 = Editar livro")
    print("3 = Deletar livro")
    print("4 = Buscar por Código ")
    print("5 = Listar todos ")
    print("6 = Sair ")

    opcao = input("Selecione a Opção: ")

    if opcao == "1":
        titulo = input("Digite o Titulo: ")
        autor = input("Digite o Autor: ")
        registrarLivro(titulo, autor)

    elif opcao == "2":
        codigo = int(input("Digite o Código: "))
        titulo = input("Digite o Título: ")
        autor = input("Digite o Autor: ")
        editarLivro(codigo, titulo, autor)

    elif opcao == "3":
        codigo = int(input("Digite o Código: "))
        deletarLivro(codigo)

    elif opcao == "4":
        codigo = int(input("Digite o código: "))
        print(buscarPorCodigo(codigo))

    elif opcao == "5":
        listarLivros()

    else:
        break

