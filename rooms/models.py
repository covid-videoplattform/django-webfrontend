from django.core.exceptions import ValidationError
from django.db import models


# health care worker who is available for appointments
class StaffMember(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)


# represents the connection between a staffmember, a time and a videochatroom
class Appointment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True, blank=True)
    last_modified = models.DateTimeField(auto_now=True, blank=True)
    start_time = models.DateTimeField(
        'start of appointment', null=True, blank=True)
    end_time = models.DateTimeField(
        'end of appointment', null=True, blank=True)
    staffmember = models.ForeignKey(
        StaffMember, on_delete=models.SET_NULL, null=True, blank=True)
    room_name = models.CharField(max_length=255, null=True, blank=True)

    def clean(self, *args, **kwargs):
        cleaned_data = super(Appointment, self).save(*args, **kwargs)

        if self.start_time and self.end_time:
            # Only do something if both fields are valid so far.
            if self.end_time <= self.start_time:
                raise ValidationError(
                    "end_time should be after start_time"
                )
        return cleaned_data

    def is_permanent(self):
        return True if self.start_time is None else False
