from django import forms
from ..models import PlantedTree

class PlantedTreeForm(forms.ModelForm):
    class Meta:
        model = PlantedTree
        fields = ['tree', 'location', 'planted_at']
        widgets = {
            'planted_at': forms.DateInput(attrs={'type': 'date'}), 
        }