# Generated by Django 2.2.3 on 2019-11-26 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('province', '0005_province_poem_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='poem_content',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
