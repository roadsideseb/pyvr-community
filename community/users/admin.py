# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib import auth

from .models import User
from .forms import UserCreationForm, UserChangeForm


@admin.register(User)
class UserAdmin(auth.admin.UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')

    add_form = UserCreationForm
    form = UserChangeForm
