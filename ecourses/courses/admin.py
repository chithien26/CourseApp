from django.contrib import admin
from django.utils.html import mark_safe
from .models import User, Category, Course, Lesson, Tag


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', "created_date", "active"]
    list_filter = ('name', 'course')
    search_fields = ('name','course__subject')
    readonly_fields = 'image'

    def image(self, lesson):
        return mark_safe('''<img src='static/{img__url}' alt='alt' />'''
                         .format(img__url = lesson.image.name, alt = lesson.name)
        )



admin.site.register(User)
admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)