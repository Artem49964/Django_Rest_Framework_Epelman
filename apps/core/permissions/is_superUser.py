
from rest_framework.permissions import IsAdminUser


class IsSuperUser(IsAdminUser):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff and request.user.is_superuser)