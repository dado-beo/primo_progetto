from django.urls import path
from .views import index, home, articoloDetailView

app_name = 'news'

urlpatterns = [
    path('index', index, name="index"),
    path('homeview', home, name="homeview"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
]