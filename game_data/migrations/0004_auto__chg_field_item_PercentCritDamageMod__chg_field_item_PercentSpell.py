# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'item.PercentCritDamageMod'
        db.alter_column(u'game_data_item', 'PercentCritDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentSpellBlockMod'
        db.alter_column(u'game_data_item', 'PercentSpellBlockMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentHPRegenMod'
        db.alter_column(u'game_data_item', 'PercentHPRegenMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatSpellBlockMod'
        db.alter_column(u'game_data_item', 'FlatSpellBlockMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatCritDamageMod'
        db.alter_column(u'game_data_item', 'FlatCritDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatMPPoolMod'
        db.alter_column(u'game_data_item', 'FlatMPPoolMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatMovementSpeedMod'
        db.alter_column(u'game_data_item', 'FlatMovementSpeedMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentAttackSpeedMod'
        db.alter_column(u'game_data_item', 'PercentAttackSpeedMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentArmorMo'
        db.alter_column(u'game_data_item', 'PercentArmorMo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentMagicDamageMod'
        db.alter_column(u'game_data_item', 'PercentMagicDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatMPRegenMod'
        db.alter_column(u'game_data_item', 'FlatMPRegenMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatAttackSpeedMod'
        db.alter_column(u'game_data_item', 'FlatAttackSpeedMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatArmorMod'
        db.alter_column(u'game_data_item', 'FlatArmorMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatHPRegenMod'
        db.alter_column(u'game_data_item', 'FlatHPRegenMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatBlockMod'
        db.alter_column(u'game_data_item', 'FlatBlockMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentMPPoolMod'
        db.alter_column(u'game_data_item', 'PercentMPPoolMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatMagicDamageMod'
        db.alter_column(u'game_data_item', 'FlatMagicDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentMPRegenMod'
        db.alter_column(u'game_data_item', 'PercentMPRegenMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentPhysicalDamageMod'
        db.alter_column(u'game_data_item', 'PercentPhysicalDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentEXPBonu'
        db.alter_column(u'game_data_item', 'PercentEXPBonu', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatPhysicalDamageMod'
        db.alter_column(u'game_data_item', 'FlatPhysicalDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentHPPoolMod'
        db.alter_column(u'game_data_item', 'PercentHPPoolMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentCritChanceMod'
        db.alter_column(u'game_data_item', 'PercentCritChanceMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentBlockMo'
        db.alter_column(u'game_data_item', 'PercentBlockMo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentDodgeMo'
        db.alter_column(u'game_data_item', 'PercentDodgeMo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatEXPBonus'
        db.alter_column(u'game_data_item', 'FlatEXPBonus', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatHPPoolMod'
        db.alter_column(u'game_data_item', 'FlatHPPoolMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.FlatCritChanceMod'
        db.alter_column(u'game_data_item', 'FlatCritChanceMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

        # Changing field 'item.PercentMovementSpeedMo'
        db.alter_column(u'game_data_item', 'PercentMovementSpeedMo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=5))

    def backwards(self, orm):

        # Changing field 'item.PercentCritDamageMod'
        db.alter_column(u'game_data_item', 'PercentCritDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentSpellBlockMod'
        db.alter_column(u'game_data_item', 'PercentSpellBlockMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentHPRegenMod'
        db.alter_column(u'game_data_item', 'PercentHPRegenMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatSpellBlockMod'
        db.alter_column(u'game_data_item', 'FlatSpellBlockMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatCritDamageMod'
        db.alter_column(u'game_data_item', 'FlatCritDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatMPPoolMod'
        db.alter_column(u'game_data_item', 'FlatMPPoolMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatMovementSpeedMod'
        db.alter_column(u'game_data_item', 'FlatMovementSpeedMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentAttackSpeedMod'
        db.alter_column(u'game_data_item', 'PercentAttackSpeedMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentArmorMo'
        db.alter_column(u'game_data_item', 'PercentArmorMo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentMagicDamageMod'
        db.alter_column(u'game_data_item', 'PercentMagicDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatMPRegenMod'
        db.alter_column(u'game_data_item', 'FlatMPRegenMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatAttackSpeedMod'
        db.alter_column(u'game_data_item', 'FlatAttackSpeedMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatArmorMod'
        db.alter_column(u'game_data_item', 'FlatArmorMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatHPRegenMod'
        db.alter_column(u'game_data_item', 'FlatHPRegenMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatBlockMod'
        db.alter_column(u'game_data_item', 'FlatBlockMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentMPPoolMod'
        db.alter_column(u'game_data_item', 'PercentMPPoolMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatMagicDamageMod'
        db.alter_column(u'game_data_item', 'FlatMagicDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentMPRegenMod'
        db.alter_column(u'game_data_item', 'PercentMPRegenMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentPhysicalDamageMod'
        db.alter_column(u'game_data_item', 'PercentPhysicalDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentEXPBonu'
        db.alter_column(u'game_data_item', 'PercentEXPBonu', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatPhysicalDamageMod'
        db.alter_column(u'game_data_item', 'FlatPhysicalDamageMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentHPPoolMod'
        db.alter_column(u'game_data_item', 'PercentHPPoolMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentCritChanceMod'
        db.alter_column(u'game_data_item', 'PercentCritChanceMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentBlockMo'
        db.alter_column(u'game_data_item', 'PercentBlockMo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentDodgeMo'
        db.alter_column(u'game_data_item', 'PercentDodgeMo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatEXPBonus'
        db.alter_column(u'game_data_item', 'FlatEXPBonus', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatHPPoolMod'
        db.alter_column(u'game_data_item', 'FlatHPPoolMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.FlatCritChanceMod'
        db.alter_column(u'game_data_item', 'FlatCritChanceMod', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

        # Changing field 'item.PercentMovementSpeedMo'
        db.alter_column(u'game_data_item', 'PercentMovementSpeedMo', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=8, decimal_places=5))

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
            'FlatArmorMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatAttackSpeedMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatBlockMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatCritChanceMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatCritDamageMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatEXPBonus': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatHPPoolMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatHPRegenMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatMPPoolMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatMPRegenMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatMagicDamageMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatMovementSpeedMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatPhysicalDamageMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'FlatSpellBlockMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'Meta': {'object_name': 'item'},
            'PercentArmorMo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentAttackSpeedMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentBlockMo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentCritChanceMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentCritDamageMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentDodgeMo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentEXPBonu': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentHPPoolMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentHPRegenMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentMPPoolMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentMPRegenMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentMagicDamageMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentMovementSpeedMo': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentPhysicalDamageMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'PercentSpellBlockMod': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '5', 'blank': 'True'}),
            'base_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemId': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'plaintext': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'purchasable': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'sell_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'total_cost': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['game_data']