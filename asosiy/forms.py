from django import forms


class MuallifForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=20, label="ism")
    nums_of_books = forms.IntegerField(min_value=0, max_value=6, label="k_soni")
    alive = forms.BooleanField(label="tirik")
    birthDate = forms.DateField(label="t_yil")