from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('rut', 'username', 'email', 'phone_number')
    ordering = ('rut',)
    search_fields = ('rut',)
    #list_editable = ('username', 'email', 'phone_number')
    list_display_links = ('rut', 'username')
    #list_filter = ('is_staff', 'is_superuser', 'is_active')
    list_per_page = 10 
    exclude = ('rut','password', 'groups', 'user_permissions')


# admin.site.register(CustomUser)
# admin.site.register(CustomUser, CustomUserAdmin)