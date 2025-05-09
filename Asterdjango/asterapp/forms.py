from django.forms import ModelForm
from . models import Moviesinfo

class Movieform(ModelForm):
    class Meta:
        model=Moviesinfo
        fields='__all__'