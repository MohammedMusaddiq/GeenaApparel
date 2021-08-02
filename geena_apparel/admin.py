from django.contrib import admin
from .models import UserCounter


@admin.register(UserCounter)
class UserCounterAdmin(admin.ModelAdmin):
    list_display = [
        'ip_address',
        'date',
        'time',
    ]
