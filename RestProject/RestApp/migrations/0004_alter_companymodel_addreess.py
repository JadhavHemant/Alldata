# Generated by Django 3.2 on 2021-07-21 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestApp', '0003_rename_comapnymodel_companymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companymodel',
            name='addreess',
            field=models.CharField(max_length=100),
        ),
    ]
