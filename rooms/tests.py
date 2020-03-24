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

    def test_autogenerate_room_name_when_empty(self):
        """
        Appointments without a room name get a random room name on save
        """
        a = Appointment(name="testappointment",
                        start_time=timezone.now(),
                        end_time=timezone.now() + datetime.timedelta(minutes=30))
        a.full_clean()
        a.save()
        self.assertIsNot(a.room_name, None)

    def test_leave_room_name_when_submitted(self):
        """
        Appointments with a room name set should not get it overwritten
        """
        a = Appointment(name="testappointment",
                        start_time=timezone.now(),
                        end_time=timezone.now() + datetime.timedelta(minutes=30),
                        room_name="my test room")
        a.full_clean()
        a.save()
        self.assertIs(a.room_name, "my test room")
