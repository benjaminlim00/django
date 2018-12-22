from django.contrib import admin
from .models import Student, Lesson, Parent


# Register your models here.
class LessonInline(admin.StackedInline):
    model = Lesson
    #ordering = ('lesson_date',)
    #extra = 3


class StudentAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('student_name', 'number_of_lessons', 'number_of_upcoming_lessons', 'next_lesson')
    list_filter = ['student_name']
    search_fields = ['student_name']


admin.site.register(Student, StudentAdmin)
admin.site.register(Parent)
