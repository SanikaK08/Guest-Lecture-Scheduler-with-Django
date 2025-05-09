# Guest Lecture Scheduling and Registration System

This is a Django-based web application for managing guest lectures in an academic institution. It provides two user roles:

- **Faculty/Organizer**: Can schedule and manage lectures.
- **Students**: Can view scheduled lectures and register for them.

## Features

- Secure login and role-based access
- Faculty can create, edit, and update the status(scheduled, cancelled, completed) of lectures
- Students can view, register for, and track upcoming lectures
- FullCalendar integration to display events in calendar format
- Alert notification upon successful registration

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, Bootstrap 5, JavaScript (jQuery, FullCalendar.js)
- **Database**: SQLite (default)
- **Authentication:** Django `User` model with custom roles (`student`, `faculty`)
- **Other:** JavaScript alerts, role-based views, session handling


---

## 📁 Project Structure
guest_lecture_project/
├── main/ # Core app (views, models, urls)
│ ├── templates/
│ │ └── main/
│ │ ├── student_dashboard.html
│ │ ├── register_lecture.html
│ │ ├── faculty_dashboard.html
│ │ └── base.html
│ ├── views.py
│ ├── models.py
│ ├── urls.py
│ └── forms.py
├── guest_lecture_project/ # Main Django settings
├── static/ # Static files (CSS/JS)
└── manage.py


## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/guest-lecture-scheduler.git
cd guest-lecture-scheduler

2. Create and Activate a Virtual Environment (optional but recommended)
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate


3. Install Python Dependencies
pip install -r requirements.txt

⚠️ Node modules. All necessary JS/CSS dependencies (like Bootstrap and FullCalendar) are loaded via CDN.

4. Run Migrations
python manage.py migrate

5. Create a Superuser (for admin access)
python manage.py createsuperuser

6. Run the Server
python manage.py runserver

Visit http://127.0.0.1:8000 in your browser.


👤 User Roles
👨‍🏫 Faculty
Access lecture management dashboard.

Use /faculty_dashboard/ or access via role redirection.

👩‍🎓 Student
View lectures on /student_dashboard/

Click Register → confirm registration → alert → return to dashboard.



Notes
Make sure your roles (student, faculty) are defined correctly in the User model or extended user profile.

JavaScript alert pops up after registration confirmation.

You may want to preload some test data or lectures from the Django admin panel.


✨ Future Enhancements
Email notifications on registration.

Attendance marking for faculty.

Export registered students to CSV.

Role-based login redirection from a common login page.

