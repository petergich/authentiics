from django.forms import ModelForm
from .models import shoes

class MyModelForm(ModelForm):
    class Meta:
        model = shoes
        fields = '__all__'
    