from django.contrib.auth.models import User
from .models import Scan, Tag, EventLog
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']

class ScanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scan
        fields = ['id', 'scan_type', 'raw_text', 'blob_id', 'blob_url', 'nice_filename', 'nice_path', 'local_path', 'user']

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag_type', 'tag_de', 'tag_en', 'tag_fr', 'tag_es', 'tag_it']

class EventLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLog
        fields = ['id', 'event_type', 'event_subtype', 'event_details', 'user']
