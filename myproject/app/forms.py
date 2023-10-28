from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        min_length=1,
        label='Имя'
    )
    last_name = forms.CharField(
        max_length=100,
        min_length=1,
        label='Фамилия'
    )
    file = forms.FileField(
    )

class MyForm(forms.Form):
    checkbox1 = forms.BooleanField(label='Чекбокс 1', required=False)
    checkbox2 = forms.BooleanField(label='Чекбокс 2', required=False)
    checkbox3 = forms.BooleanField(label='Чекбокс 3', required=False)