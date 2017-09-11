from django.forms import ModelForm, TextInput, EmailField, PasswordInput, CharField, EmailInput, Select
from university.models import Students, Teacher, Department, Group, Subject
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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
        fields = ['name', 'surname']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'surname': TextInput(attrs={'class': 'form-control'})
        }


class DepartmentForm(ModelForm):

    class Meta:
        model = Department
        fields = ['faculty']
        widget = {
            'faculty': TextInput(attrs={'class': 'form-control'})
        }


class GroupForm(ModelForm):

    class Meta:
        model = Group
        fields = ['party']
        widget = {
            'party': TextInput(attrs={'class': 'form-control'})
        }


class SubjectForm(ModelForm):

    class Meta:
        model = Subject
        fields = ['matter']
        widget = {
            'matter': TextInput(attrs={'class': 'form-control'})
        }


class UserCreateForm(UserCreationForm):
    username = CharField(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = EmailField(required=True, widget=EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password1'}))
    password2 = CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password2'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=True)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
