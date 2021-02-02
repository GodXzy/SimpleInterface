from django.db import models

# Create your models here.
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# AUTH_USER_MODEL


@receiver(post_save, sender=settings.AUTH_PASSWORD_VALIDATORS)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=isinstance)


class Product(models.Model):
    """
    产品表
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="产品名称")
    status = models.CharField(max_length=10, verbose_name="产品状态")  # 0未开始，1已计划，2研发中，3测试中，4已完成
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name='产品描述')
    LastUpdateTime = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=1024, verbose_name='创建人')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品表'
        verbose_name_plural = '产品表'
        db_table = "product"
