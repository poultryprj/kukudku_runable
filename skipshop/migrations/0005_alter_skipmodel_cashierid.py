# Generated by Django 4.2.2 on 2023-07-04 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skipshop', '0004_skipmodel_routeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skipmodel',
            name='cashierId',
            field=models.CharField(max_length=100),
        ),
    ]
