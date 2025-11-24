from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, "prova_pratica_0/index.html")

def view_a(request): # somma
    var1 = random.randint(1, 10)
    var2 = random.randint(1, 10)
    somma = var1 + var2
    context = {
        'var1': var1,
        'var2': var2,
        'somma' : somma
    }
    return render(request,"prova_pratica_0/somma.html", context)

def view_b(request): # media
    list = []
    while(len(list) < 30):
        list.append(random.randint(1, 10))
    
    somma = 0
    for i in list:
        somma += list[i]
    media = somma / 30
    
    context = {
        'list1': list,
        'media': round(media, 2)
    }
    return render(request,"prova_pratica_0/media.html", context)
