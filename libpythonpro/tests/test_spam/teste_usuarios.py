import pytest

from libpythonpro.spam.modelos import Usuario
from libpythonpro.tests.test_spam.conftest import Conexao, Sessao


@pytest.fixture(scope='session')
def conexao():
    #Setup
    conexao_obj = Conexao()
    yield conexao_obj
    #tear Down
    conexao_obj.fechar()

@pytest.fixture
def sessao(conexao):
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    sessao_obj.roll_back()
    sessao_obj.fechar()

def test_salvar_usuario(sessao):
    usuario = Usuario(nome='David')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='David'), Usuario(nome='Margarida')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

