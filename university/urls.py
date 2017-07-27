from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^students/$', views.StudentsList.as_view(), name='students'),
    url(r'^teacher/$', views.TeachersList.as_view(), name='teacher'),
    url(r'^student/(?P<pk>\d+)/$', views.StudentDetail.as_view(),
        name='student'),
    url(r'^students/student-form/$',
        login_required(views.StudentsForm.as_view()),
        name='student-form'),
    url(r'^registration/$', views.RegistrationForm.as_view(),
        name='registration'),
    url(r'^logout/$', auth_views.logout, {
        'next_page': '/university/students/'}, name='logout'),
    url(r'^login/$', auth_views.login, {
        'template_name': 'university/login.html'}, name='login'),
    url(r'^student/(?P<pk>\d+)/delete-student/$',
        views.DeleteStudentRedirect.as_view(), name='delete-student'),
    url(r'^student/(?P<pk>\d+)/copy-student/$',
        views.CopyStudentRedirect.as_view(), name='copy-student'),
    url(r'^teacher/teacher-form/$', views.TeacherForm.as_view(),
        name='teacher-form'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

student_form = login_required(views.StudentsForm.as_view())
teacher_form = login_required(views.TeacherForm.as_view())
delets_student = login_required(views.DeleteStudentRedirect.as_view())
copy_student = login_required(views.CopyStudentRedirect.as_view())
settings.LOGIN_URL = 'registration'
