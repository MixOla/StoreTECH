from django.contrib.auth.models import AbstractUser

from firm.models import Firm


class User(AbstractUser):
    pass

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'