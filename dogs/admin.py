from django.contrib import admin
from dogs.models import *


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'breed', 'birth_day')
    list_filter = ('breed',)
