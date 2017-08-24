from django.db import models
from block.models import Block
from django.contrib.auth.models import User

class Activatecode(models.Model):
    user = models.CharField("用户名",max_length=100)
    new_code = models.CharField("激活码", max_length=100)
    expire_timestamp = models.DateTimeField("过期时间")

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "激活码"
        verbose_name_plural = "激活码"
