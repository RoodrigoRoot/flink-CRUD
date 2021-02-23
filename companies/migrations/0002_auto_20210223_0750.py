# Generated by Django 3.1.5 on 2021-02-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterField(
            model_name='company',
            name='symbol',
            field=models.CharField(max_length=10, unique=True, verbose_name='Symbol'),
        ),
    ]
