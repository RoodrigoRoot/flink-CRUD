# Generated by Django 3.1.5 on 2021-02-23 04:21

import django.contrib.postgres.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('auto_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('symbol', models.CharField(max_length=10, verbose_name='Symbol')),
                ('market_values', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companines',
            },
        ),
    ]