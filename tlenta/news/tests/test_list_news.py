import pytest

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def test_list_news_anonymous_user(news, anonymous_client):
    url = reverse('news:list')

    response = anonymous_client.get(url, follow=True)

    assert response.status_code == 200
    assert len(response.context.get('page_news')) == len(news)


def test_list_news_authorized_user(news, authorized_client):
    url = reverse('news:list')

    response = authorized_client.get(url, follow=True)

    assert response.status_code == 200
    assert len(response.context.get('page_news')) == len(news)


@pytest.mark.parametrize(
    'client',
    [
        'anonymous_client',
        'authorized_client',
    ]
)
def test_list_news(news, client, request):
    current_client = request.getfixturevalue(client)

    url = reverse('news:list')

    response = current_client.get(url, follow=True)

    assert response.status_code == 200
    assert len(response.context.get('page_news')) == len(news)
