from django.dispatch.dispatcher import receiver
from xmodule.modulestore.django import SignalHandler, modulestore
try:
    from edx_proctoring.models import ProctoredCourse, ProctoredCourseProctoringService
except ImportError:
    ProctoredCourse = None
    ProctoredCourseProctoringService = None


def _set_proctored_course_details(edx_course, proctored_course=None):
    created = False
    if proctored_course:
        proctored_course.set_fields_from_edx_course(edx_course)
        proctored_course.save()
    else:
        created = True
        proctored_course = ProctoredCourse.create_new_from_edx_course(edx_course)

    return created, proctored_course


@receiver(SignalHandler.course_published)
def update_course_proctoring_services_handler(sender, course_key, **kwargs):  # pylint: disable=unused-argument
    """
    Save proctoring services for the course to the special table.
    """
    if not ProctoredCourse:
        return

    edx_course = modulestore().get_course(course_key)
    services_list_to_save = [service.strip() for service in edx_course.available_proctoring_services.split(',')
                             if service.strip()]
    services_list_to_save = list(set(services_list_to_save))

    proctored_course = None

    try:
        proctored_course = ProctoredCourse.objects.get(edx_id=unicode(course_key))
    except ProctoredCourse.DoesNotExist:
        pass

    if not services_list_to_save:
        if proctored_course:
            ProctoredCourseProctoringService.objects.filter(course=proctored_course).delete()
            proctored_course.delete()
    else:
        created, proctored_course = _set_proctored_course_details(edx_course,
                                                                  None if not proctored_course else proctored_course)
        existing_proctoring_services = []
        if not created:
            existing_proctoring_services = [s.name for s in
                                            ProctoredCourseProctoringService.objects.filter(course=proctored_course)]
            remove_list = [s for s in existing_proctoring_services if s not in services_list_to_save]
            if remove_list:
                ProctoredCourseProctoringService.objects.filter(course=proctored_course, name__in=remove_list).delete()

        for service_to_add in services_list_to_save:
            if service_to_add not in existing_proctoring_services:
                new_service = ProctoredCourseProctoringService(
                    course=proctored_course,
                    name=service_to_add)
                new_service.save()
