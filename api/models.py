from django.db import models


class User(models.Model):
    name = models.CharField(max_length=45, verbose_name="Имя")
    surname = models.CharField(max_length=45, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=45, verbose_name="Отчество")
    phone_number = models.CharField(max_length=45, verbose_name="Номер телефона")
    email = models.CharField(max_length=45, verbose_name="Почта")

    created_time = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f'{self.surname} {self.name} {self.middle_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class ExtraService(models.Model):
    name = models.CharField(max_length=45, verbose_name="Название")
    price_per_meter = models.IntegerField(verbose_name="Цена за квадратный метр")

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

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Уборщик"
        verbose_name_plural = "Уборщики"


# EASY = '1', "Лёгкая уборка"
# SUPPORT = ' 2', "Поддерживающая уборка"
# GENERAL = '3', "Генеральная уборка"
# AFTER_REPAIR = '4', "Уборка после ремонта"
class TypeOfCleaning(models.Model):
    name = models.CharField(max_length=45, verbose_name="Название")
    price_per_meter = models.IntegerField(verbose_name="Цена за квадратный метр")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Тип уборки"
        verbose_name_plural = "Типы уборки"


# ONCE = '1', "Разовая"
# ONCE_EVERY_TWO_WEEK = '2', "Раз в две недели"
# ONCE_A_WEEK = ' 3', "Раз в неделю"
# ONCE_A_MONTH = '4', "Раз в месяц"
class Frequency(models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Частота уборки"
        verbose_name_plural = "Частоты уборок"


class Order(models.Model):
    address = models.CharField(max_length=255, verbose_name="Адрес")
    date = models.DateField(verbose_name="Дата начала")
    time = models.CharField(max_length=45, verbose_name="Примерное время")
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
        User,
        on_delete=models.DO_NOTHING,
        verbose_name="Пользователь"
    )

    discount_code = models.ForeignKey(
        DiscountCode,
        on_delete=models.DO_NOTHING,
        verbose_name="Промокод"
    )

    extra_services = models.ManyToManyField(ExtraService)

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заказ на {self.address} {self.date}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
