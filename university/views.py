#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from university.models import Students, Teacher, Evalution
from django.views.generic import ListView, DetailView, FormView, RedirectView, TemplateView, CreateView
from django.views.generic.edit import FormMixin
from university.forms import StudentsForm, TeacherForm, RegistrationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required


class HomePage(TemplateView):
    template_name = 'university/home.html'


class StudentsList(ListView):
    model = Students
    template_name = 'university/students.html'
    context_object_name = 'students'
    paginate_by = 10

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(StudentsList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StudentsList, self).get_context_data(**kwargs)
        context['form'] = StudentsForm()
        return context


class TeachersList(ListView):
    model = Teacher
    template_name = 'university/teachers.html'
    context_object_name = 'teachers'
    paginate_by = 10

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(TeachersList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TeachersList, self).get_context_data(**kwargs)
        context['form'] = TeacherForm()
        return context


class StudentDetail(DetailView):
    model = Students
    template_name = 'university/student_detail.html'

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        super(StudentDetail, self).__init__(**kwargs)

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(StudentDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(StudentDetail, self).get_context_data(**kwargs)
        student = get_object_or_404(Students, id=self.kwargs['pk'])
        evalutions = Evalution.objects.filter(student_id=self.kwargs['pk'])
        context['student'] = student
        context['evalutions'] = evalutions
        return context


class StudentFormView(CreateView, FormMixin):
    form_class = StudentsForm
    success_url = reverse_lazy('students')

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(StudentFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super(StudentFormView, self).form_valid(form)


class TeacherFormView(CreateView, FormMixin):
    form_class = TeacherForm
    success_url = reverse_lazy('teacher')

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(TeacherFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super(TeacherFormView, self).form_valid(form)


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/registration_form.html'

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)


class DeleteStudentRedirect(RedirectView):
    url = reverse_lazy('students')

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteStudentRedirect, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        student = get_object_or_404(Students, pk=kwargs['pk'])
        student.delete()
        return super(DeleteStudentRedirect, self).get(request, *args, **kwargs)


class CopyStudentRedirect(RedirectView):
    url = reverse_lazy('students')

    def __init__(self, **kwargs):
        super(CopyStudentRedirect, self).__init__(**kwargs)
        self.kwargs = None

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(CopyStudentRedirect, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        student = get_object_or_404(Students, pk=self.kwargs['pk'])
        copy_student = dict([(key, student.__dict__[key])
                             for key in student.__dict__ if not key.startswith('_') and key not in 'id'])
        obj = Students(**copy_student)
        obj.save()
        return self.get(request, *args, **kwargs)
