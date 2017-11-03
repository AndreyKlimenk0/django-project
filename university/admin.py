# -*- coding: utf-8 -*-
from django.contrib import admin
from university.models import (Students, Teacher, Department, Subject, Group,
                               Cource, Evalution)

admin.site.register(Department)
admin.site.register(Cource)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Students)
admin.site.register(Teacher)
admin.site.register(Evalution)
