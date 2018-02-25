#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from university.models import Students, Teacher, Evalution
from django.views.generic import ListView, DetailView, FormView, TemplateView, CreateView
from django.views.generic.edit import FormMixin
from university.forms import StudentsForm, TeacherForm, MyRegistrationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string


class HomePage(TemplateView):
    template_name = 'university/home.html'


@method_decorator(login_required, name='dispatch')
class StudentsList(ListView):
    model = Students
    template_name = 'university/students.html'
    context_object_name = 'students'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(StudentsList, self).get_context_data(**kwargs)
        context['form'] = StudentsForm()
        return context


@method_decorator(login_required, name='dispatch')
class TeachersList(ListView):
    model = Teacher
    template_name = 'university/teachers.html'
    context_object_name = 'teachers'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(TeachersList, self).get_context_data(**kwargs)
        context['form'] = TeacherForm()
        return context


@method_decorator(login_required, name='dispatch')
class StudentDetail(DetailView):
    model = Students
    template_name = 'university/student_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)
        student = get_object_or_404(Students, id=self.kwargs['pk'])
        appraisals = Evalution.objects.filter(student_id=self.kwargs['pk'])
        context['student'] = student
        context['appraisals'] = appraisals
        return context


class StudentView(TemplateView):
    template_name = 'university/student_detail.html'

    def __init__(self, **kwargs):
        super(StudentView, self).__init__(**kwargs)
        self.kwargs = None

    def get_context_data(self, **kwargs):
        context = super(StudentView, self).get_context_data(**kwargs)
        student = get_object_or_404(Students, id=self.kwargs['pk'])
        appraisals = Evalution.objects.filter(student_id=self.kwargs['pk'])
        context['student'] = student
        context['appraisals'] = appraisals
        return context


@method_decorator(login_required, name='dispatch')
class StudentFormView(CreateView, FormMixin):
    form_class = StudentsForm
    success_url = reverse_lazy('students')

    def form_valid(self, form):
        form.save()
        return super(StudentFormView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class TeacherFormView(CreateView, FormMixin):
    form_class = TeacherForm
    success_url = reverse_lazy('teacher')

    def form_valid(self, form):
        form.save()
        return super(TeacherFormView, self).form_valid(form)


class RegistrationView(FormView):
    form_class = MyRegistrationForm
    template_name = 'registration/registration_form.html'

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class DeleteStudentRedirect(TemplateView):
    template_name = 'university/students.html'

    def get(self, request, *args, **kwargs):
        student = get_object_or_404(Students, pk=kwargs['pk'])
        student.delete()
        return super(DeleteStudentRedirect, self).get(request, *args, **kwargs)


@method_decorator(login_required, name='dispatch')
class CopyStudentRedirect(TemplateView):
    template_name = 'university/students.html'

    def post(self, request, *args, **kwargs):
        student = get_object_or_404(Students, pk=self.kwargs['pk'])
        student.id = None
        student.save()
        if request.is_ajax():
            context = {'student': student}
            stud_html = render_to_string('university/student_ajax.html', context)
            return JsonResponse({'stud_html': stud_html})
        return self.get(request, *args, **kwargs)
