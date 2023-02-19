from django.db import models

class Product(models.Model):
    product_name = models.CharField(verbose_name='Название продукта', max_length=100, unique=True)
    product_model = models.CharField(verbose_name='Модель', max_length=100)
    release_date = models.DateField(
        verbose_name='Дата выхода на рынок',
        auto_now=False,
        auto_now_add=False
    )

    class Meta:
        verbose_name = 'Название продукта'
        verbose_name_plural = 'Название продукта'

    def __str__(self):
        return self.product_name


class Firm(models.Model):
    TYPES = (
        (0, 'Завод'),
        (1, 'Дистрибьютор'),
        (2, 'Оптовый склад'),
        (3, 'Розничная сеть'),
        (4, 'Индивидуальный предприниматель')
    )
    name = models.CharField(verbose_name='Название организации', max_length=100, unique=True)
    email = models.EmailField(verbose_name="Почта", max_length=100, unique=True)
    country = models.CharField(verbose_name='Страна', max_length=50)
    city = models.CharField(verbose_name='Город', max_length=50)
    street = models.CharField(verbose_name='Улица', max_length=50)
    building_number = models.CharField(verbose_name='Номер дома', max_length=10)
    product = models.ManyToManyField(Product, related_name='firm')
    level = models.SmallIntegerField(
        verbose_name='Тип организации',
        choices=TYPES)
    provider = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='Поставщик',
        related_name='traders',
        null=True,
        blank=True,
    )
    debt = models.DecimalField(
        max_digits=20,
        decimal_places=2,
        verbose_name='Задолженность',
        default=0
    )
    employee = models.ForeignKey('user.User', verbose_name='Сотрудник', on_delete=models.PROTECT)
    release_date = models.DateField(verbose_name='Дата выхода на рынок', auto_now_add=True)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name
