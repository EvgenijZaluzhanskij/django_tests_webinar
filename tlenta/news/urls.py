from django.urls import path

from .views import list, get, create

app_name = 'news'

urlpatterns = [
    path('list/', list, name='list'),
    path('<int:id>/', get, name='get'),
    path('create/', create, name='create'),
]
