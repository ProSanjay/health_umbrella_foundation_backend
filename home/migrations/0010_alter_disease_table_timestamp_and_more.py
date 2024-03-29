# Generated by Django 4.1.7 on 2023-04-04 11:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_alter_disease_table_timestamp_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="disease_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 4, 11, 18, 43, 21296)
            ),
        ),
        migrations.AlterField(
            model_name="key_value_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 4, 11, 18, 43, 22141)
            ),
        ),
        migrations.AlterField(
            model_name="testimonial_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 4, 11, 18, 43, 21574)
            ),
        ),
        migrations.AlterField(
            model_name="video_table",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 4, 4, 11, 18, 43, 21833)
            ),
        ),
    ]
