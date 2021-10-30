from django.contrib import admin
from api.models import User, Order, Cleaner


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'middlename',)


@admin.register(Cleaner)
class CleanerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number_of_sweeps', 'rating',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'address', 'type', 'square', 'cleaner',)
