from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'scans', views.ScanViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'eventlogs', views.EventLogViewSet)

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('upload', views.simple_upload),
    path('logout', views.logout),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
    path('api/', include(router.urls)),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
