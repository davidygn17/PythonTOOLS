from libpythonpro.tests.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    resultado=enviador.enviar(
        'davidygn17@gmail.com',
        'margaridafernandes05@gmail.com',
        'teste de curso DEVPRO',
        'fazendo teste pra aprender como tudo isso funciona'
    )
    assert 'davidygn17@gmail.com' in resultado