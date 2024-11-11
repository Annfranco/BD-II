import pytest

from app.models.usuario import Usuario

@pytest.fixture
def usuario_valido():
    usuario = Usuario("Marta", "marta@gmail.com", "1234")
    return usuario

def test_usuario_nome_valido(usuario_valido):
    assert usuario_valido.nome == "Marta"

def test_usuario_email_valido(usuario_valido):
    assert usuario_valido.email == "marta@gmail.com"

def test_usuario_senha_valido(usuario_valido):
    assert usuario_valido.senha == "1234"

def test_usuario_nome_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("", "marta@gmail.com", "1234")

def test_usuario_nome_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario(000, "marta@gmail.com", "1234")

def test_usuario_email_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitano está vazio."):
        Usuario("Marta","", "1234")

def test_usuario_email_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("Marta", 000, "1234")

def test_usuario_senha_vazio_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="O que está sendo solicitado está vazio."):
        Usuario("Marta", "marta@gmail.com", "")

def test_usuario_senha_invalido_erro():
    with pytest.raises(TypeError, match="O que está sendo solicitado está inválido."):
        Usuario("Marta", "marta@gmail.com", 000)




