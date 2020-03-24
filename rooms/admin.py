from django.contrib import admin

from .models import Appointment, StaffMember


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('last_modified', 'name', 'start_time',
                    'end_time', 'staffmember', 'room_name')
    list_filter = ['start_time']


class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(StaffMember, StaffMemberAdmin)
