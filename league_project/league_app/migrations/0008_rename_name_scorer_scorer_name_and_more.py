# Generated by Django 5.0.3 on 2024-03-08 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('league_app', '0007_alter_scorer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scorer',
            old_name='name',
            new_name='scorer_name',
        ),
        migrations.RenameField(
            model_name='scorer',
            old_name='team',
            new_name='scorer_team',
        ),
    ]