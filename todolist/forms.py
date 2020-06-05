from django import forms
from .models import tasklist
class taskform(forms.ModelForm):
    class Meta:
        model= tasklist
        fields=['task','done']
    
