# social/urls.py

from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path, re_path

app_name = "dwitter"


urlpatterns = [
    path('', include(('dwitter.urls', 'dwitter'), namespace='dwitter')),
    re_path("^admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)