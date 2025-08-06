from django import forms
from .models import Animal

class CadastroAnimal(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        exclude = ['tutor', 'data_cadastro', 'data_adocao']
        