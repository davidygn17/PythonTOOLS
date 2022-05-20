from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest .fixture
def avatar_url():
    resp_Mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/98975085?v=4'
    resp_Mock.json.return_value = {
        'login': 'davidygn17', 'id': 98975085,
        'avatar_url': rl,
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_Mock)
    yield url
    github_api.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('davidygn17')
    assert avatar_url == url


def test_buscar_avatar():
    url = github_api.buscar_avatar('davidygn17')
    assert 'https://avatars.githubusercontent.com/u/98975085?v=4' == url
