# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from university.models import Students, Teacher, Evalution
from django.views.generic import (ListView, DetailView, FormView,
                                  RedirectView)
from university.forms import StudentsForm, TeacherForm, UserCreateForm
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login


class StudentsList(ListView):
    model = Students
    template_name = 'university/students.html'
    context_object_name = 'students'


class TeachersList(ListView):
    model = Teacher
    template_name = 'university/teachers.html'
    context_object_name = 'teachers'


class StudentDetail(DetailView):
    model = Students
    template_name = 'university/student_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)
        student = get_object_or_404(Students, id=self.kwargs['pk'])
        evalutions = Evalution.objects.filter(student_id=self.kwargs['pk'])
        context['student'] = student
        context['evalutions'] = evalutions
        return context


class StudentsForm(FormView):
    form_class = StudentsForm
    success_url = reverse_lazy('student-form')
    template_name = 'university/students_form.html'

    def form_valid(self, form):
        form.save()
        return super(StudentsForm, self).form_valid(form)


class TeacherForm(FormView):
    form_class = TeacherForm
    success_url = reverse_lazy('teacher-form')
    template_name = 'university/teacher_form.html'

    def form_valid(self, form):
        form.save()
        return super(TeacherForm, self).form_valid(form)


class RegistrationForm(FormView):
    form_class = UserCreateForm
    success_url = reverse_lazy('registration')
    template_name = 'university/registration.html'

    def form_valid(self, form):
        recipient = []
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        if email:
            recipient.append(email)
        send_mail(username, 'message', 'deadshot271998@gmail.com', recipient)
        form.save()
        return super(RegistrationForm, self).form_valid(form)


class DeleteStudentRedirect(RedirectView):
    url = '/university/students/'

    def get_redirect_url(self, *args, **kwargs):
        student = get_object_or_404(Students, pk=kwargs['pk'])
        student.delete()
        return super(DeleteStudentRedirect, self).get_redirect_url(
            *args, **kwargs)


class CopyStudentRedirect(RedirectView):
    url = '/university/students/'

    def get_redirect_url(self, pk, *args, **kwargs):
        evalution = Evalution.objects.filter(student_id=pk)
        evalution.delete()
        return super(CopyStudentRedirect, self).get_redirect_url(
            *args, **kwargs)
