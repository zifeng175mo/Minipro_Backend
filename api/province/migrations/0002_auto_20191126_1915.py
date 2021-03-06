# Generated by Django 2.2.3 on 2019-11-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('province', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='province',
            options={'verbose_name': '省份', 'verbose_name_plural': '省份'},
        ),
        migrations.AddField(
            model_name='province',
            name='author',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='poem_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='translation',
            field=models.TextField(blank=True, null=True),
        ),
    ]
