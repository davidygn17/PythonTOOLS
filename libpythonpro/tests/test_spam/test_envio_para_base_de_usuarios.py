import pytest

from libpythonpro.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'davidygn17"gmail.com',
        'EStudos Python pro',
        'confira os modulos Fantasticos'
    )