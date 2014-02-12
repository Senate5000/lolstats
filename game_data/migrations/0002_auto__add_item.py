# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'item'
        db.create_table(u'game_data_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tags', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('plaintext', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('total_cost', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('purchasable', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('sell_cost', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('base_cost', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('FlatArmorMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatAttackSpeedMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatBlockMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatCritChanceMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatCritDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatEXPBonus', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatHPPoolMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatHPRegenMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatMPPoolMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatMPRegenMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatMagicDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatMovementSpeedMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatPhysicalDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('FlatSpellBlockMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentArmorMo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentAttackSpeedMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentBlockMo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentCritChanceMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentCritDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentDodgeMo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentEXPBonu', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentHPPoolMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentHPRegenMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentMPPoolMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentMPRegenMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentMagicDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentMovementSpeedMo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentPhysicalDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
            ('PercentSpellBlockMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5, blank=True)),
        ))
        db.send_create_signal(u'game_data', ['item'])


    def backwards(self, orm):
        # Deleting model 'item'
        db.delete_table(u'game_data_item')


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
        },
        u'game_data.item': {
            'FlatArmorMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatAttackSpeedMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatBlockMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatCritChanceMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatCritDamageMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatEXPBonus': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatHPPoolMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatHPRegenMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatMPPoolMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatMPRegenMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatMagicDamageMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatMovementSpeedMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatPhysicalDamageMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'FlatSpellBlockMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'Meta': {'object_name': 'item'},
            'PercentArmorMo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentAttackSpeedMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentBlockMo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentCritChanceMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentCritDamageMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentDodgeMo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentEXPBonu': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentHPPoolMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentHPRegenMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentMPPoolMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentMPRegenMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentMagicDamageMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentMovementSpeedMo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentPhysicalDamageMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'PercentSpellBlockMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'base_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'plaintext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'purchasable': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'sell_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'total_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['game_data']