# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-05-11 17:01


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_remove_prize_nulls_pt2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='usepaypalsandbox',
        ),
    ]