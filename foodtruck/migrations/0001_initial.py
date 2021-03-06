# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-08-02 19:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Give your Truck a Nice Name', max_length=250)),
                ('website', models.CharField(blank=True, max_length=250, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=15, null=True)),
                ('emails', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
