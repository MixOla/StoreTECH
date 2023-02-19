from django.urls import path
from firm import views


urlpatterns = [
    path('firm/create', views.FirmCreateView.as_view(), name='firm_create'),
    path('firm/list', views.FirmListView.as_view(), name='firm_list'),
    path('firm/<pk>', views.FirmView.as_view(), name='firm_pk'),
]