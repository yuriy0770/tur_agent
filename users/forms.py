from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'password1', 'password2']