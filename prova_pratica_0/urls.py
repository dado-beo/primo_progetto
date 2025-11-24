from django.urls import path
from prova_pratica_0.views import index ,view_a, view_b

app_name="prova_pratica_0"
urlpatterns=[
    path('', index, name='index'),
    path('somma', view_a, name='somma'),
    path('media', view_b, name='media')
]