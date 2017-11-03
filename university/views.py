# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from university.models import Students, Teacher, Evalution
from django.views.generic import (ListView, DetailView, FormView,
                                  RedirectView, TemplateView)
from university.forms import StudentsForm, TeacherForm, RegistrationForm
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
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
        student = Students.objects.all()
        return context


class TeachersList(ListView):
    model = Teacher
    template_name = 'university/teachers.html'
    context_object_name = 'teachers'
    paginate_by = 10

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(TeachersList, self).dispatch(request, *args, **kwargs)


class StudentDetail(DetailView):
    model = Students
    template_name = 'university/student_detail.html'

    def __init__(self, **kwargs):
        super(StudentDetail, self).__init__(**kwargs)
        self.kwargs = None

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


class StudentFormView(FormView):
    form_class = StudentsForm
    success_url = reverse_lazy('student-form')
    template_name = 'university/students_form.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(StudentFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super(StudentFormView, self).form_valid(form)


class TeacherFormView(FormView):
    form_class = TeacherForm
    success_url = reverse_lazy('teacher-form')
    template_name = 'university/teacher_form.html'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(TeacherFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super(TeacherFormView, self).form_valid(form)


class RegistrationView(FormView):
    form_class = RegistrationForm
    success_url = reverse_lazy('register')
    template_name = 'registration/registration_form.html'

    def form_valid(self, form):
        recipient = []
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        if email:
            recipient.append(email)
        send_mail(username, 'message', 'deadshot271998@gmail.com', recipient)
        form.save()
        return super(RegistrationView, self).form_valid(form)


class DeleteStudentRedirect(RedirectView):
    url = '/university/students/'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(DeleteStudentRedirect, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        student = get_object_or_404(Students, pk=kwargs['pk'])
        student.delete()
        return super(DeleteStudentRedirect, self).get_redirect_url(
            *args, **kwargs)


class CopyStudentRedirect(RedirectView):
    url = '/university/students/'

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(CopyStudentRedirect, self).dispatch(request, *args, **kwargs)

    def get_redirect_url(self, pk, *args, **kwargs):
        student = Students.objects.get(pk=pk)
        student.pk = None
        student.save()
        return super(CopyStudentRedirect, self).get_redirect_url(*args, **kwargs)
