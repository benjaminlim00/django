from django.test import TestCase
from .models import Student, Lesson
import datetime
from django.utils import timezone

# Create your tests here.

class StudentModelTests(TestCase):
    def test_number_of_lessons_with_no_lessons(self):
        test_student = Student(student_name = 'test')
        self.assertIs(test_student.number_of_lessons(), 0)
    def test_number_of_lessons_with_lessons(self):
        test_student = Student(student_name = 'test')
        #test_student.lesson_set.add(Lesson.objects.create(lesson_date = timezone.now(), teacher = 'ben'))
        self.assertIs(test_student.number_of_lessons(), test_student.lesson_set.all().count())
    def test_number_of_upcoming_lessons_with_no_lessons(self):
        test_student = Student(student_name = 'test')
        self.assertIs(test_student.number_of_lessons(), 0)
    def test_number_of_upcoming_lessons_with_lessons(self):
        test_student = Student(student_name = 'test')
        #test_student.lesson_set.add(Lesson.objects.create(lesson_date = timezone.now(), teacher = 'ben'))
        ls = test_student.lesson_set.exclude(lesson_date__gt=timezone.now())
        self.assertIs(test_student.number_of_lessons(), ls.count())
