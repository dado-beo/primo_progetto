from django.shortcuts import render

# La view_a per visualizzare in un elenco la lista delle materie
def view_a (request):
    materie = ["Matematica","Italiano","Inglese","Storia","Geografia"]
    
    context = {
        'materie': materie
    }
    
    return render(request, "voti/lista_materie.html", context)

# La view_b per visualizzare il contenuto del seguente dizionario dei voti : studente : [(materia,voto,assenze)]:
def view_b (request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    context = {
        'voti': voti
    }
    
    return render(request, "voti/voti_studenti.html", context)

# La view_c per visualizzare la media dei voti di ciascuno studente
def view_c (request):
    dati = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    
    studenti = []
    lista_medie = []
    
    for studente in dati:
        media = 0
        n = 0
        studenti.append(studente)
        for materie in dati[studente]:
            media += materie[1]
            n = n+1
        lista_medie.append(media/n)

    
    context = {
        'dati':{
            'studenti': studenti,
            'medie': lista_medie
        }
    }
    
    return render(request, "voti/media_studenti.html", context)

# La view_d per visualizzare i voti massimo e minimo, le materie in cui si sono registrati e gli studenti che li hanno ottenuti
def view_d (request):
    voti = {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
           'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
           'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    max_studente=[]
    min_studente=[]
    max_materia=[]
    min_materia=[]
    max=0
    min=100

    for studente in voti:
        for materia, voto, assenze in voti[studente]:
            if(max<voto):
                max=voto
                max_materia=[materia]
                max_studente=[studente]
            elif(max==voto):
                if(materia not in max_materia):
                    max_materia.append(materia) 
                if(studente not in max_studente):
                    max_studente.append(studente)
            if(min>voto):
                min=voto
                min_materia=[materia]
                min_studente=[studente]
            elif(min==voto):
                if(materia not in min_materia):
                    min_materia.append(materia) 
                if(studente not in min_studente):
                    min_studente.append(studente)

    context = {
            'max_studente': max_studente,
            'min_studente': min_studente,
            'max_materia': max_materia,
            'min_materia': min_materia,
            'max': max,
            'min': min
    }
    
    return render(request, "voti/max_min_voti.html", context)

def index (request):
    return render(request,"voti/index.html")