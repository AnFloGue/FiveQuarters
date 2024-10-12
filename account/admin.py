from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import Account, UserProfile

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_type', 'email', 'first_name', 'last_name', 'username', 'date_joined', 'last_login', 'is_active', 'is_admin', 'is_staff')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    readonly_fields = ('date_joined', 'last_login')
    list_display_links = ('id', 'email', 'first_name', 'last_name', 'username')
    ordering = ('-date_joined',)
    list_filter = ('user_type',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address_line_1', 'address_line_2', 'city', 'state', 'country')
    search_fields = ('user__first_name', 'user__last_name', 'city', 'state', 'country')
    list_display_links = ('user', 'address_line_1', 'address_line_2', 'city', 'state', 'country')

class UserAdmin(DefaultUserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)