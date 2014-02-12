from urllib2 import urlopen
import json

# base_url = 'https://prod.api.pvp.net'
# region = 'na'
# api_url = '/api/lol/static-data/{0}/v1/champion'.format(region)
# locale = 'en_US'
# champData = 'all'
# api_key = ''
# formatted_url = '{0}{1}?locale={2}&champData={3}&api_key={4}'.format(base_url, api_url, locale, champData, api_key)
# print formatted_url
json_file = open('item.json')
item_json = json.load(json_file)

for i in item_json['data']:
    try:
        print '{0}: {1}'.format(i, item_json['data'][i]['stats'])
    except Exception, e:
        print '{0} - no stats ?'.format(i)
