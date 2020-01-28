from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
# 9-7


# Register your models here.
# 9-7
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {"fields": ("avartar", "gender", "bio","birthdate","language","currency","superhost")}),)


