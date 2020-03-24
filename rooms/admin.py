from django.contrib import admin

from .models import Appointment, StaffMember


admin.site.register(Appointment)
admin.site.register(StaffMember)
