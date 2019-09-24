from django.forms import ModelForm
from .models import Wish


class Wish_Form(ModelForm):
    class Meta:
        model = Wish
        fields = ['description']