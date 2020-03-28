import datetime

from django.test import TestCase
from django.utils import timezone
from ..forms import AppointmentForm, StaffMemberForm


class TestAppointmentForm(TestCase):

    def test_valid_form(self):
        in_the_future = timezone.now() + datetime.timedelta(days=30)
        data = {'name': 'a simple name',
                'description': 'lorem ipsum dolor sit amet',
                'start_time': timezone.now(),
                'end_time': in_the_future,
                'staffmember': None,
                'room_name': 'test-room'}
        form = AppointmentForm(data=data)
        self.assertTrue(form.is_valid())
