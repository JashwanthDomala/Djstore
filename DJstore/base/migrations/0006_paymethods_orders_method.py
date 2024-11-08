# Generated by Django 5.1.2 on 2024-11-06 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_orders_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayMethods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='method',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.paymethods'),
        ),
    ]
