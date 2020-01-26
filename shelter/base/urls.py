from django.urls import path
from .views import DogsListView


urlpatterns = [
    path('', DogsListView.as_view(), name='dogs-list'),
]


