import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario

class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1

@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='David', email='davidygn17@gmail.com'),
            Usuario(nome='Margarida', email='davidygn17@gmail.com')
        ],
        [
            Usuario(nome='David', email='davidygn17@gmail.com')
        ]
    ]

)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'davidygn17@gmail.com',
        'EStudos Python pro',
        'confira os modulos Fantasticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
        usuario=Usuario(nome='David', email='davidygn17@gmail.com')
        sessao.salvar(usuario)
        enviador = EnviadorMock()
        enviador_de_spam = EnviadorDeSpam(sessao, enviador)
        enviador_de_spam.enviar_emails(
            'margaridafernandes05@gmail.com',
            'EStudos Python pro',
            'confira os modulos Fantasticos'
        )
        assert enviador.parametros_de_envio == (
            'margaridafernandes05@gmail.com',
            'davidygn17@gmail.com',
            'EStudos Python pro',
            'confira os modulos Fantasticos'
        )
