from django.contrib import admin
from django.urls    import path, include
from Listagem       import views

urlpatterns = [
    path('admin/',      admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),

    path('',                views.index,    name="main"),
    path('login/',          views.login,    name="login"),
    path('register/',       views.register, name="register"),
    path('about/',          views.about,    name="about"),
    # Páginas de CRUD de Música
    path('Musica/edit',     views.edit,     name="edit"),
    path('Musica/list',     views.listagem, name="listagem"),
    path('Musica/search',   views.busca,    name="busca"),
    # CRUD de MUSICAS
    path('Musica/create',                   views.createMusica, name="cMusica"),
    path('Musica/update/<int:id_Musica>',   views.updateMusica, name="uMusica"),
    path('Musica/delete/<int:id_Musica>',   views.deleteMusica, name="dMusica"),
]
