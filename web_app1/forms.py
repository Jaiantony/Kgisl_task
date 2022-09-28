from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class ExampleForm(forms.Form):
    date = forms.DateField(widget=DateInput)


class AnimalCreationForm(forms.ModelForm):
    class Meta:
        model = Animal_data
        fields = ('animal', 'breed', 'date')
        widgets = {
            "date": DateInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['breed'].queryset = Breed.objects.none()
        if "animal" in self.data:
            try:
                animal_id = int(self.data.get('animal'))
                self.fields['breed'].queryset = Breed.objects.filter(animal_id=animal_id).order_by('name')
            except:
                pass
        elif self.instance.pk:
            pass
