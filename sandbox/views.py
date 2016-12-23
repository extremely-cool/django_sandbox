from django.shortcuts import render
from .models import Games, Players, Stats, Teams


def post_list(request):
    games = Games.objects.filter(date='2016-01-10').order_by('gameid')
    return render(request, 'blog/scoreboard.html', {'games': games})


def injuries_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = []
    return render(request, 'blog/injuries.html', {'posts': posts})
