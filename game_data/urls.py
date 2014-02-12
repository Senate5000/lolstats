from django.conf.urls import *


urlpatterns = patterns('',
    (r'update_champions', 'game_data.views.championUpdate'),
    (r'update_items', 'game_data.views.itemUpdate'),
    
)