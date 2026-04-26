from django.urls import path
from forms_app.views import contatti, listaContatti

app_name = "forms_app"

urlpatterns=[
    path('contattaci/', contatti, name='contatti'),
    path('lista_contatti/', listaContatti, name='lista_contatti'),
]
