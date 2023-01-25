from django.db import models

# Create your models here.
class Musica(models.Model):
    mu_id           = models.AutoField(primary_key=True)
    mu_musica       = models.CharField(max_length=100, verbose_name="Música"           )
    mu_autor        = models.CharField(max_length=100, verbose_name="Autor/Compositor" )
    mu_interprete   = models.CharField(max_length=100, verbose_name="Intérprete/Cantor")
    mu_capa         = models.CharField(max_length=500, verbose_name="Link da Capa"     )

    def __str__(self):
        return self.mu_musica