from django.contrib.auth.models import User
from .models import Scan
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ScanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scan
        fields = ['scan_type', 'raw_text', 'blob_id', 'blob_url', 'nice_filename', 'nice_path', 'local_path', 'user']
