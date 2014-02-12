import json

challenger_json = open('challengers.json')
players = json.load(challenger_json)

total_players = 0

for player in players['entries']:
    print player['playerOrTeamName']
    total_players += 1

print 'Total Players = {0}'.format(total_players)