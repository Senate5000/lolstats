from django.conf.urls import *


urlpatterns = patterns('',
    (r'update_players', 'player_stats.views.updatePlayers'),
    (r'query_test', 'player_stats.views.queryTest'),
    
)