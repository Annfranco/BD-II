from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from config.connection import db

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150), unique=True) # Não aceita e-mail repetido.
    senha = Column(String(150))

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = self._verificar_nome_usuario(nome)
        self.email = self._verificar_email_usuario(email)
        self.senha = self._verificar_senha_usuario(senha)

    def _verificar_nome_usuario(self, nome):

        self._verificar_nome_invalido(nome)
        self._verificar_nome_vazio(nome)

        self.nome = nome
        return self.nome

    def _verificar_email_usuario(self, email):

        self._verificar_email_invalido(email)
        self._verificar_email_vazio(email)

        self.email = email
        return self.email

    def _verificar_senha_usuario(self, senha):

        self._verificar_senha_invalido(senha)
        self._verificar_senha_vazio(senha)

        self.senha = senha
        return self.senha

    def _verificar_nome_vazio(self, nome):
        if not nome.strip():
            raise ValueError("O que está sendo solicitado está vazio.")
        return nome

    def _verificar_nome_invalido(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O que está sendo solicitado está inválido.")
        return nome

    def _verificar_email_vazio(self, email):
        if not email.strip():
            raise ValueError("O que está sendo solicitano está vazio.")
        return email

    def _verificar_email_invalido(self, email):
        if not isinstance(email, str):
            raise TypeError("O que está sendo solicitado está inválido.")
        return email

    def _verificar_senha_vazio(self, senha):
        if not senha.strip():
            raise ValueError("O que está sendo solicitado está vazio.")
        return senha

    def _verificar_senha_invalido(self, senha):
        if not isinstance(senha, str):
            raise TypeError("O que está sendo solicitado está inválido.")
        return senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)
