from django.contrib import admin
from .models import User, Category, Course, Lesson, Tag


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', "created_date", "active"]
    list_filter = ('name', 'course')
    search_fields = ('name','course__subject')


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)