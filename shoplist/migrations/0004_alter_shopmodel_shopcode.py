# Generated by Django 4.2.2 on 2023-07-03 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoplist', '0003_alter_shopmodel_shopcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopmodel',
            name='shopCode',
            field=models.IntegerField(),
        ),
    ]