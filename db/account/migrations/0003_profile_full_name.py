# Generated by Django 4.0.5 on 2022-06-12 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_subscription_subscriber'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]