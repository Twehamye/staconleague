# Generated by Django 5.0.3 on 2024-03-08 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league_app', '0005_scorer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scorer',
            old_name='week',
            new_name='num_goals',
        ),
    ]
