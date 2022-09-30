from django.shortcuts import render

# Create your views here.
from .models import Directors, Movies

def index(request):
    cant_movies = Movies.objects.all().count()
    cant_directors = Directors.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'cant_movies': cant_movies,
            'cant_directors': cant_directors
        }
    )
def directores(request):
    nom_directores=Directors.objects.all()



    return render(
        request,
        'directors.html',
        context={
            'nom_director': nom_directores,

        }
    )

def peliculas(request):
    nom_peliculas=Movies.objects.all()
    return render(
        request,
        'movies.html',
        context={
            'nom_peliculas':nom_peliculas,

        }
    )

def peliculas_director(request,id_director):
    pelis = Movies.objects.filter(director=id_director)

    return render(request,
                  'movies_detail.html',
                  context={
                      'pelicula_detail':pelis
                  }

                  )
