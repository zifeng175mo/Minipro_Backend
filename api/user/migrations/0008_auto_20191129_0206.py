# Generated by Django 2.2.5 on 2019-11-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20191129_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamics',
            name='time',
            field=models.CharField(default=1574964407, max_length=50),
        ),
    ]
