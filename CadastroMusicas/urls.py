from django.contrib import admin
from django.urls    import path
from Listagem       import views

urlpatterns = [
    path('admin/',  admin.site.urls),
    path('',        views.index),
    path('login/',  views.login),
    path('Musica/create',                   views.createMusica, name="cMusica"),
    path('Musica/update/<int:id_Musica>',   views.updateMusica, name="uMusica"),
    path('Musica/delete/<int:id_Musica>',   views.deleteMusica, name="dMusica"),
]
