from django.db import models


class User(models.Model):
    name = models.CharField(max_length=45, verbose_name="Имя")
    surname = models.CharField(max_length=45, verbose_name="Фамилия")
    middlename = models.CharField(max_length=45, verbose_name="Отчество")
    phone_number = models.CharField(max_length=45, verbose_name="Номер телефона")
    email = models.CharField(max_length=45, verbose_name="Почта")

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.surname} {self.name} {self.middlename}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Cleaner(models.Model):
    name = models.CharField(max_length=45)
    number_of_sweeps = models.IntegerField(default=0)
    rating = models.FloatField()
    phone_number = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Уборщик"
        verbose_name_plural = "Уборщики"


class Order(models.Model):
    class Type(models.TextChoices):
        EASY = '1', "Лёгкая уборка"
        SUPPORT = ' 2', "Поддерживающая уборка"
        GENERAL = '3', "Генеральная уборка"
        AFTER_REPAIR = '4', "Уборка после ремонта"

    class Frequency(models.TextChoices):
        ONCE = '1', "Разовая"
        ONCE_EVERY_TWO_WEEK = '2', "Раз в две недели"
        ONCE_A_WEEK = ' 3', "Раз в неделю"
        ONCE_A_MONTH = '4', "Раз в месяц"

    address = models.CharField(max_length=255, verbose_name="Адрес")
    date = models.DateField(verbose_name="Дата начала")
    time = models.CharField(max_length=45, verbose_name="Примерное время")
    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.EASY,
        verbose_name="Тип"
    )
    frequency = models.CharField(
        max_length=2,
        choices=Frequency.choices,
        default=Frequency.ONCE,
        verbose_name="Площадь квартиры"
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

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Заказ на {self.address} {self.date}'

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
