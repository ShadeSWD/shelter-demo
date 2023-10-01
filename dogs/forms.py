from django import forms
from .models import Dog, Breed


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'breed', 'sex', 'birth_day', 'photo']


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = '__all__'
