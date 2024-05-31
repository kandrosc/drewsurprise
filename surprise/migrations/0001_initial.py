# Generated by Django 4.0.6 on 2024-05-31 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('1', 'June 2nd'), ('2', 'June 6th'), ('3', 'June 10th'), ('4', 'June 14th')], max_length=1)),
                ('content', models.CharField(max_length=10000)),
            ],
        ),
    ]