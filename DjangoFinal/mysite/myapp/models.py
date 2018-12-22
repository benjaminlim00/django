from django.db import models

import time
from django.utils import timezone

# Create your models here.
class Student(models.Model):
	student_name = models.CharField(max_length=20)

	def number_of_lessons(self):
		try:
			return self.lesson_set.all().count()
		except IndexError:
			return 0

	def number_of_upcoming_lessons(self):
		now = timezone.now()
		try:
			ls = self.lesson_set.exclude(lesson_date__gt=now)
			return ls.count()
		except IndexError:
			return 0

	def next_lesson(self):
		try:
			now = timezone.now()
			ls = self.lesson_set.exclude(lesson_date__gt=now)
			#return time.strftime(str(ls[0]))
			return ls[0]
		except IndexError:
			return "No lessons scheduled"
	# fix this part


	def __str__(self):
		return self.student_name

class Lesson(models.Model):
	Student = models.ForeignKey(Student, on_delete=models.CASCADE)
	lesson_date = models.DateTimeField('Lesson Date', default = None)
	teacher = models.CharField(max_length=20, default = None)
	present = models.BooleanField(default=True)

	def student_attendance(self):
		if self.present == True:
			return "{} is present on {}".format(self.Student.student_name, self.lesson_date)
		else:
			return "{} is absent on {}".format(self.Student.student_name, self.lesson_date)

	def __str__(self):
		return str(self.lesson_date)
