# users/forms.py

from django.contrib.auth.forms import UserCreationForm
from .models import Item, File
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


GEEKS_CHOICES = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

class ItemForm(forms.ModelForm):

    body = forms.CharField(required=True)
    trading_time_1 = forms.DateTimeField(required=True)
    trading_time_2 = forms.DateTimeField(required=True)
    choice = forms.ChoiceField(choices=GEEKS_CHOICES, required=True)


    class Meta:

        model = Item
        exclude = ("user", )

class GeeksForm(forms.Form):
    geeks_field = forms.ChoiceField(choices = GEEKS_CHOICES)


class FileForm(forms.ModelForm):
    file = forms.FileField(required=False)

    class Meta:
        model = File
        exclude = ("item",)