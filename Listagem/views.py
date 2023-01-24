from django.shortcuts           import render, redirect
from django.http                import HttpResponse
from Listagem                   import models, forms
from django.contrib.auth        import authenticate, login as loginUser, logout, models as modelUser

# ---------------------------------
# Páginas
# ---------------------------------

def index(request):
    return render(request, "index.html")

def listagem(request):
    list = {'MusicList':models.Musica.objects.all()}
    return render(request, "pages/listagem.html", list)

def busca(request):
    buscar = request.GET.get('busca')
    resultados = None
    if buscar:
        resultados = models.Musica.objects.filter(mu_musica__contains=buscar)
    list = {'MusicList':resultados}
    return render(request, "pages/listagem.html", list)

# ---------------------------------
# Manipulação de Usuários
# ---------------------------------

def login(request):
    if request.method == 'GET':
        return render(request, "registration/login.html")
    else:
        email       = request.POST.get('email')
        password    = request.POST.get('password')
        
        mUser = modelUser.User.objects.filter(email=email).first()
        print(mUser)
        user = authenticate(request, username=mUser.username, password=password)
        if user:
            loginUser(request, user)
            return redirect('main')
        else:
            erro = {'erro': 'Email ou Senha INVÁLIDA'}
            return render(request, "registration/login.html", erro)

def register(request):
    if request.method == 'GET':
        return render(request, "registration/register.html")
    else:
        name        = request.POST.get('name')
        email       = request.POST.get('email')
        password    = request.POST.get('password')

        userVerify = modelUser.User.objects.filter(username=name).first()
        emailVerify = modelUser.User.objects.filter(email=email).first()

        if userVerify:
            print(userVerify)
            erro = {'erroUser':'Usuário já Cadastrado'}
            return render(request, "registration/register.html", erro)

        if emailVerify:
            erro = {'erroEmail':'Email já Cadastrado'}
            return render(request, "registration/register.html", erro)

        user = modelUser.User.objects.create_user(
            username=name,
            email=email,
            password=password,
        )

        user.save()
        loginUser(request, user)
        return redirect('main')

# ---------------------------------
# CRUD Músicas
# ---------------------------------

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