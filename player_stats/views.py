from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse

from urllib2 import urlopen
from models import player
import json

# Create your views here.

def updatePlayers(request):
    base_url = 'https://prod.api.pvp.net'
    region = 'na'
    api_url = '/api/lol/{0}/v2.3/league/challenger'.format(region)
    queue_type = 'RANKED_SOLO_5x5'
    api_key = ''
    formatted_url = '{0}{1}?type={2}&api_key={3}'.format(base_url, api_url, queue_type, api_key)
    print formatted_url
    json_file = urlopen(formatted_url)
    players = json.load(json_file)

    for i in players['entries']:
        player_id = i['playerOrTeamId']
        print i['playerOrTeamName']
        new_player, created = player.objects.get_or_create(player_id=player_id)
        new_player.name = i['playerOrTeamName']
        new_player.isHotStreak = i['isHotStreak']
        new_player.isFreshBlood = i['isFreshBlood']
        new_player.leagueName = i['leagueName']
        new_player.isVeteran = i['isVeteran']
        new_player.tier = i['tier']
        new_player.playerOrTeamId = i['playerOrTeamId']
        new_player.leaguePoints = i['leaguePoints']
        new_player.rank = i['rank']
        new_player.isInactive = i['isInactive']
        new_player.queueType = i['queueType']
        new_player.playerOrTeamName = i['playerOrTeamName']
        new_player.wins = i['wins']
        new_player.save()

    return HttpResponse(json.dumps('updating players'), content_type='application/json')


def queryTest(request):
    base_url = 'https://prod.api.pvp.net'
    region = 'na'
    api_url = '/api/lol/{0}/v1.3/summoner'.format(region)
    api_key = ''
    total_players = player.objects.all().count()
    player_count = 0
    for i in range(0, total_players, 40): # incrementing by 40 as the api allows 40 player ID's per request
        temp_list = []
        player_query = player.objects.all()[i:i+40] # gets groups of 40 players
        for x in player_query:
            # create a list of 40 player ID's
            temp_list.append(x.player_id)
            player_count += 1
        temp_list_string = ",".join([str(x) for x in temp_list]) # converts list into a comma separated string without brackets
        formatted_url = '{0}{1}/{2}?api_key={3}'.format(base_url, api_url, temp_list_string, api_key)
        print formatted_url
        json_file = urlopen(formatted_url)
        players = json.load(json_file)
        print players
        for x in players:
            update_player = player.objects.get(player_id=x)
            update_player.profileIconId = players[x]['profileIconId']
            update_player.summonerLevel = players[x]['summonerLevel']
            update_player.save()
        print temp_list
    print 'Total players = {0}'.format(player_count)

    return HttpResponse(json.dumps('doing stuff'), content_type='application/json')
