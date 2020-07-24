from django.db import models
import datetime 
from django.contrib.auth.models import User

class Scan(models.Model):
    scan_type = models.IntegerField(default=0)
    raw_text = models.CharField(max_length=200)
    blob_id = models.IntegerField(default=0)
    blob_url = models.CharField(max_length=200)
    nice_filename = models.CharField(max_length=200)
    nice_path = models.CharField(max_length=200)
    local_path = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(default=datetime.datetime.now)

class EventLog(models.Model):
    event_type = models.IntegerField(default=0)
    event_subtype = models.IntegerField(default=0)
    event_details = models.CharField(max_length=2048)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(default=datetime.datetime.now)

class Tag(models.Model):
    tag_type = models.IntegerField(default=0)
    tag_de = models.CharField(max_length=200)
    tag_en = models.CharField(max_length=200)
    tag_fr = models.CharField(max_length=200)
    tag_es = models.CharField(max_length=200)
    tag_it = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.datetime.now)
