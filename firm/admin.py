from django.contrib import admin

from firm.models import *

from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from firm.models import Firm, Product


class FirmAdmin(admin.ModelAdmin):
    """
    Настройка админ-панели для работы с моделями приложения firm
    """
    list_display = ('name', 'level', 'debt', 'provider_link')
    list_filter = ('city',)
    fieldsets = [
        (None, {'fields': ['level', 'name', 'debt', 'provider']}),
        ('Contacts', {'fields': ['email', 'country', 'city', 'street', 'building_number']}),
        ('Employee', {'fields': ['employee']}),
    ]

    def provider_link(self, obj):
        """
        Реализация ссылки на поставщика
        """
        if obj.provider:
            url = reverse(
                'admin:firm_firm_change',
                args=(obj.provider.id, )
            )

            return mark_safe(u'<a href="{0}">{1}</a>'.format(url, obj.provider))

    actions = ['DebtZero']

    @admin.action(description='Списать задолженность')
    def DebtZero(self, request, queryset):
        """
        Action - списание задолженности
        """
        queryset.update(debt=0)


admin.site.register(Firm, FirmAdmin)
admin.site.register(Product)
