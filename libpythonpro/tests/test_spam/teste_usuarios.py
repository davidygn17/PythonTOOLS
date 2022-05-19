import pytest

from libpythonpro.spam.modelos import Usuario
from libpythonpro.tests.test_spam.conftest import Conexao, Sessao



def test_salvar_usuario(sessao):
    usuario = Usuario(nome='David', email='davidygn17@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='David', email='davidygn17@gmail.com'),
        Usuario(nome='Margarida', email='davidygn17@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

