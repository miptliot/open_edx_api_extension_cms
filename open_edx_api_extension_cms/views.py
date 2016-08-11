import logging
from contentstore.views.course import _create_or_rerun_course
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from openedx.core.lib.api.permissions import ApiKeyHeaderPermission
from student.models import CourseAccessRole
from student.roles import CourseCreatorRole

log = logging.getLogger(__name__)


@csrf_exempt
@api_view(['POST'])
@permission_classes([ApiKeyHeaderPermission])
def create_or_rerun_course(request):
    course_creators = CourseAccessRole.objects.filter(role=CourseCreatorRole.ROLE)
    if course_creators.exists():
        request.user = course_creators[0].user
    return _create_or_rerun_course(request)
