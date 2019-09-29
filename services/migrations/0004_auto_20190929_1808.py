# Generated by Django 2.2.3 on 2019-09-29 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20190929_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verb', models.CharField(max_length=12)),
                ('description', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='headers',
            field=models.ManyToManyField(to='services.Header'),
        ),
        migrations.AddField(
            model_name='service',
            name='method',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='services.Method'),
            preserve_default=False,
        ),
    ]
