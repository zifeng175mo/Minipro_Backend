# Generated by Django 2.2.5 on 2020-02-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20191215_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(default=1580540191, max_length=50),
        ),
        migrations.AlterField(
            model_name='dynamics',
            name='time',
            field=models.CharField(default=1580540191, max_length=50),
        ),
    ]