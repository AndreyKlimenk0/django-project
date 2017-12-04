#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.forms import ModelForm, TextInput, EmailField, PasswordInput, CharField, EmailInput, Select, SelectMultiple
from university.models import Students, Teacher
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'surname', 'photo', 'department', 'cource', 'group']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'surname': TextInput(attrs={'class': 'form-control'}),
            'department': Select(attrs={'class': 'form-control'}),
            'cource': Select(attrs={'class': 'form-control'}),
            'group': Select(attrs={'class': 'form-control'}),
        }


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'surname', 'department', 'cource', 'group', 'subject']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'surname': TextInput(attrs={'class': 'form-control'}),
            'department': SelectMultiple(attrs={'class': 'form-control'}),
            'cource': SelectMultiple(attrs={'class': 'form-control'}),
            'group': SelectMultiple(attrs={'class': 'form-control'}),
            'subject': SelectMultiple(attrs={'class': 'form-control'}),
        }


class RegistrationForm(UserCreationForm):
    username = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = EmailField(required=True, widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password1'}))
    password2 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password2'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

'''
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
'''


class LoginForm(AuthenticationForm):
    username = CharField(label=u'Имя пользавателя', widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(label=u'Пароль', widget=PasswordInput(attrs={'class': 'form-control'}))