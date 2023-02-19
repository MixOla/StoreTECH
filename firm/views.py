from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination

from firm.permissions import ActiveUsers

from firm.filter import FirmFilter
from firm.models import Firm
from firm.serializers import FirmSerializer


# class FirmViewSet(viewsets.ModelViewSet):
#     queryset = Firm.objects.all()
#     filter_backends = (DjangoFilterBackend,)
#     filterset_class = FirmFilter
#     permission_classes = ActiveUsers
#
#     serializer_class = FirmSerializer


class FirmCreateView(CreateAPIView):
    model = Firm
    permission_classes = [permissions.IsAuthenticated, ActiveUsers]
    serializer_class = FirmSerializer


class FirmListView(ListAPIView):
    """Класс получения списка организаций."""
    model = Firm
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FirmSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    search_fields = ['name']
    filterset_class = FirmFilter


class FirmView(RetrieveUpdateDestroyAPIView):
    """Класс обновления/удаления организаций."""
    model = Firm
    serializer_class = FirmSerializer
    permission_classes = [permissions.IsAuthenticated, ActiveUsers]
    http_method_names = ['put', 'post', 'get', 'delete']


