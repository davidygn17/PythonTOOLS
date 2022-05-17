import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['davidygn17@gmail.com', 'davidyurigarcianunes93@gmail.com']
)
def test_remetente(destinatario):
    enviador = Enviador()
    destinatarios = ['davidygn17@gmail.com', 'davidyurigarcianunes93@gmail.com']
    destinatario
    resultado = enviador.enviar(
         destinatario,
        'margaridafernandes05@gmail.com',
        'teste de curso DEVPRO',
        'fazendo teste pra aprender como tudo isso funciona'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['','david']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'margaridafernandes05@gmail.com',
            'teste de curso DEVPRO',
            'fazendo teste pra aprender como tudo isso funciona'
        )
