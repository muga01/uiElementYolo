# Generated by Django 4.0 on 2021-12-28 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uielementdetectorapi', '0003_detections_delete_hero'),
    ]

    operations = [
        migrations.AddField(
            model_name='detections',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]
