import logging
from contentstore.views.course import _create_or_rerun_course
from django.core.exceptions import PermissionDenied
import json

from opaque_keys.edx.keys import CourseKey
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from openedx.core.lib.api.permissions import ApiKeyHeaderPermission
from django.contrib.auth import get_user_model
from openedx.core.djangoapps.models.course_details import CourseDetails
from xmodule.modulestore.django import modulestore
from util.json_request import JsonResponse
from contentstore.utils import reverse_course_url

log = logging.getLogger(__name__)

User = get_user_model()


@csrf_exempt
@api_view(['POST'])
@permission_classes([ApiKeyHeaderPermission])
def create_or_rerun_course(request):
    global_stuff = User.objects.filter(is_staff=True).first()
    if global_stuff is not None:
        request.user = global_stuff
    else:
        raise PermissionDenied()
    response = _create_or_rerun_course(request)
    if response.status_code >= 400:
        return response
    course_key_string = json.loads(response.content).get("course_key")
    if course_key_string is not None:
        course_key = CourseKey.from_string(course_key_string)
    else:
        course_key = modulestore().make_course_key(request.json["org"], request.json["number"], request.json["run"])
    CourseDetails.update_from_json(course_key, request.json, global_stuff)
    return JsonResponse({
        'url': reverse_course_url('course_handler', course_key),
        'course_key': unicode(course_key),
    })
