# Generated by Django 5.1.6 on 2025-02-18 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='usuarios/avatar/'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nascimento',
            field=models.DateField(default=datetime.date(2025, 2, 18)),
            preserve_default=False,
        ),
    ]
