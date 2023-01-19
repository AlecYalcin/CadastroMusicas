from django.shortcuts   import render, redirect
from Listagem            import models, forms

# CRUD Músicas
def createMusica(request):
    form = forms.MusicaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('main')
    listagem = {'form_Musica': form}
    return render(request, "index.html", listagem)

def updateMusica(request, id_Musica):
    Musica = models.Musica.objects.get(pk=id_Musica)
    form = forms.MusicaForm(request.POST or None, instance=Musica)
    if form.is_valid():
        form.save()
        return redirect('main')
    listagem = {'form_Musica': form, 'Musica': Musica}
    return render(request, "index.html", listagem)

def deleteMusica(request, id_Musica):
    Musica = models.Musica.objects.get(pk=id_Musica)
    Musica.delete()
    return redirect('main')