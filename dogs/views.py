from django.shortcuts import render
from dogs.models import Dog, Breed
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView


class DogsListView(ListView):
    model = Dog
    template_name = "dogs/dogs.html"
    context_object_name = 'dogs'
    extra_context = {'title': 'Our dogs'}
    queryset = Dog.objects.all()


class DogDetailView(DetailView):
    model = Dog
    template_name = "dogs/dog.html"
    context_object_name = 'dog'


class BreedsListView(ListView):
    model = Breed
    template_name = "dogs/breeds.html"
    context_object_name = 'breeds'
    queryset = Breed.objects.all()


class BreedDetailView(DetailView):
    model = Breed
    template_name = "dogs/breed.html"
    context_object_name = 'breed'


class BreedDogsListView(ListView):
    model = Dog
    template_name = "dogs/dogs.html"
    context_object_name = 'dogs'
    extra_context = {'title': ''}

    def get_context_data(self, **kwargs):
        breed = Breed.objects.get(pk=self.kwargs['pk'])
        context = {'title': breed.name, 'dogs': Dog.objects.filter(breed_id=self.kwargs['pk'])}
        return context
