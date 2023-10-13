# Generated by Django 4.2.2 on 2023-08-29 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_roleid_userroles_roleid'),
        ('collection', '0007_alter_collectionmodel_paymentmethod'),
    ]

    operations = [
        migrations.CreateModel(
            name='collectionInfo',
            fields=[
                ('collectionId', models.IntegerField(primary_key=True, serialize=False)),
                ('collectionDate', models.DateField(auto_now=True)),
                ('collectionTime', models.TimeField(auto_now=True)),
                ('collectionMode', models.CharField(max_length=10, null=True)),
                ('collectionAmount', models.PositiveBigIntegerField()),
                ('collectionVerified', models.CharField(max_length=30, null=True)),
                ('collectionConfimed', models.CharField(max_length=30, null=True)),
                ('accountCredited', models.CharField(max_length=10, null=True)),
                ('shopId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='collection.collectionmodel')),
                ('userId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.usermodel')),
            ],
        ),
    ]