from django.contrib import admin
from . models import School,Student,StrandCreate,Subject,Assesment,Score
# Register your models here.

admin.site.register(School)
admin.site.register(Student)
# admin.site.register(Progress)
admin.site.register(Subject)
admin.site.register(Score)
admin.site.register(StrandCreate)
admin.site.register(Assesment)