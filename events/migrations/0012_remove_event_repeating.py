# Generated by Django 3.2.16 on 2022-10-28 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_alter_event_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='repeating',
        ),
    ]
