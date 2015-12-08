# -*- coding: utf-8 -*-
from django.contrib.auth import forms

from .models import User


class UserCreationForm(forms.UserCreationForm):
    def clean_username(self):
        return self.cleaned_data['username']

    class Meta:
        model = User
        fields = ("username",)


class UserChangeForm(forms.UserChangeForm):
    class Meta:
        model = User
        fields = '__all__'
