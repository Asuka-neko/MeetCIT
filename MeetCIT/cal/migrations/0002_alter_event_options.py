# Generated by Django 4.0.1 on 2022-01-15 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'permissions': (('can_edit', 'Can edit the event'),)},
        ),
    ]