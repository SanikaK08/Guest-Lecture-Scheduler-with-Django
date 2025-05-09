from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('faculty/dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'), 
    
   
    path('lectures/create/', views.create_lecture, name='create_lecture'),
    path('lectures/edit/<int:lecture_id>/', views.edit_lecture, name='edit_lecture'), 
    
    path('register/', views.user_register, name='user_register'),
    path('register/<int:lecture_id>/', views.register, name='lecture_register'),

    
]
