from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # hint: add your custom fields to the existing fieldsets
    # so wake_time, sleep_time, goals show up when editing a user
    add_fieldsets = UserAdmin.add_fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ('Personal Info', {'fields': ('wake_time', 'sleep_time', 'goals')}),
    )