# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'matchInfo'
        db.create_table(u'player_stats_matchinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('totalDamageDealtToChampions', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('goldEarned', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item0', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item3', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item4', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item5', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('item6', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('wardPlaced', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('totalDamageTaken', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('trueDamageDealtPlayer', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('physicalDamageDealtPlayer', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('trueDamageDealtToChampions', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('visionWardsBought', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('killingSprees', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('totalUnitsHealed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('neutralMinionsKilledYourJungle', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('magicDamageDealtToChampions', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('magicDamageDealtPlayer', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('neutralMinionsKilledEnemyJungle', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('assists', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('magicDamageTaken', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('numDeaths', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('totalTimeCrowdControlDealt', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('largestMultiKill', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('physicalDamageTaken', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('win', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('team', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('totalDamageDealt', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('largestKillingSpree', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('totalHeal', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('minionsKilled', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('timePlayed', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('physicalDamageDealtToChampions', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('championsKilled', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('trueDamageTaken', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('neutralMinionsKilled', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('goldSpent', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gameId', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('spell1', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('teamId', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('spell2', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('gameMode', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('mapId', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('subType', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('championId', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('createDate', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'player_stats', ['matchInfo'])


    def backwards(self, orm):
        # Deleting model 'matchInfo'
        db.delete_table(u'player_stats_matchinfo')


    models = {
        u'player_stats.matchinfo': {
            'Meta': {'object_name': 'matchInfo'},
            'assists': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'championId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'championsKilled': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'createDate': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gameId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'gameMode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'goldEarned': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'goldSpent': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item0': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item3': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item4': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item5': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'item6': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'killingSprees': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'largestKillingSpree': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'largestMultiKill': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'magicDamageDealtPlayer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'magicDamageDealtToChampions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'magicDamageTaken': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mapId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'minionsKilled': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'neutralMinionsKilled': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'neutralMinionsKilledEnemyJungle': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'neutralMinionsKilledYourJungle': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'numDeaths': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'physicalDamageDealtPlayer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'physicalDamageDealtToChampions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'physicalDamageTaken': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'spell1': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'spell2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'subType': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'teamId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timePlayed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'totalDamageDealt': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'totalDamageDealtToChampions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'totalDamageTaken': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'totalHeal': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'totalTimeCrowdControlDealt': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'totalUnitsHealed': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trueDamageDealtPlayer': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trueDamageDealtToChampions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'trueDamageTaken': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'visionWardsBought': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wardPlaced': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'win': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'player_stats.player': {
            'Meta': {'object_name': 'player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isFreshBlood': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'isHotStreak': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'isInactive': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'isVeteran': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'leagueName': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'leaguePoints': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'player_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profileIconId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'queueType': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rank': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'summonerLevel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'wins': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['player_stats']