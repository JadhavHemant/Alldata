# Generated by Django 3.2 on 2021-07-21 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0004_alter_companymodel_addreess'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companymodel',
            old_name='addreess',
            new_name='address',
        ),
    ]