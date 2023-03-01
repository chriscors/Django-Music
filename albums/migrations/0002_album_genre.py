# Generated by Django 4.1.7 on 2023-03-01 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('ROCK', 'Rock'), ('ALT', 'Alternative'), ('POP', 'Pop'), ('RAP', 'Hip-Hop/Rap'), ('COUNTRY', 'Country')], default='---------', max_length=8),
        ),
    ]
