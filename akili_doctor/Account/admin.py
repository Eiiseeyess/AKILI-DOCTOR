from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    '''Admin class that determines the information that appears on the admin model'''
    model = Account

    list_display = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'created_at', 'profile_picture']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'gender', 'date_of_birth')}),
    )
    list_filter = ('gender', 'created_at')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-created_at',)


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'username', 'phone', 'password1', 'password2','gender', 'date_of_birth', 'profile_picture'),
        }),
    )

admin.site.register(Account, AccountAdmin)
