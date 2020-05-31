import os
import sys
import tempfile

import pytest

sys.path.append('./web')

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    from web.app import app
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


def test_empty_call(client):
    response = client.get('/api')
    assert response.status_code == 400
    assert b'keyword' in response.data


@pytest.mark.parametrize(('keyword', 'suggestion'), (
    ('hool', 'tool'),
    ('chool', 'school'),
    ('schoo', 'school'),
))
def test_keyword_match(client, keyword, suggestion):
    response = client.get(f'/api?keyword={keyword}')
    res_suggestions = [s[1] for s in response.json['suggestions']]
    assert response.status_code == 200
    assert suggestion in res_suggestions