# Generated by Django 4.2.4 on 2023-08-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0015_alter_collectioninfo_collectionid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectioninfo',
            name='collectionId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]