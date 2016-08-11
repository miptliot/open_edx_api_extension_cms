from django.conf.urls import url

from open_edx_api_extension_cms import views


urlpatterns = [
    url(r'^course/$', views.create_or_rerun_course),
]
