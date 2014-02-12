from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse

from urllib2 import urlopen
from models import champion, item
import json

# Create your views here.

def championUpdate(request):
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
        champ, created = champion.objects.get_or_create(name=champion_name)
        champ.code = i
        print '{0}({1})'.format(champion_name, i)
        champ.armorperlevel = champion_json['data'][champion_name]['stats']['armorperlevel']
        champ.attackdamage = champion_json['data'][champion_name]['stats']['attackdamage']
        champ.mpperlevel = champion_json['data'][champion_name]['stats']['mpperlevel']
        champ.attackspeedoffset = champion_json['data'][champion_name]['stats']['attackspeedoffset']
        champ.mp = champion_json['data'][champion_name]['stats']['mp']
        champ.armor = champion_json['data'][champion_name]['stats']['armor']
        champ.hp = champion_json['data'][champion_name]['stats']['hp']
        champ.hpregenperlevel = champion_json['data'][champion_name]['stats']['hpregenperlevel']
        champ.attackspeedperlevel = champion_json['data'][champion_name]['stats']['attackspeedperlevel']
        champ.attackrange = champion_json['data'][champion_name]['stats']['attackrange']
        champ.movespeed = champion_json['data'][champion_name]['stats']['movespeed']
        champ.attackdamageperlevel = champion_json['data'][champion_name]['stats']['attackdamageperlevel']
        champ.mpregenperlevel = champion_json['data'][champion_name]['stats']['mpregenperlevel']
        champ.critperlevel = champion_json['data'][champion_name]['stats']['critperlevel']
        champ.spellblockperlevel = champion_json['data'][champion_name]['stats']['spellblockperlevel']
        champ.crit = champion_json['data'][champion_name]['stats']['crit']
        champ.mpregen = champion_json['data'][champion_name]['stats']['mpregen']
        champ.spellblock = champion_json['data'][champion_name]['stats']['spellblock']
        champ.hpregen = champion_json['data'][champion_name]['stats']['hpregen']
        champ.hpperlevel = champion_json['data'][champion_name]['stats']['hpperlevel']

        # for k, v in champion_json['data'][champion_name]['stats'].iteritems():
        #     champ.k = v
            # print '\t{0}: {1}'.format(k, v)
        champ.save()

    return HttpResponse(json.dumps('champions updating'), content_type='application/json')


def itemUpdate(request):
    base_url = 'https://prod.api.pvp.net'
    region = 'na'
    api_url = '/api/lol/static-data/{0}/v1/item'.format(region)
    locale = 'en_US'
    itemListData = 'all'
    api_key = ''
    formatted_url = '{0}{1}?locale={2}&itemListData={3}&api_key={4}'.format(base_url, api_url, locale, itemListData, api_key)
    print formatted_url
    json_file = urlopen(formatted_url)
    item_json = json.load(json_file)

    for i in item_json['data']:
        itemObj, created = item.objects.get_or_create(itemId=i)
        itemObj.name = item_json['data'][i]['name']
        itemObj.description = item_json['data'][i]['description']
        try:
            itemObj.plaintext = item_json['data'][i]['plaintext']
        except Exception, e:
            print 'no plaintext'
        try:
            itemObj.into = item_json['data'][i]['into']
        except:
            print "item doesn't build into anything"
        try:
            itemObj.tags = item_json['data'][i]['tags']
        except Exception, e:
            print 'no tags'
        itemObj.total_cost = item_json['data'][i]['gold']['total']
        itemObj.purchasable = item_json['data'][i]['gold']['purchasable']
        itemObj.sell_cost = item_json['data'][i]['gold']['sell']
        itemObj.base_cost = item_json['data'][i]['gold']['base']
        try:
            # loops through stats and uses setattr to update the appropriate model fields
            for stat in item_json['data'][i]['stats']:
                print stat
                print '{0}: {1}'.format(stat, item_json['data'][i]['stats'][stat])
                setattr(itemObj, stat, item_json['data'][i]['stats'][stat])
        except Exception, e:
            print '{0} - no stats ?'.format(i)
        itemObj.save()

    return HttpResponse(json.dumps('updating items'), content_type='application/json')