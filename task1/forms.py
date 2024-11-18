from django import forms

class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин', required=True)
    password = forms.CharField(min_length=3, widget=forms.PasswordInput(), label='Введите пароль', required=True)
    repeat_password = forms.CharField(min_length=3, widget=forms.PasswordInput(), label='Повторите пароль', required=True)
    age = forms.IntegerField(max_value=999, label='Введите свой возраст', required=True)