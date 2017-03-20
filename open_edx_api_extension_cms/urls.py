from django.conf.urls import url

from open_edx_api_extension_cms import views


urlpatterns = [
    url(r'^course/$', views.create_or_update_course),
    url(r'^course-check/$', views.check_course_exists),
]
