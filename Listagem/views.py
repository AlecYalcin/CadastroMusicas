from django.shortcuts          import render, redirect
from django.http               import HttpResponse
from Listagem                  import models, forms
from django.contrib.auth.forms import UserCreationForm

#Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "registration/login.html")

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "registration/register.html")

def listagem(request):
    return render(request, "pages/listagem.html")

# CRUD Músicas
def createMusica(request):
    form = forms.MusicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main')
    listagem = {'form_Musica': form}
    return render(request, "showMusica.html", listagem)

def updateMusica(request, id_Musica):
    Musica = models.Musica.objects.get(pk=id_Musica)
    form = forms.MusicaForm(request.POST or None, instance=Musica)
    if form.is_valid():
        form.save()
        return redirect('main')
    listagem = {'form_Musica': form, 'Musica': Musica}
    return render(request, "showMusica.html", listagem)

def deleteMusica(request, id_Musica):
    Musica = models.Musica.objects.get(pk=id_Musica)
    Musica.delete()
    return redirect('main')