# Generated by Django 4.2 on 2023-04-03 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_video_table_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease_table',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 3, 23, 2, 29, 330260), null=True),
        ),
        migrations.AddField(
            model_name='key_value_table',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 3, 23, 2, 29, 331259), null=True),
        ),
        migrations.AddField(
            model_name='testimonial_table',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 3, 23, 2, 29, 331259), null=True),
        ),
        migrations.AddField(
            model_name='video_table',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 3, 23, 2, 29, 331259), null=True),
        ),
    ]
