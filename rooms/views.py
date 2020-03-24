from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Appointment, StaffMember


# Create your views here.
def index(request):
    latest_appointments_list = Appointment.objects.order_by('-start_time')[:10]
    context = {'latest_appointments_list': latest_appointments_list}
    return render(request, 'rooms/index.html', context)


def detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'rooms/detail.html',
                  {'appointment': appointment,
                   'jitsi_base_url': settings.JITSI_BASE_URL})


def print_pdf(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'rooms/print.html',
                  {'appointment': appointment,
                   'jitsi_base_url': settings.JITSI_BASE_URL})


def new(request):
    return render(
        request, 'rooms/new.html',
        {'staffmembers': [{'id': m.id, 'name': m.name}
                          for m in StaffMember.objects.all()]})
