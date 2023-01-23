from django.contrib     import admin
from Listagem.models    import Musica

# Register your models here.
@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_display = ['mu_musica', 'mu_autor', 'mu_interprete', 'mu_capa']