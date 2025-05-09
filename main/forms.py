from django import forms
from .models import GuestLecture
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'role']
class GuestLectureForm(forms.ModelForm):
    class Meta:
        model = GuestLecture
        exclude = ['speaker']
        fields = ['title', 'datetime', 'venue', 'speaker_name','link', 'status']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'status': forms.Select(choices=[
                ('scheduled', 'Scheduled'),
                ('completed', 'Completed'),
                ('canceled', 'Canceled')
            ])
        }
   