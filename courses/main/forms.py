from django import forms
from .models import *


class DataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Data
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input', 'name': 'name', 'placeholder': 'Введите имя'}),
            'second_name': forms.TextInput(attrs={'class': 'input', 'name': 'firstname', 'placeholder': 'Введите фамилию'}),
            'email': forms.TextInput(attrs={'class': 'input', 'name': 'email', 'placeholder': 'Введите свой E-mail'}),
            'telephone': forms.TextInput(attrs={'class': 'input', 'name': 'tel', 'placeholder': 'Введите телефон'}),
        }
