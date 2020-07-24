from django.contrib import admin
from .models import Scan, Tag, EventLog

admin.site.register(Scan)
admin.site.register(Tag)
admin.site.register(EventLog)