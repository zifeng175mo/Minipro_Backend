from django.db import models


# Create your models here.
class Province(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    name_ch = models.CharField(max_length=10, blank=True, null=True)
 
    class Meta:
        verbose_name = '省份'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name if self.name else 'None'

    objects = models.Manager()


class Poem(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    poem_name = models.CharField(max_length=40, blank=True, null=True)
    poem_content = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=20, blank=True, null=True)
    translation = models.TextField(blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = '唐诗'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.province.name_ch + '  ' + self.poem_name if self.poem_name else 'None'

    objects = models.Manager()


class Test(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    question = models.TextField(blank=True, null=False)
    option_A = models.TextField(blank=True, null=False)
    option_B = models.TextField(blank=True, null=False)
    option_C = models.TextField(blank=True, null=False)
    option_D = models.TextField(blank=True, null=False)
    answer = models.CharField(max_length=10, blank=True, null=False)

    class Meta:
        verbose_name = '题目'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.province.name + '的题目'

    objects = models.Manager()
