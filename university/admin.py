# -*- coding: utf-8 -*-
from django.contrib import admin
from university.models import (Students, Teacher, Department, Subject, Group,
                               Cource, Evalution)

admin.site.register(Department)
admin.site.register(Cource)
admin.site.register(Group)
admin.site.register(Subject)


class DepartmentInline(admin.TabularInline):
    model = Department
    extra = 1


class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1


class GroupInline(admin.TabularInline):
    model = Group
    extra = 1


class TeacherAdmin(admin.ModelAdmin):
    inlines = [
        DepartmentInline,
        SubjectInline,
        GroupInline,
    ]


class StudentsAdmin(admin.ModelAdmin):
    raw_id_fields = ('department', 'cource', 'group')
    list_display = ('name', 'surname', 'department', 'group', 'cource')


class EvalutionAdmin(admin.ModelAdmin):
    raw_id_fields = ('teacher', 'student', 'subject')
    list_display = ('teacher', 'student', 'subject')


admin.site.register(Students, StudentsAdmin)
admin.site.register(Evalution, EvalutionAdmin)
admin.site.register(Teacher, TeacherAdmin)
