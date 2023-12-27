from django.contrib import admin

from users.models import User


@admin.register(User)
class UsersListAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'email',
        'first_name',
        'last_name',
        'middle_name',
        'organization',
        'phone',
        'country',
        'city',
        'is_staff',
        'is_superuser'
    )
    list_filter = ('organization', 'country', 'city', 'is_superuser', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name', 'organization',)
