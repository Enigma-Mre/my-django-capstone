
from django import forms

class ChoiceForm(forms.Form):
    choice_text = forms.CharField(label='Choice text', max_length=200)