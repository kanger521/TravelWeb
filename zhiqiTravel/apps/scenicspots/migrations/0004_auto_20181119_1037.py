# Generated by Django 2.1.2 on 2018-11-19 10:37

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scenicspots', '0003_auto_20181016_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='active',
            name='introduce',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='活动介绍'),
        ),
    ]
