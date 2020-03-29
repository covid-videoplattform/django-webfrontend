from django import forms
from rooms.models import Appointment, StaffMember
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.translation import gettext_lazy as _


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['name', 'description', 'start_time', 'end_time', 'staffmember', 'room_name']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'test3', 'cols': 20, 'rows': 20}),
            'start_time': forms.DateTimeInput(),
            'end_time': forms.DateTimeInput(),
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
