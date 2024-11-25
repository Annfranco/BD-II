from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository
from app.config.connection import session

class UsuarioService:
    def __init__(self, repository: UsuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            consulta_usuario = self.repository.pesquisar_usuario(usuario.email)

            if consulta_usuario:
                print("Usuário já existe no banco de dados.")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuário salvo com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        print("\nListando todos os usuários.")
        lista_usuarios = self.repository.listar_todos_usuarios()
        for usuario in lista_usuarios:
            print(f"{usuario.nome} - {usuario.email} - {usuario.senha}") 
        
    def excluir_usuario(self):
        try:
            email_usuario = input("Digite o e-mail do usuario que será excluído: ")

            usuario = session.query(Usuario).filter_by(email = email_usuario).first()

            if usuario:
                session.delete(usuario)
                session.commit()
                print(f"Cliente {usuario.nome} excluido com sucesso!")
            else:
                print("Cliente não encontrado.")
                return
            
        except TypeError as erro:
            print("Erro ao excluir usuario: {erro}")
        except Exception as erro:
            print("Ocorreu um erro inesperado: {erro}")

    def atualizar_usuario(self):
        try:
            print("\nAtualizando dados dos alunos.")
            email_usuario = input("Digite o e-mail do usuario que será atualizado: ")

            usuario = session.query(Usuario).filter_by(email = email_usuario).first()

            if usuario: 
                usuario.nome = input("Digite seu nome: ")
                usuario.email = input("Digite seu email: ")
                usuario.senha = input("Digite sua senha: ")

                session.commit()
            else:
                print("Usuario não encontrado.")
                return
            
        except TypeError as erro:
            print("Erro ao excluir usuario: {erro}")
        except Exception as erro:
            print("Ocorreu um erro inesperado: {erro}")
    
    def consultar_usuario_unico(self):
        try:
            print("Consultando os dados de apenas um usuario.")
            email_usuario = input("Digite o e-mail do usuario que deseja consultar: ")

            usuario = session.query(Usuario).filter_by(email = email_usuario).first()

            if usuario:
                print(f"{usuario.nome} -  {usuario.email} - {usuario.senha}")
            else:
                print("Cliente não encontrado.")
                return
            
        except TypeError as erro:
            print("Erro ao excluir usuario: {erro}")
        except Exception as erro:
            print("Ocorreu um erro inesperado: {erro}")


        
