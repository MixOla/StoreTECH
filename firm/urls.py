from django.urls import path, include
from rest_framework.routers import SimpleRouter

from firm.views import FirmViewSet

company_router = SimpleRouter()
company_router.register('company', FirmViewSet, basename='firm')

urlpatterns = [
    path('', include(company_router.urls)),
]