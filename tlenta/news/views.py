import requests

from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

from .models import News
from .forms import NewsForm


def list(request):
    news = News.objects.all()

    return render(request, 'list.html', context={'page_news': news})


def get(request, id):
    article = get_object_or_404(News, pk=id)

    form = NewsForm(instance=article)

    return render(request, 'detail.html', context={'form': form})


# @login_required
# @require_http_methods(['GET', 'POST'])
# def create(request):
#     if request.method == 'GET':
#         return render(request, 'detail.html', context={'form': NewsForm()})
#
#     data = request.POST.copy()
#     data['created_at'] = datetime.now()
#     data['author'] = request.user
#
#     form = NewsForm(data)
#     if form.is_valid():
#         form.save()
#
#     return render(request, 'detail.html', context={'form': form})


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'GET':
        return render(request, 'detail.html', context={'form': NewsForm()})

    data = request.POST.copy()
    data['created_at'] = datetime.now()
    data['author'] = request.user

    form = NewsForm(data)
    if form.is_valid():
        form.save()

        try:
            response = requests.post('http://test.com', {'is_saved': True})
            response.raise_for_status()
        except requests.HTTPError as e:
            print(f'Error notify: {e}')

    return render(request, 'detail.html', context={'form': form})