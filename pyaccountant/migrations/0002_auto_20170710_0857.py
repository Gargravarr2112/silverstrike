# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 08:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyaccountant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pyaccountant.AccountType'),
        ),
        migrations.AlterField(
            model_name='account',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pyaccountant.Currency'),
        ),
        migrations.AlterField(
            model_name='account',
            name='internal_type',
            field=models.IntegerField(choices=[(1, 'Personal'), (2, 'Revenue'), (3, 'Expense')], default=1),
        ),
    ]