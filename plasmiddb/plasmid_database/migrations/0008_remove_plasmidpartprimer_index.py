# Generated by Django 3.0.7 on 2021-05-20 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plasmid_database', '0007_auto_20210520_0341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plasmidpartprimer',
            name='index',
        ),
    ]