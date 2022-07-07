from django.contrib import admin
from api.models import User, Order, Cleaner, ExtraService, DiscountCode, TypeOfCleaning, Frequency


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'middle_name', 'email',)


@admin.register(Cleaner)
class CleanerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number_of_sweeps', 'rating',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'address', 'type', 'square', 'cleaner',)


@admin.register(ExtraService)
class ExtraServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_per_meter',)


@admin.register(TypeOfCleaning)
class TypeOfCleaningAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_per_meter',)


@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code', 'is_active',)
