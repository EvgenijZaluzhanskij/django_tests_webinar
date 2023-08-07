import pytest

from django.urls import reverse
from django.forms.models import model_to_dict


pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize(
    'client',
    [
        'anonymous_client',
        'authorized_client',
    ]
)
def test_list_news(article, author, client, request, article_fields):
    current_client = request.getfixturevalue(client)

    url = reverse('news:get', kwargs={'id': article.pk})

    response = current_client.get(url, follow=True)

    assert response.status_code == 200
    assert response.context.get('form').initial == model_to_dict(article)
    

    for field in article_fields:
        assert response.context.get('form').initial.get(field) == getattr(article, field)
