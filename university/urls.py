#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from university.forms import LoginForm
from . import views


urlpatterns = [
    url(r'^home/$', views.HomePage.as_view(), name='home'),
    url(r'^students/$', views.StudentsList.as_view(), name='students'),
    url(r'^teacher/$', views.TeachersList.as_view(), name='teacher'),
    url(r'^student/(?P<pk>\d+)/$', views.StudentDetail.as_view(), name='student'),
    url(r'^students/student-form/$', views.StudentFormView.as_view(), name='student-form'),
    url(r'^students/teacher-form/$', views.TeacherFormView.as_view(), name='teacher-form'),
    url(r'^registration/$', views.RegistrationView.as_view(), name='registration'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/university/students/'}, name='logout'),
    url(r'^login/$', auth_views.login, {
        'template_name': 'university/index.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^student/(?P<pk>\d+)/delete-student/$', views.DeleteStudentRedirect.as_view(), name='delete-student'),
    url(r'^student/(?P<pk>\d+)/copy-student/$', views.CopyStudentRedirect.as_view(), name='copy-student'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
settings.LOGIN_URL = '/account/register/'
