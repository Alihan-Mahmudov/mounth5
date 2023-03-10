from django.contrib.auth.models import User
from django.db import models


class ConfirmCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='confirm_code')
    code = models.CharField(max_length=6, blank=True)