from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Article, CustomUser
from django.utils.translation import gettext as _

class CUAdmin(UserAdmin):
    ordering = ('login',)
    list_display = ('login', 'email', 'last_login', 'date_joined', 'is_superuser', 'is_staff', 'is_active')
    search_fields = ('login', 'email', 'is_staff')
    readonly_fields = ('last_login', 'date_joined')
    fieldsets = (
        (None, {'fields': ('login', 'email', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )



admin.site.register(Article)

admin.site.register(CustomUser,CUAdmin)
