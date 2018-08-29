# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'cpf', 'email', 'telefone', 'city', 'adress', 'complement']


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'cpf', 'email', 'name', 'telefone',  'city', 'adress', 'complement', 'is_active', 'is_staff']
