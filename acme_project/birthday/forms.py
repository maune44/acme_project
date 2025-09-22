from django import forms


class BirthdayForm(forms.Form):
    first_name = forms.CharField(label='Имя', max_length=20)
    last_name = forms.CharField(label='Фамилия', required=False)
    birthday = forms.DateField(label='Дата рождения')
