# Generated by Django 2.2.3 on 2019-09-29 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20190929_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='responses',
        ),
        migrations.AddField(
            model_name='response',
            name='service',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='services.Service'),
            preserve_default=False,
        ),
    ]
