from rest_framework import serializers
from .models import User, Order, BasicService, ExtraService, DiscountCode, Cleaner, TypeOfCleaning, Frequency, \
    CleaningTime, CleanerCalendar


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class BasicServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicService
        fields = '__all__'


class ExtraServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraService
        fields = '__all__'


class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = '__all__'


class CleanerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cleaner
        fields = '__all__'


class TypeOfCleaningSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfCleaning
        fields = '__all__'


class FrequencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Frequency
        fields = '__all__'


class CleaningTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningTime
        fields = '__all__'


class CleanerCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleanerCalendar
        fields = '__all__'
