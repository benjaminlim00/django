from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Student, Lesson


class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        """
        Return the list of students in reverse order of class date.
        """
        return Student.objects.order_by('student_name')
    #objects.all()

class DetailView(generic.DetailView):
    model = Student
    template_name = 'myapp/detail.html'

'''
class LessonsView(generic.DetailView):
    model = Student
    template_name = 'myapp/lessons.html'
'''

def lessons(request):
    lesson_list = Lesson.objects.order_by('-lesson_date')
    return render(request, 'myapp/lessons.html', {'lesson_list': lesson_list})

def edit(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    try:
        selected_lesson = student.lesson_set.get(pk=request.POST['lesson'])
    except (KeyError, Lesson.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'myapp/detail.html', {
            'student': student,
            'error_message': "You didn't select a lesson.",
        })
    else:
        if selected_lesson.present == True:
            selected_lesson.present = False
            selected_lesson.save()
        else:
            selected_lesson.present = True
            selected_lesson.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('myapp:detail', args=(student.id,)))
