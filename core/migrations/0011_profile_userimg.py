# Generated by Django 5.0.3 on 2024-04-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_valoracion_valoracion'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='userimg',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]
