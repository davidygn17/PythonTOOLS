import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario



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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'davidygn17@gmail.com',
        'EStudos Python pro',
        'confira os modulos Fantasticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados
