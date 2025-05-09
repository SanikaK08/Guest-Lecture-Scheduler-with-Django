from django.contrib import admin
from .models import GuestLecture, Registration, User  # Add all models you want in the admin

admin.site.register(GuestLecture)
admin.site.register(Registration)
admin.site.register(User)