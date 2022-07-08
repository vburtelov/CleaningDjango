from rest_framework import serializers

from users.serializers import CustomUserSerializer
from .models import Order, BasicService, ExtraService, DiscountCode, Cleaner, TypeOfCleaning, Frequency, \
    CleaningTime, CleanerCalendar


class ExtraServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraService
        fields = '__all__'


class BasicServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicService
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
    basic_services = BasicServiceSerializer()
    extra_services = ExtraServiceSerializer()

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


class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    time = CleaningTimeSerializer()
    type = TypeOfCleaningSerializer()
    frequency = FrequencySerializer()
    cleaner = CleanerSerializer()
    user = CustomUserSerializer()
    discount_code = DiscountCodeSerializer()
    extra_services = ExtraServiceSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'
