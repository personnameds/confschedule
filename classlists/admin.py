from django.contrib import admin
from .models import Klass, Student

class KlassAdmin(admin.ModelAdmin):
    list_display=('name','room','grade','teacher')
    list_filter=('grade',)
    ordering=['-grade']

class StudentAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','klass')
    list_filter=('klass__name','klass__grade','klass__teacher')

admin.site.register(Klass, KlassAdmin)
admin.site.register(Student, StudentAdmin)
