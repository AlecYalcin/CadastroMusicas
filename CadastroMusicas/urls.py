from django.contrib import admin
from django.urls    import path, include
from Listagem       import views

urlpatterns = [
    path('admin/',      admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),

    path('',            views.index,    name="main"),
    path('login/',      views.login,    name="login"),
    path('register/',   views.register, name="register"),
    path('list/',       views.listagem, name="listagem"),
    path('search/',     views.busca,    name="busca"),

    path('Musica/create',                   views.createMusica, name="cMusica"),
    path('Musica/update/<int:id_Musica>',   views.updateMusica, name="uMusica"),
    path('Musica/delete/<int:id_Musica>',   views.deleteMusica, name="dMusica"),
]
