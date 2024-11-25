from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Gestor personalizado para el modelo de usuario."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('El email es obligatorio.'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError(_('Superusuario debe tener is_staff=True.'))
        if not extra_fields.get('is_superuser'):
            raise ValueError(_('Superusuario debe tener is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Modelo de usuario personalizado."""
    
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=150)
    age = models.PositiveIntegerField(_('age'), blank=True, default=0)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Enviar un email al usuario."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
