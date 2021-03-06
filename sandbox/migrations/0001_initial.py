# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-18 21:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'managed': False,
                'db_table': 'django_migrations',
            },
        ),
        migrations.CreateModel(
            name='Games',
            fields=[
                ('gameid', models.TextField(db_column='GameID', primary_key=True, serialize=False)),
                ('hometeampoints', models.SmallIntegerField(blank=True, db_column='HomeTeamPoints', null=True)),
                ('visitorteampoints', models.SmallIntegerField(blank=True, db_column='VisitorTeamPoints', null=True)),
                ('result', models.SmallIntegerField(blank=True, db_column='Result', null=True)),
                ('week', models.SmallIntegerField(db_column='Week')),
                ('date', models.DateField(db_column='Date')),
            ],
            options={
                'managed': False,
                'db_table': 'Games',
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('sportsid', models.IntegerField(blank=True, db_column='SportsID', null=True, unique=True)),
                ('name', models.TextField(db_column='Name')),
                ('sportsname', models.TextField(blank=True, db_column='SportsName', null=True)),
                ('position', models.TextField(blank=True, db_column='Position', null=True)),
                ('price', models.SmallIntegerField(blank=True, db_column='Price', null=True)),
                ('points', models.SmallIntegerField(blank=True, db_column='Points', null=True)),
                ('played', models.SmallIntegerField(db_column='Played')),
                ('totalppg', models.FloatField(db_column='TotalPPG')),
                ('last5ppg', models.FloatField(db_column='Last5PPG')),
                ('number', models.CharField(blank=True, db_column='Number', max_length=2, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fantasypoints', models.SmallIntegerField(blank=True, db_column='FantasyPoints', null=True)),
                ('points', models.SmallIntegerField(db_column='Points')),
                ('assists', models.SmallIntegerField(db_column='Assists')),
                ('steals', models.SmallIntegerField(db_column='Steals')),
                ('rebounds', models.SmallIntegerField(db_column='Rebounds')),
                ('blocks', models.SmallIntegerField(db_column='Blocks')),
                ('ftm', models.SmallIntegerField(db_column='FTM')),
                ('fta', models.SmallIntegerField(db_column='FTA')),
                ('fgm', models.SmallIntegerField(db_column='FGM')),
                ('fga', models.SmallIntegerField(db_column='FGA')),
                ('turnovers', models.SmallIntegerField(db_column='Turnovers')),
                ('fouls', models.SmallIntegerField(db_column='Fouls')),
                ('date', models.DateField(db_column='Date')),
                ('dnp', models.BooleanField(db_column='DNP')),
                ('minutes', models.TextField(db_column='Minutes')),
            ],
            options={
                'managed': False,
                'db_table': 'Stats',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('sportsid', models.IntegerField(db_column='SportsID', unique=True)),
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
                ('sportsname', models.TextField(db_column='SportsName')),
                ('shortname', models.CharField(db_column='ShortName', max_length=3)),
            ],
            options={
                'managed': False,
                'db_table': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Usersstats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_column='Date')),
                ('week', models.IntegerField(db_column='Week')),
                ('points', models.IntegerField(db_column='Points')),
                ('players', models.IntegerField(db_column='Players')),
                ('dnp', models.IntegerField(db_column='DNP')),
                ('ppp', models.FloatField(db_column='PPP')),
                ('roster', models.TextField(blank=True, db_column='Roster', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'UsersStats',
            },
        ),
        migrations.CreateModel(
            name='Usersteams',
            fields=[
                ('teamid', models.IntegerField(db_column='TeamID', primary_key=True, serialize=False)),
                ('teamname', models.TextField(db_column='TeamName')),
                ('username', models.TextField(db_column='UserName')),
                ('points', models.IntegerField(db_column='Points')),
                ('rosterpath', models.TextField(db_column='RosterPath')),
                ('teampath', models.TextField(blank=True, db_column='TeamPath', null=True)),
                ('position', models.IntegerField(db_column='Position')),
                ('transfers', models.IntegerField(db_column='Transfers')),
            ],
            options={
                'managed': False,
                'db_table': 'UsersTeams',
            },
        ),
        migrations.CreateModel(
            name='Usersweekstats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(db_column='Points')),
                ('position', models.IntegerField(db_column='Position')),
                ('week', models.IntegerField(db_column='Week')),
                ('games', models.IntegerField(db_column='Games')),
                ('dnp', models.IntegerField(db_column='DNP')),
                ('left', models.IntegerField(db_column='Left')),
            ],
            options={
                'managed': False,
                'db_table': 'UsersWeekStats',
            },
        ),
    ]
