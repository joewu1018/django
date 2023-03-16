from django.contrib import admin

from students.models import student
# Register your models here.
class studentAdmin(admin.ModelAdmin):
	list_display=("stuName","stuID","stuSex","stuBirth")
admin.site.register(student,studentAdmin)