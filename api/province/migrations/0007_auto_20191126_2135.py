# Generated by Django 2.2.5 on 2019-11-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('province', '0006_auto_20191126_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='poem_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]