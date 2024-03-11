# Generated by Django 5.0.3 on 2024-03-09 05:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('league_app', '0008_rename_name_scorer_scorer_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scorer',
            name='scorer_name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scored_at', models.DateTimeField(auto_now_add=True)),
                ('num_goals', models.IntegerField()),
                ('match_detail', models.CharField(max_length=100)),
                ('scorer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='league_app.player')),
            ],
        ),
    ]