# Generated by Django 2.2.7 on 2020-04-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0015_auto_20200215_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.CharField(default=1586058513, max_length=50),
        ),
        migrations.AlterField(
            model_name='dynamics',
            name='text',
            field=models.TextField(blank=True, max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='dynamics',
            name='time',
            field=models.CharField(default=1586058513, max_length=50),
        ),
    ]
