from django.urls import path
from dogs.views import DogsListView, BreedsListView, BreedDetailView, BreedDogsListView

app_name = 'catalog'

urlpatterns = [
    path('', DogsListView.as_view(), name='dogs_list'),
    path('breeds/', BreedsListView.as_view(), name='breeds_list'),
    path('breeds/<int:pk>/', BreedDetailView.as_view(), name='breed_detail'),
    path('breeds/<int:pk>/dogs/', BreedDogsListView.as_view(), name='breed_dogs_list'),
]
