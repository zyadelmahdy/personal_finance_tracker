# Generated by Django 5.2.2 on 2025-06-12 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance_tracker_app', '0002_alter_transaction_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance_tracker_app.method'),
        ),
    ]
