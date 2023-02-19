from django.urls import path

from user import views


urlpatterns = [
    path('signup', views.RegistrationView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('update_password', views.UpdatePasswordView.as_view(), name='update_password'),
]