from django.forms   import ModelForm
from Listagem       import models

class MusicaForm(ModelForm):
    class Meta:
        model = models.Musica
        fields = '__all__'