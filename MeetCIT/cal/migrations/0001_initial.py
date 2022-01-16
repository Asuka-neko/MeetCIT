# Generated by Django 4.0.1 on 2022-01-16 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor', models.CharField(max_length=200)),
                ('mentee', models.CharField(max_length=200)),
                ('zoom_link', models.TextField()),
                ('start_time', models.DateTimeField(verbose_name='start time')),
                ('end_time', models.DateTimeField(verbose_name='end time')),
                ('available', models.BooleanField(default=True)),
            ],
            options={
                'permissions': (('can_edit', 'Can edit the event'), ('cannot_book', 'Cannot book the event')),
            },
        ),
    ]
