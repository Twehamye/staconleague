# Generated by Django 5.0.3 on 2024-03-09 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league_app', '0014_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='points_got',
            field=models.IntegerField(default=0),
        ),
    ]
