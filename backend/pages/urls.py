from .views import Ramais,Info, Nivers, Noticias, Mural
from django.urls import path, include

urlpatterns = [
    
    path('ramais/', Ramais.as_view(), name='ramais'),
    path('info/', Info.as_view(), name='informativo'),
    path('nivers/', Nivers.as_view(), name='nivers'),
    path('noticias/', Noticias.as_view(), name='noticias'),
    path('mural/', Mural.as_view(), name='mural'),
    
]