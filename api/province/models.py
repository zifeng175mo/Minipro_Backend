from django.db import models


# Create your models here.
class Province(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        verbose_name = '省份'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name if self.name else 'None'
