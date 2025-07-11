from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('profile_picture', 'bio', 'location', 'birth_date'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
