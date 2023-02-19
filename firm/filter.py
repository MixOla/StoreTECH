import django_filters

from firm.models import Firm


class FirmFilter(django_filters.FilterSet):
    """
    Фильтр по полю город
    """
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Firm
        fields = ['city', ]

