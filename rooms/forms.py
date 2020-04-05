import datetime

from django import forms
from rooms.models import Appointment, StaffMember
from django.utils import timezone
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.translation import gettext_lazy as _


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['name', 'description', 'start_time', 'end_time', 'staffmember', 'room_name']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'test3', 'cols': 60, 'rows': 4}),
            'start_time': forms.DateTimeInput(attrs={
                'placeholder': timezone.now().strftime('%Y-%m-%d %H:%M')}),
            'end_time': forms.DateTimeInput(attrs={
                'placeholder': (timezone.now() + datetime.timedelta(minutes=30)).strftime('%Y-%m-%d %H:%M')
                }),
        }


class StaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': _('Firstname Lastname')}),
            'email': forms.DateTimeInput(attrs={
                'placeholder': _('name@example.com')}),
            'phone': PhoneNumberPrefixWidget(attrs={}),
        }
