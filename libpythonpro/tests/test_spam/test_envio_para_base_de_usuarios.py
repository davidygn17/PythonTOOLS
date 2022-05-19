from unittest import mock
from unittest.mock import Mock

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
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'davidygn17@gmail.com',
        'EStudos Python pro',
        'confira os modulos Fantasticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='David', email='davidygn17@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'margaridafernandes05@gmail.com',
        'EStudos Python pro',
        'confira os modulos Fantasticos'
    )
    enviador.enviar.assert_called_once_with(
        'margaridafernandes05@gmail.com',
        'davidygn17@gmail.com',
        'EStudos Python pro',
        'confira os modulos Fantasticos'
    )
