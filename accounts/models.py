from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """ カスタムユーザーモデル """

    class Meta:
        verbose_name_plural = 'CustomUser'
