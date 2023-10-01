from django.urls import path
from dogs.views import DogsListView, BreedsListView

app_name = 'catalog'

urlpatterns = [
    path('', DogsListView.as_view(), name='dogs_list'),
    path('breeds/', BreedsListView.as_view(), name='breeds_list'),
]
