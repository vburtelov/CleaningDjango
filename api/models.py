import datetime

from django.conf import settings
from django.db import models


class BasicService(models.Model):
    name = models.CharField(max_length=45, verbose_name="Название")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Базовая услуга"
        verbose_name_plural = "Базовые услуги"


class ExtraService(models.Model):
    name = models.CharField(max_length=45, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена", default=0)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Дополнительная услуга"
        verbose_name_plural = "Дополнительные услуги"


class DiscountCode(models.Model):
    name = models.CharField(max_length=45, verbose_name="Название")
    code = models.CharField(max_length=45, verbose_name="Промокод")
    number_of_uses = models.IntegerField(default=0, verbose_name="Количество использований")
    is_active = models.BooleanField(default=False, verbose_name="Активный")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Промокод"
        verbose_name_plural = "Промокоды"


class Cleaner(models.Model):
    name = models.CharField(max_length=45, verbose_name="Имя")
    number_of_sweeps = models.IntegerField(default=0, verbose_name="Количество уборок")
    rating = models.FloatField(verbose_name="Рейтинг")
    phone_number = models.CharField(max_length=45, verbose_name="Номер телефона")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Уборщик"
        verbose_name_plural = "Уборщики"


class TypeOfCleaning(models.Model):
    name = models.CharField(max_length=45, verbose_name="Название")
    price_per_meter = models.IntegerField(verbose_name="Цена за квадратный метр")
    basic_services = models.ManyToManyField(BasicService, verbose_name="Доступные базовые услуги")
    extra_services = models.ManyToManyField(ExtraService, verbose_name="Доступные дополнительные услуги")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Тип уборки"
        verbose_name_plural = "Типы уборки"


class Frequency(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Частота уборки"
        verbose_name_plural = "Частоты уборок"


class CleaningTime(models.Model):
    time = models.TimeField(verbose_name="Время уборки")

    def __str__(self):
        return f'{self.time}'

    class Meta:
        verbose_name = "Время уборок"
        verbose_name_plural = "Времена уборок"


class Order(models.Model):
    address = models.CharField(max_length=255, verbose_name="Адрес")
    date = models.DateField(verbose_name="Дата уборки")
    time = models.ForeignKey(
        CleaningTime,
        on_delete=models.DO_NOTHING,
        verbose_name="Время уборки"

    )
    type = models.ForeignKey(
        TypeOfCleaning,
        on_delete=models.DO_NOTHING,
        verbose_name="Тип уборки"
    )
    frequency = models.ForeignKey(
        Frequency,
        on_delete=models.DO_NOTHING,
        verbose_name="Частота уборки"
    )
    square = models.IntegerField(verbose_name="Площадь уборки")

    cleaner = models.ForeignKey(
        Cleaner,
        on_delete=models.DO_NOTHING,
        verbose_name="Уборщик"
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        verbose_name="Пользователь"
    )

    discount_code = models.ForeignKey(
        DiscountCode,
        on_delete=models.DO_NOTHING,
        verbose_name="Промокод",
        null=True,
        blank=True
    )

    is_active = models.BooleanField(verbose_name="Активен", default=True)

    extra_services = models.ManyToManyField(ExtraService, blank=True, verbose_name="Дополнительные услуги")

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заказ на {self.address} {self.date}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class CleanerCalendar(models.Model):
    cleaner = models.ForeignKey(
        Cleaner,
        on_delete=models.DO_NOTHING,
        verbose_name="Уборщик"
    )
    date = models.DateField(verbose_name="Дата уборки", default=datetime.date.today)

    time = models.ForeignKey(
        CleaningTime,
        on_delete=models.DO_NOTHING,
        verbose_name="Время уборки"
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        verbose_name="Заказ"

    )

    def __str__(self):
        return f'{self.cleaner} {self.date} {self.time} {self.order}'

    class Meta:
        verbose_name = "Календарь уборок"
        verbose_name_plural = "Календари уборок"
