# Generated by Django 5.0.6 on 2024-11-25 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxi', '0003_alter_request_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_12', models.BooleanField(default=False)),
                ('is_24', models.BooleanField(default=False)),
                ('is_ping', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
