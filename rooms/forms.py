from django import forms
from rooms.models import Appointment, StaffMember


class AppointmentForm(forms.ModelForm):
    # i'm trying to customize form fields, but nothing is working:

    # first way
    description = forms.CharField(widget=forms.Textarea(
            attrs={'class': 'test1', 'maxlength': 123, 'rows': 40})),

    # second way
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget = forms.Textarea(
            attrs={'class': 'test2', 'maxlength': 155, 'rows': 4})
    
    class Meta:
        model = Appointment
        fields = ['name', 'description',
                  'start_time', 'end_time', 'staffmember', 'room_name']
        # third way
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'test3', 'cols': 20, 'rows': 20}),
        }


class StaffMemberForm(forms.ModelForm):
    class Meta:
        model = StaffMember
        fields = ['name', 'email', 'phone']
