from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='scoreboard'),
    url(r'^scoreboard', views.post_list, name='scoreboard'),
    url(r'^injuries', views.injuries_list, name='injuries'),
    url(r'^support', views.injuries_list, name='support'),
    url(r'^schedule', views.injuries_list, name='schedule'),
    url(r'^standings', views.injuries_list, name='standings'),
]

