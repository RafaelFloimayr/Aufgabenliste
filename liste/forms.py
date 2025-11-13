from django import forms
from .models import ListItem

# Create your models here.
class ListItemForm(forms.ModelForm):
    class Meta:
        model = ListItem
        fields=['item_name', 'item_done']
        labels = {
            'item_name': 'Aufgabe',
            'item_done': 'Erledigt',
        }