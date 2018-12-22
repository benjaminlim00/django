from django.urls import path

from . import views


app_name = 'myapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:student_id>/edit/', views.edit, name='edit'),
    path('lessons', views.lessons, name='lessons'),

]
