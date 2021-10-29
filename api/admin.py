from django.contrib import admin
from api.models import User, Order


class UserAdmin(admin.ModelAdmin):
    list_display = {'id', 'surname', 'name', 'middlename'}


admin.site.register(User)
admin.site.register(Order)
