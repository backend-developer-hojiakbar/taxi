# Generated by Django 5.0.6 on 2024-12-01 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0005_advertisement_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='car',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
