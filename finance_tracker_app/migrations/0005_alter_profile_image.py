# Generated by Django 5.2.2 on 2025-06-15 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_tracker_app', '0004_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
