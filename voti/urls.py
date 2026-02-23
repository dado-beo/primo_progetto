from django.urls import path
from .views import index, view_a, view_b, view_c, view_d

app_name = "voti"

urlpatterns = [
    path("", index, name="index"),
    path("lista_materie", view_a, name="lista_materie"),
    path("voti_studenti", view_b, name="voti_studenti"),
    path("media_studenti", view_c, name="media_studenti"),
    path("max_min_voti", view_d, name="max_min_voti"),
]