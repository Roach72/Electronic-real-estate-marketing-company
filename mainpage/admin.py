from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # تخصيص الحقول التي تظهر في لوحة تحكم Django
    list_display = ['username', 'email', 'full_name', 'mobile_number', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('full_name', 'mobile_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)