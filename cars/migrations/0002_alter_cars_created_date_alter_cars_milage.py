# Generated by Django 4.0 on 2023-05-24 12:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 24, 19, 25, 8, 411269)),
        ),
        migrations.AlterField(
            model_name='cars',
            name='milage',
            field=models.IntegerField(),
        ),
    ]
