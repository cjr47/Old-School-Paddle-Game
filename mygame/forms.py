from django import forms
from .models import Score

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['points', 'player',]
        help_text = {
            'player': 'Enter your intials'
        }