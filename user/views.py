from django.contrib.auth import (
    get_user_model,
    login
)
from drf_spectacular.utils import extend_schema
from rest_framework import (
    permissions,
)
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    UpdateAPIView
)
from rest_framework.response import Response

from user.serializers import (
    LoginSerializer,
    RegistrationSerializer,
    UpdatePasswordSerializer
)


USER_MODEL = get_user_model()


class RegistrationView(CreateAPIView):
    """ Регистрация пользователя. """
    model = USER_MODEL
    serializer_class = RegistrationSerializer


class LoginView(GenericAPIView):
    """ User login. """
    serializer_class = LoginSerializer

    @extend_schema(
        description="User login",
        summary="User login"
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(serializer.data)


class UpdatePasswordView(UpdateAPIView):
    """ Обновление пароля. """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    @extend_schema(
        description="Update user",
        summary="Update"
    )
    def get_object(self):
        return self.request.user
