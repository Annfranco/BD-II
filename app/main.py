import os
from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from sqlalchemy.orm import Session
from config.connection import Session
from models.usuario import Usuario

os.system("cls || clear")
def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    def adicionar(Usuario):
        # Solicitando dados.
        print("\nAdicionando usuario.")
        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
    
        service.criar_usuario(nome=nome, email=email, senha=senha)
        
        # Listando todos os usuarios.
        print("\nListando todos os usuários.")
        lista_usuarios = service.listar_todos_usuarios()
        for usuario in lista_usuarios:
            print(f"{usuario.nome} - {usuario.email} - {usuario.senha}") 

    def consultar(Usuario):
        # R - Read - select - Consulta
        print("\nExibindo dados de todos os clientes.")
        lista_usuario = session.query(Usuario).all()

        for usuario in lista_usuario:
            print(f"{usuario.nome} - {usuario.email} - {usuario.senha}")

    def atualizar(Usuario):
        # U - Update - UPDATE - Atualizar
        print("\nAtualizando dados dos alunos.")
        email_usuario = input("Digite o e-mail do aluno que será atualizado: ")

        usuario = session.query(Usuario).filter_by(email = email_usuario).first()

        if usuario: 
            usuario.nome = input("Digite seu nome: ")
            usuario.email = input("Digite seu email: ")
            usuario.senha = input("Digite sua senha: ")

            session.commit()
        else:
            print("Usuario não encontrado.")

    def excluir(Usuario):
        # D - Delete - DELETE - Excluir 
        print("\nExcluindo os dados de um usuario.")
        email_usuario = input("Digite o e-mail do aluno que será excluído: ")

        usuario = session.query(Usuario).filter_by(email = email_usuario).first()

        if usuario:
            session.delete(usuario)
            session.commit()
            print(f"Cliente {usuario.nome} excluido com sucesso!")
        else:
            print("Cliente não encontrado.")

    def consultar_apenas_um(Usuario):
        # R - Read - select - Consulta
        print("Consultando os dados de apenas um usuario.")
        email_usuario = input("Digite o e-mail do usuario que deseja consultar: ")

        usuario = session.query(Usuario).filter_by(email = email_usuario).first()

        if usuario:
            print(f"{usuario.nome} -  {usuario.email} - {usuario.senha}")
        else:
            print("Cliente não encontrado.")

    while True:
        print("\n1. Adicionando Usuario.")
        print("2. Consultar Usuarios.")
        print("3. Deletar Usuario.")
        print("4. Atualizar Usuario.")
        print("5. Consultar 1 Usuario.")
        print("6. Sair")

   
        opcao = int(input("\nInforme a opção desejada: "))

        match(opcao):
            case 1:
                adiciona = adicionar(Usuario)

                resposta = input("\nDeseja escolher mais uma opção do menu? ")
                if resposta == "nao":
                    break
            case 2:
                consulta = consultar(Usuario)

                resposta = input("\nDeseja escolher mais uma opção do menu? ")
                if resposta == "nao":
                    break
            case 3:
                deletar = excluir(Usuario)

                resposta = input("\nDeseja escolher mais uma opção do menu? ")
                if resposta == "nao":
                    break
            case 4:
                atualiza = atualizar(Usuario)

                resposta = input("\nDeseja escolher mais uma opção do menu? ")
                if resposta == "nao":
                    break
            case 5:
                consultar_um = consultar_apenas_um(Usuario)

                resposta = input("\nDeseja escolher mais uma opção do menu? ")
                if resposta == "nao":
                    break
            case 6:
                print("\nSair.")
                break
            case _:
                print("\nOpção Invalida. Tente Novamente.")


if __name__ == "__main__":
    main() # Chamada de função