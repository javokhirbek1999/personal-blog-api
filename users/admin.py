from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models 
from django.utils.translation import gettext as _

from .models import User

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email','username','name')
    list_filter = ('email','username','name','is_active','is_staff')
    ordering = ('-joined_at',)
    list_display = ('email','id','username','name','is_active','is_staff')
    fieldsets = (
        (None, {'fields': ('email','username')}),
        (_('Personal Info'),{'fields':('name',)}),
        (_('Permissions'),{'fields':('is_active','is_staff','is_superuser')}),
    )
    formfields_overrides = {
        models.TextField: {'widget':Textarea(attrs={'row':20,'cols':60})},
    }
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields': ('email','username','name','password1','password2','is_active','is_staff')
        }),
    )

admin.site.register(User,UserAdminConfig)