# Generated by Django 4.0.5 on 2022-06-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='banned',
            field=models.BooleanField(default=False),
        ),
    ]
