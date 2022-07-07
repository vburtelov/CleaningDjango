from rest_framework import viewsets

from api.models import Order, ExtraService, BasicService, Cleaner, TypeOfCleaning, Frequency, CleaningTime, \
    CleanerCalendar
from api.serializers import OrderSerializer, OrderSerializerCreate, ExtraServiceSerializer, BasicServiceSerializer, \
    CleanerSerializer, TypeOfCleaningSerializer, FrequencySerializer, CleaningTimeSerializer, CleanerCalendarSerializer


class CleanerCalendarViewSet(viewsets.ModelViewSet):
    queryset = CleanerCalendar.objects.all()
    serializer_class = CleanerCalendarSerializer
    http_method_names = ['get']


class CleaningTimeViewSet(viewsets.ModelViewSet):
    queryset = CleaningTime.objects.all()
    serializer_class = CleaningTimeSerializer
    http_method_names = ['get']


class FrequencyViewSet(viewsets.ModelViewSet):
    queryset = Frequency.objects.all()
    serializer_class = FrequencySerializer
    http_method_names = ['get']


class TypeOfCleaningViewSet(viewsets.ModelViewSet):
    queryset = TypeOfCleaning.objects.all()
    serializer_class = TypeOfCleaningSerializer
    http_method_names = ['get']


class CleanerViewSet(viewsets.ModelViewSet):
    queryset = Cleaner.objects.all()
    serializer_class = CleanerSerializer
    http_method_names = ['get']


class ExtraServiceViewSet(viewsets.ModelViewSet):
    queryset = ExtraService.objects.all()
    serializer_class = ExtraServiceSerializer
    http_method_names = ['get']


class BasicServiceViewSet(viewsets.ModelViewSet):
    queryset = BasicService.objects.all()
    serializer_class = BasicServiceSerializer
    http_method_names = ['get']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.request.method == 'POST':
            serializer_class = OrderSerializerCreate
        return serializer_class
