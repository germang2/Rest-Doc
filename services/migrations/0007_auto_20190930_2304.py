# Generated by Django 2.2.3 on 2019-10-01 04:04

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20190930_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='json_data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True),
        ),
    ]