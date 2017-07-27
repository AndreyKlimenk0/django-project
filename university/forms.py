from django.forms import ModelForm
from university.models import Students, Teacher


class StudentsForm(ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'surname', 'photo', 'department', 'cource', 'group']


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
