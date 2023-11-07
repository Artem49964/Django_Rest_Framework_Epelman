from django.urls import path

from .views import (
    AdminToUserView,
    AvatarView,
    BlockAdminView,
    BlockUserView,
    SendEmailView,
    UnblockAdminView,
    UnblockUserView,
    UserCreateListView,
)

urlpatterns = [
    path('', UserCreateListView.as_view()),
    path('/admin_to_user/<int:pk>', AdminToUserView.as_view()),
    path('/avatar', AvatarView.as_view()),
    path('/block_user/<int:pk>', BlockUserView.as_view()),
    path('/unblock_user/<int:pk>', UnblockUserView.as_view()),
    path('/block_admin/<int:pk>', BlockAdminView.as_view()),
    path('/unblock_admin/<int:pk>', UnblockAdminView.as_view()),
    path('/send_email', SendEmailView.as_view()),

]
