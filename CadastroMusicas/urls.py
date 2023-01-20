from django.contrib import admin
from django.urls    import path
from Listagem       import views

urlpatterns = [
    path('admin/',      admin.site.urls),
    path('',            views.index, name="main"),
    path('login/',      views.login, name="login"),
    path('register/',   views.register, name="register"),
    path('Musica/create',                   views.createMusica, name="cMusica"),
    path('Musica/update/<int:id_Musica>',   views.updateMusica, name="uMusica"),
    path('Musica/delete/<int:id_Musica>',   views.deleteMusica, name="dMusica"),
]
