# Generated by Django 5.0.3 on 2024-04-19 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_rating_user_valoracion_delete_comment_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='valoracion',
            options={'ordering': ('creado',)},
        ),
        migrations.RenameField(
            model_name='valoracion',
            old_name='timestamp',
            new_name='creado',
        ),
        migrations.AddField(
            model_name='valoracion',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='valoracion',
            name='editado',
            field=models.DateTimeField(auto_now=True),
        ),
    ]