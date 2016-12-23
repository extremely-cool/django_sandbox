from django.db import models


class Games(models.Model):
    gameid = models.TextField(db_column='GameID', primary_key=True)
    hometeamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='HomeTeamID',
                                   blank=True, null=True, related_name='hometeam_teams')
    visitorteamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='VisitorTeamID',
                                      blank=True, null=True, related_name='visitorteam_teams')
    hometeampoints = models.SmallIntegerField(db_column='HomeTeamPoints', blank=True, null=True)
    visitorteampoints = models.SmallIntegerField(db_column='VisitorTeamPoints', blank=True, null=True)
    result = models.SmallIntegerField(db_column='Result', blank=True, null=True)
    week = models.SmallIntegerField(db_column='Week')
    date = models.DateField(db_column='Date')

    class Meta:
        managed = False
        db_table = 'Games'

    def home_team_stats(self):
        pass

class Players(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)
    sportsid = models.IntegerField(db_column='SportsID', unique=True, blank=True, null=True)
    name = models.TextField(db_column='Name')
    sportsname = models.TextField(db_column='SportsName', blank=True, null=True)
    position = models.TextField(db_column='Position', blank=True, null=True)
    price = models.SmallIntegerField(db_column='Price', blank=True, null=True)
    teamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='TeamID', blank=True, null=True)
    points = models.SmallIntegerField(db_column='Points', blank=True, null=True)
    played = models.SmallIntegerField(db_column='Played')
    totalppg = models.FloatField(db_column='TotalPPG')
    last5ppg = models.FloatField(db_column='Last5PPG')
    number = models.CharField(db_column='Number', max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Players'


class Stats(models.Model):
    gameid = models.ForeignKey(Games, models.DO_NOTHING, db_column='GameID')
    playerid = models.ForeignKey(Players, models.DO_NOTHING, db_column='PlayerID')
    teamid = models.ForeignKey('Teams', models.DO_NOTHING, db_column='TeamID')
    fantasypoints = models.SmallIntegerField(db_column='FantasyPoints', blank=True, null=True)
    points = models.SmallIntegerField(db_column='Points')
    assists = models.SmallIntegerField(db_column='Assists')
    steals = models.SmallIntegerField(db_column='Steals')
    rebounds = models.SmallIntegerField(db_column='Rebounds')
    blocks = models.SmallIntegerField(db_column='Blocks')
    ftm = models.SmallIntegerField(db_column='FTM')
    fta = models.SmallIntegerField(db_column='FTA')
    fgm = models.SmallIntegerField(db_column='FGM')
    fga = models.SmallIntegerField(db_column='FGA')
    turnovers = models.SmallIntegerField(db_column='Turnovers')
    fouls = models.SmallIntegerField(db_column='Fouls')
    date = models.DateField(db_column='Date')
    dnp = models.BooleanField(db_column='DNP')
    minutes = models.TextField(db_column='Minutes')

    class Meta:
        managed = False
        db_table = 'Stats'
        unique_together = (('gameid', 'playerid'),)


class Teams(models.Model):
    alias = models.TextField(db_column='Alias', null=True)
    sportsid = models.IntegerField(db_column='SportsID', unique=True)
    id = models.IntegerField(db_column='ID', primary_key=True)
    name = models.TextField(db_column='Name')
    sportsname = models.TextField(db_column='SportsName')
    shortname = models.CharField(db_column='ShortName', max_length=3)

    class Meta:
        db_table = 'Teams'

    @property
    def alias(self):
        return self.name.split(' ')[-1]


class Usersstats(models.Model):
    teamid = models.ForeignKey('Usersteams', models.DO_NOTHING, db_column='TeamID')
    date = models.DateField(db_column='Date')
    week = models.IntegerField(db_column='Week')
    points = models.IntegerField(db_column='Points')
    players = models.IntegerField(db_column='Players')
    dnp = models.IntegerField(db_column='DNP')
    ppp = models.FloatField(db_column='PPP')
    roster = models.TextField(db_column='Roster', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'UsersStats'
        unique_together = (('date', 'teamid'),)


class Usersteams(models.Model):
    teamid = models.IntegerField(db_column='TeamID', primary_key=True)
    teamname = models.TextField(db_column='TeamName')
    username = models.TextField(db_column='UserName')
    points = models.IntegerField(db_column='Points')
    rosterpath = models.TextField(db_column='RosterPath')
    teampath = models.TextField(db_column='TeamPath', blank=True, null=True)
    position = models.IntegerField(db_column='Position')
    transfers = models.IntegerField(db_column='Transfers')

    class Meta:
        managed = False
        db_table = 'UsersTeams'


class Usersweekstats(models.Model):
    teamid = models.ForeignKey(Usersteams, models.DO_NOTHING, db_column='TeamID')
    points = models.IntegerField(db_column='Points')
    position = models.IntegerField(db_column='Position')
    week = models.IntegerField(db_column='Week')
    games = models.IntegerField(db_column='Games')
    dnp = models.IntegerField(db_column='DNP')
    left = models.IntegerField(db_column='Left')

    class Meta:
        managed = False
        db_table = 'UsersWeekStats'
        unique_together = (('teamid', 'week'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
