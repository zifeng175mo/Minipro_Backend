from datetime import datetime

from django.db import models

# Create your models here.
from province.models import Province


class User(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    address = models.TextField(max_length=128, blank=True, null=True)
    avatar = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name if self.name else 'None'


class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True, null=True)
    achieved = models.BooleanField(default=False)

    class Meta:
        verbose_name = '成就'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name if self.name else 'None'


class Dynamics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now)
    text = models.TextField(max_length=400, blank=True, null=True)
    picture = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user.name) + '的动态'


class Gone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    gone = models.BooleanField(default=False)

    class Meta:
        verbose_name = '去过'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user.name) + '去过' + str(self.province.name)
