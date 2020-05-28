from django import forms
from django.forms import Form


class ContactForm(Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


    def clean_name(self):
        name = self.cleaned_data['name']
        alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz '
        for letter in name:
            if letter not in alphabet:
                raise forms.ValidationError('Name should be consists of letters only')

        return name







