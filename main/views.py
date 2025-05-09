from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import GuestLecture, Registration
from .forms import GuestLectureForm
from django.utils.timezone import now
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.utils import timezone

from django.contrib.auth import get_user_model

User = get_user_model()

# Home / Landing Page
def home(request):
    return render(request, 'main/home.html')
def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
# Dashboard Routing
@login_required
def dashboard(request):
    if request.user.role == 'faculty':
        return redirect('faculty_dashboard')
    elif request.user.role == 'student':
        return redirect('student_dashboard')
    else:
        messages.error(request, "Access denied.")
        return redirect('home')

# ------------------- FACULTY VIEWS -------------------

@login_required
def faculty_dashboard(request):
    if request.user.role != 'faculty':
        return redirect('access_denied')
    lectures = GuestLecture.objects.order_by('-datetime')
    now = timezone.now()
    upcoming_lectures =  GuestLecture.objects.filter(datetime__gte=now, status__in=['scheduled']).order_by('datetime')
    
    return render(request, 'main/faculty_dashboard.html', {'lectures': lectures, 'upcoming_lectures': upcoming_lectures})

@login_required
def create_lecture(request):
    if request.user.role != 'faculty':
        return redirect('access_denied')
    if request.method == 'POST':
        form = GuestLectureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Lecture created successfully.")
            return redirect('faculty_dashboard')
    else:
        form = GuestLectureForm()
    return render(request, 'main/lecture_form.html', {'form': form})

@login_required
def edit_lecture(request, lecture_id):
    if request.user.role != 'faculty':
        return redirect('access_denied')
    lecture = get_object_or_404(GuestLecture, id=lecture_id)
    form = GuestLectureForm(request.POST or None, instance=lecture)
    if form.is_valid():
        form.save()
        messages.success(request, "Lecture updated successfully.")
        return redirect('faculty_dashboard')
    return render(request, 'main/lecture_form.html', {'form': form})


@login_required
def student_dashboard(request):
    user = request.user
    if request.user.role != 'student':
        return redirect('access_denied')
    # now = timezone.now()
    # Fetch the registered lectures for the student
    registered_ids = Registration.objects.filter(student=request.user).values_list('lecture_id', flat=True)
    lectures = GuestLecture.objects.filter(datetime__gte=now()).order_by('datetime')  # Or filter based on the student
    # registered_lectures = user.registered_lectures.all()
    upcoming_lectures =  GuestLecture.objects.filter(datetime__gte=now(), status__in=['scheduled']).order_by('datetime')
    
    
    return render(request, 'main/student_dashboard.html', {
        'registered_ids': set(registered_ids),
        'available_lectures': lectures, 
        'upcoming_lectures': upcoming_lectures,
        # 'registered_lectures': registered_lectures
    })



@login_required
def register(request, lecture_id):
    if request.user.role != 'student':
        return redirect('access_denied')
    
    lecture = get_object_or_404(GuestLecture, id=lecture_id)
    
    registered = Registration.objects.filter(student=request.user, lecture=lecture).exists()
    
    if request.method == 'POST':
        if not registered:
            Registration.objects.create(student=request.user, lecture=lecture)
            messages.success(request, "Registered successfully!")
            registered = True  # Now mark as registered
        else:
            messages.info(request, "You are already registered for this lecture.")
        # Instead of redirecting, render the confirmation
        return render(request, 'main/register_lecture.html', {'lecture': lecture, 'registered': registered})

    return render(request, 'main/register_lecture.html', {'lecture': lecture, 'registered': registered})

# def register_lecture(request, lecture_id):
#     lecture = get_object_or_404(Lecture, id=lecture_id)
#     if request.method == 'POST':
#         # Logic to register the user for the lecture
#         Registration.objects.create(user=request.user, lecture=lecture)
#         return render(request, 'register_lecture.html', {'lecture': lecture, 'registered': True})
#     return render(request, 'register_lecture.html', {'lecture': lecture})

# ------------------- ERROR VIEW -------------------

def access_denied(request):
    return render(request, 'main/access_denied.html')
