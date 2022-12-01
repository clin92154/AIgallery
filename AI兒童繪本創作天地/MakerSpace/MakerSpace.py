from django import forms
from .models import MakerSpace
class PromptModelForm(forms.ModelForm):
    class Meta:
        model = MakerSpace
        fields = '__all__'
        widgets = {
            'prompt': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'prompt': '敘述',
        }


