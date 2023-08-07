import pytest

from django.conf import settings
from django.test.client import Client
from mixer.backend.django import mixer

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def author():
    return mixer.blend(settings.AUTH_USER_MODEL)


@pytest.fixture
def news():
    return mixer.cycle(10).blend('news.News')


@pytest.fixture
def article(author):
    x = mixer.blend('news.News', author=author)
    return x


@pytest.fixture
def anonymous_client():
    return Client()


@pytest.fixture
def authorized_client(author):
    client = Client()
    client.force_login(author)

    return client


@pytest.fixture
def notify_mock(requests_mock):
    requests_mock.post('http://test.com', text='success')
