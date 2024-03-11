# Generated by Django 5.0.3 on 2024-03-10 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league_app', '0016_alter_fixture_date_alter_fixture_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('team_name', models.CharField(max_length=100)),
                ('matches_played', models.CharField(max_length=100)),
                ('matches_won', models.IntegerField()),
                ('matches_drawn', models.IntegerField()),
                ('matches_lost', models.IntegerField()),
                ('goals_for', models.IntegerField()),
                ('goals_against', models.IntegerField()),
            ],
        ),
    ]
