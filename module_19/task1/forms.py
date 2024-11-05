from django import forms


class RegistrationForm(forms.Form):
    login = forms.CharField(max_length=30, label='Введите имя')
    password = forms.CharField(min_length=8, label='Введите пароль')
    password_rep = forms.CharField(min_length=8, label='Повторите пароль')
    age = forms.IntegerField(max_value=999, label='Введите возраст')
