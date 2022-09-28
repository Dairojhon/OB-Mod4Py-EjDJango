from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('movies/', views.peliculas, name='movies'),
    url('director/', views.directores, name='directors')

]
