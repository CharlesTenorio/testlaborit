# Generated by Django 3.2.6 on 2021-08-09 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lead',
            options={'ordering': ('name',)},
        ),
    ]
