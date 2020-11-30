from django import forms
from pages.models import Information

class Info(forms.ModelForm):
    
    class Meta:
        model = Information
        fields = ('name', 'email', 'address', 'city', 'phone', 'state', 'zip', 'comments', 'name1', 'cnumber', 'expm', 'expy', 'cvv', 'arrive', 'depart', 'guest', 'rooms')
