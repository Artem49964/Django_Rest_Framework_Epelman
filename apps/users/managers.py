from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_kwargs):
        if not email:
            raise ValueError('Email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, email, password, **extra_kwargs):
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_active', True)
        extra_kwargs.setdefault('is_superuser', True)

        if not extra_kwargs['is_staff']:
            raise ValueError('Super user must be is_staff')

        if not extra_kwargs['is_superuser']:
            raise ValueError('Super user must be is_superuser')

        user = self.create_user(email, password, **extra_kwargs)
        return user

    def create_with_profile(self):
        return self.select_related('profile')

    def all_with_profiles(self):
        return self.select_related('profile')
