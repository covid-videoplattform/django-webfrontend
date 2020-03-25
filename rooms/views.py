from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


from .models import Appointment, StaffMember


class IndexView(ListView):
    template_name = 'rooms/index.html'
    context_object_name = 'latest_appointments_list'

    def get_queryset(self):
        return Appointment.objects.order_by('-start_time')[:10]

    def head(self, *args, **kwargs):
        last_appointment = self.get_queryset().latest('-last_modified')
        response = HttpResponse()
        # RFC 1123 date format
        response['Last-Modified'] = last_appointment.last_modified.strftime(
            '%a, %d %b %Y %H:%M:%S GMT')
        return response


class DetailView(DetailView):
    model = Appointment
    template_name = 'rooms/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jitsi_base_url'] = settings.JITSI_BASE_URL
        return context

    def head(self, *args, **kwargs):
        response = HttpResponse()
        # RFC 1123 date format
        response['Last-Modified'] = self.model.last_modified.strftime(
            '%a, %d %b %Y %H:%M:%S GMT')
        return response


class PrintPDFView(DetailView):
    model = Appointment
    template_name = 'rooms/print.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jitsi_base_url'] = settings.JITSI_BASE_URL
        return context


class AppointmentCreate(CreateView):
    model = Appointment
    fields = ['name', 'description', 'start_time', 'end_time', 'staffmember',
              'room_name']
