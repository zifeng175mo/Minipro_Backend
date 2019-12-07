import time

from django.db import models

# Create your models here.
from province.models import Province


class User(models.Model):
    openid = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    address = models.TextField(max_length=128, blank=True, null=True)
    avatar = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name if self.name else 'None'

    objects = models.Manager()


class Dynamics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.CharField(max_length=50, default=int(time.time()))
    text = models.TextField(max_length=400, blank=True, null=True)
    like = models.IntegerField(default=0)

    class Meta:
        verbose_name = '动态'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user.name) + '的动态'

    objects = models.Manager()


class DynamicsPicture(models.Model):
    dynamics = models.ForeignKey(Dynamics, on_delete=models.CASCADE)
    img = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        verbose_name = '动态图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '动态图片'

    objects = models.Manager()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dynamics = models.ForeignKey(Dynamics, on_delete=models.CASCADE)
    reply = models.CharField(max_length=30, blank=True, null=True)
    text = models.TextField(blank=False, null=False)
    time = models.CharField(max_length=50, default=int(time.time()))

    class Meta:
        verbose_name = '动态评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.name + '的评论'

    objects = models.Manager()


class Gone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    gone = models.BooleanField(default=False)

    class Meta:
        verbose_name = '去过'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.user.name) + '去过' + str(self.province.name)


class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True, null=True)
    achieved = models.BooleanField(default=False)

    class Meta:
        verbose_name = '成就'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name if self.name else 'None'
