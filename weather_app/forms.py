from django.forms import ModelForm, TextInput
from .models import City

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ["city"]
<<<<<<< HEAD
        widgets = {"city": TextInput(attrs={"class": "input", "placeholder": "City Name"})} 
=======
        widgets = {"city": TextInput(attrs={"class": "input", "placeholder": "City Name"})}
>>>>>>> first commit
