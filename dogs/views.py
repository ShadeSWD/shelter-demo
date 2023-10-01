from django.shortcuts import render
from dogs.models import Dog, Breed
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView


class DogsListView(ListView):
    model = Dog
    template_name = "dogs/dogs.html"
    context_object_name = 'dogs'
    queryset = Dog.objects.all()


class BreedsListView(ListView):
    model = Breed
    template_name = "dogs/breeds.html"
    context_object_name = 'breeds'
    queryset = Breed.objects.all()
