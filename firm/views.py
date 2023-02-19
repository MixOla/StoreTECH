from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from firm.permissions import ActiveUsers

from firm.filter import FirmFilter
from firm.models import Firm
from firm.serializers import FirmSerializer


class FirmViewSet(viewsets.ModelViewSet):
    queryset = Firm.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FirmFilter
    permission_classes = ActiveUsers

    serializer_class = FirmSerializer

