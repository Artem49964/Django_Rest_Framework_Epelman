from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from apps.core.permissions.is_admin_or_write_only import IsAdminOrWriteOnlyPermission
from apps.core.permissions.is_superUser import IsSuperUser
from apps.core.services.email_service import EmailService

from .filters import UserFilter
from .models import UserModel as User
from .serializers import AvatarSerializer, UserSerializer

UserModel: User = get_user_model()


class UserCreateListView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all_with_profiles()
    filterset_class = UserFilter
    permission_classes = (IsAdminOrWriteOnlyPermission,)

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)


class AdminToUserView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
        serializer = UserSerializer(user)
        user.save()
        return Response(serializer.data, status.HTTP_200_OK)


class BlockUserView(GenericAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (IsAdminUser,)

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
        serializer = UserSerializer(user)
        user.save()
        return Response(serializer.data, status.HTTP_200_OK)


class UnblockUserView(GenericAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
        serializer = UserSerializer(user)
        user.save()
        return Response(serializer.data, status.HTTP_200_OK)


class BlockAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user: User = self.get_object()
        if user.is_active == True:
            user.is_active = False
        serializer = UserSerializer(user)
        user.save()
        return Response(serializer.data, status.HTTP_200_OK)


class UnblockAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(pk=self.request.user.pk)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
        serializer = UserSerializer(user)
        user.save()
        return Response(serializer.data, status.HTTP_200_OK)


class AvatarView(UpdateAPIView):
    serializer_class = AvatarSerializer
    http_method_names = ('put',)

    def get_object(self):
        return UserModel.objects.all_with_profiles().get(pk=self.request.user.pk).profile

    # def perform_update(self, serializer):
    #     self.get_object().avatar.delete()
    #     super().perform_update(serializer)
        # print(self.get_object())


class SendEmailView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        EmailService.test_email()
        return Response('ok')