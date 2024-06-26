# Generated by Django 5.0.4 on 2024-04-21 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Goal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goalTitle', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Not_Started', 'Not started'), ('In_Progress', 'In progress'), ('Done', 'Done')], default='Not started', max_length=20)),
                ('type', models.CharField(choices=[('Study', 'Study'), ('Work', 'Work'), ('Other', 'Other')], default='Other', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestModel.account')),
            ],
        ),
        migrations.CreateModel(
            name='Subgoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subgoalTitle', models.CharField(max_length=100)),
                ('timelineDate', models.CharField(max_length=100)),
                ('timelineTime', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subgoals', to='TestModel.goal')),
            ],
        ),
    ]
