from django.db import models


# Create your models here.
class Province(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    poem_name = models.CharField(max_length=40, blank=True, null=True)
    poem_content = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    translation = models.TextField(blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = '省份'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name if self.name else 'None'

    objects = models.Manager()
