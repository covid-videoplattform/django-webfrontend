from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Count
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.views.generic.edit import CreateView


from .forms import AppointmentForm, StaffMemberForm
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
        context['page_title'] = _('List of Appointments')
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


class AppointmentPrintView(DetailView):
    model = Appointment
    template_name = 'appointments/print.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jitsi_base_url'] = settings.JITSI_BASE_URL
        return context


class AppointmentCreate(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'appointments/appointment_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('New Appointment')
        return context


class AppointmentDelete(DeleteView):
    model = Appointment
    template_name = 'appointments/appointment_confirm_delete.html'
    success_url = reverse_lazy('rooms:appointment-index')


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
        context['page_title'] = _('List of Staff Members')
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


class StaffPrintView(DetailView):
    model = StaffMember
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
    form_class = StaffMemberForm
    template_name = 'staff/staffmember_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('New Staff Member')
        return context


class StaffMemberDelete(DeleteView):
    model = StaffMember
    template_name = 'staff/staffmember_confirm_delete.html'
    success_url = reverse_lazy('rooms:staff-index')
