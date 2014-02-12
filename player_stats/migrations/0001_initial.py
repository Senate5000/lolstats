# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'player'
        db.create_table(u'player_stats_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('profileIconId', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('summonerLevel', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('isHotStreak', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('isFreshBlood', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('leagueName', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('isVeteran', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('tier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('leaguePoints', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('rank', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('isInactive', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('queueType', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('wins', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'player_stats', ['player'])


    def backwards(self, orm):
        # Deleting model 'player'
        db.delete_table(u'player_stats_player')


    models = {
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