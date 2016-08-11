import logging
from contentstore.views.course import _create_or_rerun_course
from rest_framework.decorators import api_view

log = logging.getLogger(__name__)


@api_view
def create_or_rerun_course(request):
    return _create_or_rerun_course(request)
