# Generated by Django 2.2.5 on 2019-11-28 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_dynamicspicture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dynamics',
            name='picture',
        ),
    ]
