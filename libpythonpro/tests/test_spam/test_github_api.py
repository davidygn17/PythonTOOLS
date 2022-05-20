from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_Mock = Mock()
    resp_Mock.json.return_value = {
        'login': 'davidygn17', 'id': 98975085,
        'avatar_url': 'https://avatars.githubusercontent.com/u/98975085?v=4',
    }
    github_api.requests.get = Mock(return_value=resp_Mock)
    url = github_api.buscar_avatar('davidygn17')
    assert 'https://avatars.githubusercontent.com/u/98975085?v=4' == url
