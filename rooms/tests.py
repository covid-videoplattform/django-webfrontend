import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from .models import Appointment


# Create your tests here.
class AppointmentModelTests(TestCase):

    def test_invalid_when_end_before_start(self):
        """
        Appointments with end_time before start_time are invalid
        """
        in_the_future = timezone.now() + datetime.timedelta(days=30)
        a = Appointment(name="testappointment",
                        start_time=in_the_future,
                        end_time=timezone.now())
        with self.assertRaises(ValidationError):
            a.full_clean()
