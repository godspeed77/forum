from django.db import models
from block.models import Block
from article.models import Article
from django.contrib.auth.models import User

class Message(models.Model):
    owner = models.ForeignKey(User,verbose_name="作者")
    content = models.CharField("内容",max_length=10000)
    link = models.CharField("链接",max_length=10000)
    status = models.IntegerField("已读",choices=((0,"未读"),(1,"已读")))

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "消息"
        verbose_name_plural = "消息很多"
