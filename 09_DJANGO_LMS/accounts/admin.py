from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from .models import Profile


class ProfileInline(admin.StackedInline):
    width = 200
    model = Profile
    can_delete = False
    fields = [
        'user',
        # ('avatar', 'avatar_image'),
        'avatar_image',
        'birthday',
        'city',
    ]

    readonly_fields = ['avatar_image']

    def avatar_image(self, obj):
        return mark_safe(f'<img src="{obj.avatar.url}" width="{self.width}" />')


class CustomUserAdmin(UserAdmin):
    width = 100
    inlines = [ProfileInline]
    list_display = ['username', 'email', 'is_staff', 'avatar_image']
    fieldsets = (
        (None, {'fields': (('username', 'email'), 'password')}),
        ('Personal infor', {'fields': (('first_name', 'last_name'),)}),
        ('Permissions', {
            'fields': (('is_active', 'is_staff', 'is_superuser'), 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': (('last_login', 'date_joined'),)}),
    )

    readonly_fields = ['last_login', 'date_joined']

    def avatar_image(self, obj):
        return mark_safe(f'<img src="{obj.profile.avatar.url}" width="{self.width}" />')

    avatar_image.short_description = 'Avatar'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
