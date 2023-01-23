from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from django                     import forms
from django.forms               import ModelForm
from Listagem                   import models

class MusicaForm(ModelForm):
    class Meta:
        model = models.Musica
        fields = '__all__'
        # widgets = {
        #     'mu_musica': forms.TextInput(attrs={'class': 'basilio'}),
        # }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']