from django.conf import settings
from django.db.models import Count
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


from .models import Appointment, StaffMember


class AppointmentIndexView(ListView):
    template_name = 'appointments/index.html'
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activate'] = 'appointments'
        context['page_title'] = 'Lits of Appointments'
        return context


class AppointmentDetailView(DetailView):
    model = Appointment
    template_name = 'appointments/detail.html'

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


class AppointmentPrintPDFView(DetailView):
    model = Appointment
    template_name = 'appointments/print.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jitsi_base_url'] = settings.JITSI_BASE_URL
        return context


class AppointmentCreate(CreateView):
    model = Appointment
    template_name = 'appointments/appointment_form.html'
    fields = ['name', 'description', 'start_time', 'end_time', 'staffmember',
              'room_name']


class StaffIndexView(ListView):
    template_name = 'staff/index.html'
    context_object_name = 'latest_staff_members_list'
    staff_members = StaffMember.objects.annotate(Count('appointment'))

    def get_queryset(self):
        return StaffMember.objects.order_by('-name')[:10]

    def head(self, *args, **kwargs):
        last_modified_staff = self.get_queryset().latest('-last_modified')
        response = HttpResponse()
        # RFC 1123 date format
        response['Last-Modified'] = last_modified_staff.last_modified.strftime(
            '%a, %d %b %Y %H:%M:%S GMT')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['activate'] = 'staff'
        context['page_title'] = 'Lits of Staff Members'
        return context


class StaffDetailView(DetailView):
    model = StaffMember
    template_name = 'staff/detail.html'

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


class StaffPrintPDFView(DetailView):
    model = Appointment
    template_name = 'staff/print.html'

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


class StaffCreate(CreateView):
    model = StaffMember
    template_name = 'staff/staff_member_form.html'
    fields = ['name', 'email']
