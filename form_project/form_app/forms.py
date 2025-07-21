from django import forms
from .models import FormResponse

class FormResponseForm(forms.ModelForm):
    class Meta:
        model = FormResponse
        fields = '__all__'
