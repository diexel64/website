# Generated by Django 5.0.3 on 2024-04-01 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='language',
        ),
        migrations.AddField(
            model_name='profile',
            name='fecharegistro',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='profile',
            name='suscripcion',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
