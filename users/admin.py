from django.contrib import admin
from users.models import CustomUser, CustomGroup
from django.contrib.auth.models import Group


admin.site.unregister(Group)


@admin.register(CustomGroup)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email', 'is_superuser',)
    ordering = ('email',)
