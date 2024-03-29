# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-23 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Id', models.IntegerField()),
                ('Product_Name', models.CharField(max_length=100)),
                ('Product_cost', models.IntegerField()),
                ('Product_color', models.CharField(max_length=100)),
                ('Product_class', models.CharField(max_length=100)),
                ('Customer_Name', models.CharField(max_length=100)),
                ('Customer_Mobile', models.BigIntegerField()),
                ('Customer_Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
