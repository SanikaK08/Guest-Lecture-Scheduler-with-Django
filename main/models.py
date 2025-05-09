from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User with role
class User(AbstractUser):
    ROLE_CHOICES = [
        ('faculty', 'Faculty/Organizer'),
        ('student', 'Student'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

# class Speaker(models.Model):
#     name = models.CharField(max_length=100)
#     bio = models.TextField()
#     photo = models.ImageField(upload_to='speakers/', null=True, blank=True)
#     contact_email = models.EmailField()

class GuestLecture(models.Model):
    title = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    venue = models.CharField(max_length=200)
    link = models.URLField(blank=True)
    
    speaker_name = models.CharField(max_length=255, default='Unknown Speaker')
    status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('canceled', 'Canceled')])

class Registration(models.Model):
    lecture = models.ForeignKey(GuestLecture, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
