from django.forms import ModelForm, TextInput
from rooms.models import Appointment, StaffMember


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'description',
                  'start_time', 'end_time', 'staffmember', 'room_name']


class StaffMemberForm(ModelForm):
    class Meta:
        model = StaffMember
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Firstname Lastname'}),
            'email': TextInput(attrs={'placeholder': 'name@example.com'}),
            'phone': TextInput(attrs={'placeholder': '0123 456 7890'}),
        }
