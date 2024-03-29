# Generated by Django 5.0.3 on 2024-03-09 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league_app', '0012_alter_goal_date_alter_team_class_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('team_home', models.CharField(max_length=100)),
                ('team_away', models.CharField(max_length=100)),
                ('team_home_score', models.IntegerField()),
                ('team_away_score', models.IntegerField()),
                ('team_home_points', models.IntegerField()),
                ('team_away_points', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='team',
            name='class_year',
            field=models.IntegerField(),
        ),
    ]
