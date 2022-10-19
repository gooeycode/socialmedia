from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomerUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomerUserChangeForm
    model = CustomUser
    list_display = [
        'email',
        'username',
        'age',
        'tagline',
        'is_staff',
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('age', 'tagline',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('age', 'tagline',)}),)

admin.site.register(CustomUser, CustomUserAdmin)
