# Generated by Django 4.2.2 on 2023-08-29 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0010_rename_colledtionskipped_collectionskipped'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectionskipped',
            old_name='CollectionDate',
            new_name='collectionDate',
        ),
        migrations.RenameField(
            model_name='collectionskipped',
            old_name='CollectionId',
            new_name='collectionId',
        ),
        migrations.RenameField(
            model_name='collectionskipped',
            old_name='CollectionTime',
            new_name='collectionTime',
        ),
        migrations.RenameField(
            model_name='collectionskipped',
            old_name='Confirmed',
            new_name='confirmed',
        ),
        migrations.RenameField(
            model_name='collectionskipped',
            old_name='Remark',
            new_name='remark',
        ),
    ]
