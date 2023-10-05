from dogs.models import Dog, Breed
from dogs.forms import DogForm, BreedForm
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404


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


class DogCreateView(CreateView):
    model = Dog
    form_class = DogForm
    success_url = '/dogs'

    def form_valid(self, form):
        new_dog = form.save()
        new_dog.save()
        return super().form_valid(form)


class DogUpdateView(UpdateView):
    model = Dog
    form_class = DogForm

    def form_valid(self, form):
        if form.is_valid():
            new_dog = form.save()
            new_dog.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('dogs:dogs_detail', args=[self.kwargs.get('pk')])


class DogDeleteView(DeleteView):
    model = Dog
    context_object_name = 'dog'
    success_url = reverse_lazy("dogs:dogs_list")

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Dog, pk=pk)


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
