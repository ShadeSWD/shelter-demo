from django.db import models
NULLABLE = {'blank': True, 'null': True}


class Breed(models.Model):
    name = models.CharField(max_length=50, verbose_name='Breed', unique=True)
    description = models.TextField(**NULLABLE, verbose_name='Description')
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Changed at', auto_now=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'breed'
        verbose_name_plural = 'breeds'


class Dog(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    SEX_TYPES = ((MALE, 'Male'), (FEMALE, 'Female'))

    name = models.CharField(max_length=50, verbose_name='Dog name')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Breed')
    sex = models.CharField(choices=SEX_TYPES, max_length=6)

    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name='Photo')
    birth_day = models.DateField(**NULLABLE, verbose_name='Date of birth')
    created_at = models.DateTimeField(verbose_name='Created at', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Changed at', auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.breed}'

    class Meta:
        verbose_name = 'dog'
        verbose_name_plural = 'dogs'
