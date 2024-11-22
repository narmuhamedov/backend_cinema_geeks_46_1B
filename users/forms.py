# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER = (
    ('M', 'Мужской'),
    ('F', 'Женский'),
)

class CustomRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Электронная почта')
    phone_number = forms.CharField(required=True, label='Номер телефона')
    age = forms.IntegerField(required=True, label='Возраст')
    gender = forms.ChoiceField(choices=GENDER, required=True, label='Пол')

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "age",
            "gender",
            "phone_number",
        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.age = self.cleaned_data["age"]
        user.gender = self.cleaned_data["gender"]
        if commit:
            user.save()
        return user
