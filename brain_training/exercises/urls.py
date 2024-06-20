from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('memory/', views.memory, name='memory'),
    path('attention/', views.attention, name='attention'),
    path('problem_solving/', views.problem_solving, name='problem_solving'),
    path('creativity/', views.creativity, name='creativity'),
]