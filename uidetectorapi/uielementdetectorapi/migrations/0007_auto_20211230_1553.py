# Generated by Django 3.2.10 on 2021-12-30 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uielementdetectorapi', '0006_alter_detections_image_to_detect'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detections',
            old_name='codes',
            new_name='code_generated',
        ),
        migrations.RenameField(
            model_name='detections',
            old_name='detectedimage',
            new_name='detected_image_path',
        ),
        migrations.RenameField(
            model_name='detections',
            old_name='jsonfile',
            new_name='json_file',
        ),
        migrations.AlterField(
            model_name='detections',
            name='image_to_detect',
            field=models.ImageField(default='', upload_to='uploads/2021_12_30_15_51_20'),
        ),
    ]