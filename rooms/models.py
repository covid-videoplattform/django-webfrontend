import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


# health care worker who is available for appointments
class StaffMember(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('full name'))
    email = models.EmailField(null=True, blank=True,
                              verbose_name=_('contact email address'))
    phone = PhoneNumberField(null=True, blank=True,
                             verbose_name=_('phone number'))
    last_modified = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rooms:staff-detail', kwargs={'pk': self.pk})


# represents the connection between a staffmember, a time and a videochatroom
class Appointment(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    description = models.TextField(null=True, blank=True,
                                   verbose_name=_('description'))
    last_modified = models.DateTimeField(auto_now=True, blank=True)
    start_time = models.DateTimeField(
        _('start of appointment'), null=True, blank=True)
    end_time = models.DateTimeField(
        _('end of appointment'), null=True, blank=True)
    staffmember = models.ForeignKey(
        StaffMember, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name=_('staff member'))
    room_name = models.CharField(max_length=255, null=True, blank=True, 
                                 verbose_name=_('room name'))

    def clean(self, *args, **kwargs):
        cleaned_data = super(Appointment, self).save(*args, **kwargs)

        if getattr(self, 'room_name') is None:
            self.room_name = uuid.uuid4().hex[:6].upper()

        if self.start_time and self.end_time:
            # Only do something if both fields are valid so far.
            if self.end_time <= self.start_time:
                raise ValidationError(
                    _("End time should be after start time.")
                )
        return cleaned_data

    def is_permanent(self):
        return True if self.start_time is None else False

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rooms:appointment-detail', kwargs={'pk': self.pk})

    def short_description(self):
        if self.description and len(self.description) > 75:
            return (self.description[:75] + '…')
        else:
            return self.description
