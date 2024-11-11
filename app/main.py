import os
import sys

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.usuario_service import UsuarioService
from app.repositories.usuario_repository import UsuarioRepository
from app.config.connection import Session

os.system("cls || clear")
def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:
        print("\n1. Adicionando Usuario.")
        print("2. Consultar 1 Usuario.")
        print("3. Atualizar Usuario.")
        print("4. Deletar Usuario.")
        print("5. Exibir todos os usuarios cadastrados.")
        print("0. Sair")

   
        opcao = int(input("\nInforme a opção desejada: "))

        match(opcao):
            case 1:
                print("\nAdicionando usuario.")
                nome = input("Digite seu nome: ")
                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")
    
                service.criar_usuario(nome=nome, email=email, senha=senha)

                resposta = input("\nDeseja escolher mais uma opção do menu? ")
                if resposta == "nao":
                    break
            case 2:
                service.consultar_usuario_unico()

                resposta = input("\nDeseja escolher mais uma opção do menu? ")
                if resposta == "nao":
                    break
            case 3:
                service.atualizar_usuario()

                resposta = input("\nDeseja escolher mais uma opção do menu? ")
                if resposta == "nao":
                    break
            case 4:
                service.excluir_usuario()

                resposta = input("\nDeseja escolher mais uma opção do menu? ")
                if resposta == "nao":
                    break
            case 5:
                service.listar_todos_usuarios()

                resposta = input("\nDeseja escolher mais uma opção do menu? ")
                if resposta == "nao":
                    break
            case 0:
                print("\nSair.")
                break
            case _:
                print("\nOpção Invalida. Tente Novamente.")


if __name__ == "__main__":
    main() # Chamada de função