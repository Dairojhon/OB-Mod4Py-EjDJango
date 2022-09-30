from django.db import models
from django.urls import reverse

# Create your models here.
class Directors(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('director_detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)



class Movies(models.Model):
    title = models.CharField(max_length=64)
    director = models.ForeignKey('Directors', on_delete=models.SET_NULL, null=True)
    year = models.CharField(max_length=10, null=True)
    summary = models.TextField(max_length=500,help_text="Escribe aqui una pequeña reseña de la pelicula")

    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])


    def __str__(self):
        return self.title



