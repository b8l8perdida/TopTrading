#dwitter/urls.py

from django.contrib import admin
from django.urls import path
from dwitter.views import create_item, dashboard, my_items, profile_list, profile, register
from django.urls import include, re_path

app_name = "dwitter"

urlpatterns = [
    re_path("^admin/", admin.site.urls),
    re_path(r"^accounts/", include("django.contrib.auth.urls")),
    re_path(r"^dashboard/", dashboard, name="dashboard"),
    re_path(r"^register/", register, name="register"),
    re_path(r"^profile_list/", profile_list, name="profile_list"),
    re_path(r"^profile/(?P<pk>[0-9]+)", profile, name="profile"),
    re_path(r"^my_items/(?P<pk>[0-9]+)", my_items, name="my_items"),
    re_path(r"^create_item/", create_item, name="create_item"),
]
