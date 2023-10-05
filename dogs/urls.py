from django.urls import path
from dogs.views import *

app_name = 'catalog'

urlpatterns = [
    path('', DogsListView.as_view(), name='dogs_list'),
    path('dog/<int:pk>/', DogDetailView.as_view(), name='dogs_detail'),
    path('dog/create/', DogCreateView.as_view(), name='dogs_create'),
    path('dog/<int:pk>/update/', DogUpdateView.as_view(), name='dogs_update'),
    path('dog/<int:pk>/delete/', DogDeleteView.as_view(), name='dogs_delete'),
    path('breeds/', BreedsListView.as_view(), name='breeds_list'),
    path('breeds/<int:pk>/', BreedDetailView.as_view(), name='breed_detail'),
    path('breeds/<int:pk>/dogs/', BreedDogsListView.as_view(), name='breed_dogs_list'),
]
