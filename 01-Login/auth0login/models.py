from django.db import models


class Scan(models.Model):
    scan_type = models.IntegerField(default=0)
    raw_text = models.CharField(max_length=200)
    blob_id = models.IntegerField(default=0)
    blob_url = models.CharField(max_length=200)
    nice_filename = models.CharField(max_length=200)
    nice_path = models.CharField(max_length=200)
    local_path = models.CharField(max_length=200)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
