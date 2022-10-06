from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        # editable field만 가능.
        fields = ['title', 'summary','running_time']
