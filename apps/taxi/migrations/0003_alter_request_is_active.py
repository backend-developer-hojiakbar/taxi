# Generated by Django 5.0.6 on 2024-11-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
