# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Torrent.folder'
        db.add_column(u'bay_torrent', 'folder',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=1024),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Torrent.folder'
        db.delete_column(u'bay_torrent', 'folder')


    models = {
        u'bay.file': {
            'Meta': {'object_name': 'File'},
            'extension': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'torrent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bay.Torrent']"}),
            'wanted': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'bay.torrent': {
            'Meta': {'object_name': 'Torrent'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'folder': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infohash': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'leechers': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'seeders': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'uploaded': ('django.db.models.fields.DateTimeField', [], {}),
            'uploader': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        u'bay.word': {
            'Meta': {'object_name': 'Word'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'word': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['bay']