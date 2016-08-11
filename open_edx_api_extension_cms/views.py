import logging
from contentstore.views.course import _create_or_rerun_course
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from openedx.core.lib.api.permissions import ApiKeyHeaderPermission
from django.contrib.auth import get_user_model

log = logging.getLogger(__name__)

User = get_user_model()


@csrf_exempt
@api_view(['POST'])
@permission_classes([ApiKeyHeaderPermission])
def create_or_rerun_course(request):
    global_stuff = User.objects.filter(is_staff=True)
    if global_stuff.exists():
        request.user = global_stuff[0]
    return _create_or_rerun_course(request)
