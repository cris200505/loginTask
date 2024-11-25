from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from .models import CustomUser
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
    )
    add_fieldsets = (
        (None, {
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
            )
        }),
    )
    fieldsets = (
        (None, {'fields': (
            'username',
            'email',
            'age',
            'password'
        )}),
        ('Permisos', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )}),
    )
    search_fields = ('username', 'email') 


class UserAdmin(auth_admin.UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'twitter', 'photo', 'event')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    limited_fieldsets = (
        (None, {'fields': ('email',)}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'twitter', 'photo')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = auth_admin.AdminPasswordChangeForm
    list_display = ('username', 'email', 'age')  
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    readonly_fields = ('last_login', 'date_joined',)

admin.site.register(CustomUser, UserAdmin)