"""Forms of the project."""

# Create your forms here.
from django import forms
from django.core.validators import RegexValidator
from things.models import Thing

class ThingForm(forms.ModelForm):

    class Meta:
        model = Thing
        fields = ('name', 'description', 'quantity')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'quantity': forms.NumberInput(attrs={'min': 0, 'max': 50})
        }
    

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if not password1 == password2:
            raise forms.ValidationError('Passwords do not match.')