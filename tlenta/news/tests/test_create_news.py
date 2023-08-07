import pytest

from django.urls import reverse

from ..models import News


pytestmark = [pytest.mark.django_db]


def test_create_news_unauthorized_user(anonymous_client):
    url = reverse('news:create')

    old_count = News.objects.count()

    response = anonymous_client.post(url, data={
        'text': 'test text',
        'title': 'test title',
    })

    assert response.status_code == 302
    assert response.url == '/accounts/login/?next=/create/'
    assert News.objects.count() == old_count


# def test_create_news_authorized_user(authorized_client):
#     url = reverse('news:create')
#
#     old_count = News.objects.count()
#
#     response = authorized_client.post(url, data={
#         'text': 'test text',
#         'title': 'test title',
#     })
#
#     assert response.status_code == 200
#     assert News.objects.count() == old_count + 1


def test_create_news_authorized_user(authorized_client, notify_mock):
    url = reverse('news:create')

    old_count = News.objects.count()

    response = authorized_client.post(url, data={
        'text': 'test text',
        'title': 'test title',
    })

    assert response.status_code == 200
    assert News.objects.count() == old_count + 1