from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista

# Create your views here.
def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context = {"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage.html", context)

""" 
def home(request):
    a = ""
    g = ""
    for art in Articolo.objects.all():
        a += (art.titolo + "<br>")

    for gio in Giornalista.objects.all():
        g += (gio.titolo + "<br>")
    response = "Articolo:<br>" + a + "<br>Giornalisti:<br>" + g 
    return HttpResponse("<h1>"+ response +"</h1>")
"""

""" 
def home(request):
    a = []
    g = []
    for art in Articolo.objects.all():
        a.append(art.titolo)

    for gio in Giornalista.objects.all():
        g.append(gio.titolo)
    
    response = str(a) + "<br>" + "str(g)"
    print(response)

    return HttpResponse("<h1>"+ response +"</h1>")
"""

def articoloDetailView(request, pk):
    # articolo = Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context = {"articolo":articolo}
    return render(request, "articolo_detail.html", context)