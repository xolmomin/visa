# Generated by Django 3.1.2 on 2020-10-24 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201024_1204'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='puser',
            options={'verbose_name': 'Ariza topshirganlar', 'verbose_name_plural': 'Ariza topshirganlar'},
        ),
        migrations.AlterModelOptions(
            name='winner',
            options={'verbose_name': "Go'liblar", 'verbose_name_plural': "Go'liblar"},
        ),
    ]
