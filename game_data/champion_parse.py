from urllib2 import urlopen
from models import champion
import json

base_url = 'https://prod.api.pvp.net'
region = 'na'
api_url = '/api/lol/static-data/{0}/v1/champion'.format(region)
locale = 'en_US'
champData = 'all'
api_key = ''
formatted_url = '{0}{1}?locale={2}&champData={3}&api_key={4}'.format(base_url, api_url, locale, champData, api_key)
print formatted_url
json_file = urlopen(formatted_url)
champion_json = json.load(json_file)

for i in champion_json['keys']:
    champion_name = champion_json['keys'][i]
    champion = champion.objects.get_or_create(name=champion_name)
    champion.code = i
    print '{0}({1})'.format(champion_name, i)
    for k, v in champion_json['data'][champion_name]['stats'].iteritems():
        print '\t{0}: {1}'.format(k, v)
