from .models import Scan, EventLog, Tag
from .serializers import UserSerializer, ScanSerializer, TagSerializer, EventLogSerializer
from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from django.conf import settings
from django.http import HttpResponseRedirect
from urllib.parse import urlencode
from django.core.files.storage import FileSystemStorage
import logging
import subprocess
import json


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect(dashboard)
    else:
        return render(request, 'index.html')


@login_required
def dashboard(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture'],
        'email': auth0user.extra_data['email']
    }

    return render(request, 'dashboard.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })

def logout(request):
    log_out(request)
    return_to = urlencode({'returnTo': request.build_absolute_uri('/')})
    logout_url = 'https://%s/v2/logout?client_id=%s&%s' % \
                 (settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to)
    return HttpResponseRedirect(logout_url)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class ScanViewSet(viewsets.ModelViewSet):
    queryset = Scan.objects.all().order_by('-created_at')
    serializer_class = ScanSerializer
    
class EventLogViewSet(viewsets.ModelViewSet):
    queryset = EventLog.objects.all().order_by('-created_at')
    serializer_class = EventLogSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('-created_at')
    serializer_class = TagSerializer

logger = logging.getLogger(__name__)

@login_required
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        
        if (str(myfile.name).lower().endswith(".pdf")):
            contenttype = "Content-type: application/pdf"
        elif (str(myfile.name).lower().endswith(".jpg")):
            contenttype = "Content-type: image/jpg"
        elif (str(myfile.name).lower().endswith(".jpeg")):
            contenttype = "Content-type: image/jpeg"
        elif (str(myfile.name).lower().endswith(".png")):
            contenttype = "Content-type: image/png"
            
        tika_input = ["curl", "-X", "PUT", "--data-binary", "@"+fs.path(filename), settings.TIKA_URL, "--header", contenttype]
        tika_output = subprocess.check_output(tika_input)
        
        s = Scan(scan_type=1, raw_text=tika_output, blob_id=0, blob_url='',
                 nice_filename=myfile.name, nice_path='', local_path=fs.path(filename),
                 user=request.user)
        s.save()

        return render(request, 'simple_upload.html', {
            'uploaded_file_url': fs.path(filename),
            'tika_output': str(tika_output).replace("\\n", "\n")
        })
    return render(request, 'simple_upload.html')