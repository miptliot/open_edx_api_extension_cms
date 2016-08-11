from django.conf.urls import url
from django.conf import settings

from open_edx_api_extension_cms import views


urlpatterns = [
    url(r'^create_or_rerun_course/$', views.create_or_rerun_course),
]
