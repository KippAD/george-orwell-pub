# Generated by Django 3.2.16 on 2022-10-11 13:32

import cloudinary.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('description', models.TextField(blank=True)),
                ('time', models.TimeField()),
                ('date', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('repeating', models.BooleanField(default=False)),
                ('capacity', models.IntegerField(validators=[django.core.validators.MaxValueValidator(64), django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
