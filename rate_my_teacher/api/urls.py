from .views import TeacherPageView
from django.urls import path

urlpatterns = [
    path('home', TeacherPageView.as_view()),
]