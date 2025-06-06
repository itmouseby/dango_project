from django import forms
from datetime import date


class AuthorsForm(forms.Form):
    first_name = forms.CharField(label="Имя автора")
    last_name = forms.CharField(label="Фамилия автора")
    date_of_birth = forms.DateField(label="Дата рождения", initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_of_death = forms.DateField(label="Дата смерти", initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
class UsersForm(forms.Form):
    username = forms.CharField(label="Имя пользователя")
    email = forms.EmailField(label="Почта пользователя")
