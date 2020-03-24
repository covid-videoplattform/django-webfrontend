from django.db import models


# health care worker who is available for appointments
class StaffMember(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, null=True)


# represents the connection between a staffmember, a time and a videochatroom
class Appointment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    start_time = models.DateTimeField('start of appointment', null=True)
    end_time = models.DateTimeField('end of appointment', null=True)
    staffmember = models.ForeignKey(
        StaffMember, on_delete=models.SET_NULL, null=True)
    room_name = models.CharField(max_length=255, null=True)
