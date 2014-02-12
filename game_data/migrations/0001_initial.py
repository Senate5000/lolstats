# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'champion'
        db.create_table(u'game_data_champion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('armorperlevel', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('attackdamage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('mpperlevel', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('attackspeedoffset', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('mp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('armor', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('hp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('hpregenperlevel', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('attackspeedperlevel', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('attackrange', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('movespeed', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('attackdamageperlevel', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('mpregenperlevel', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('critperlevel', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('spellblockperlevel', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('crit', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('mpregen', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('spellblock', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('hpregen', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('hpperlevel', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
        ))
        db.send_create_signal(u'game_data', ['champion'])


    def backwards(self, orm):
        # Deleting model 'champion'
        db.delete_table(u'game_data_champion')


    models = {
        u'game_data.champion': {
            'Meta': {'object_name': 'champion'},
            'armor': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'armorperlevel': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'attackdamage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'attackdamageperlevel': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'attackrange': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'attackspeedoffset': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'attackspeedperlevel': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'code': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'crit': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'critperlevel': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'hp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'hpperlevel': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'hpregen': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'hpregenperlevel': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movespeed': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'mp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'mpperlevel': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'mpregen': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'mpregenperlevel': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'spellblock': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'spellblockperlevel': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'})
        }
    }

    complete_apps = ['game_data']