# Generated by Django 4.0.6 on 2024-05-31 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surprise', '0003_remove_message_id_alter_message_day_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='upload',
            field=models.ImageField(upload_to='images'),
        ),
    ]
