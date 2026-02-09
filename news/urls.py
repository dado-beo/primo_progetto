from django.urls import path
from .views import index, home, articoloDetailView, listaArticoli, query, giornalistaDetailView

app_name = "news"

urlpatterns = [
    path("", index, name="index"),
    path("homeview", home, name="homeview"),
    path("query", query, name="query"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("lista_articoli", listaArticoli, name="lista_articoli"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli"),
    path("giornalistaDetailView/<int:pk>", giornalistaDetailView, name="giornalistaDetailView"),
]