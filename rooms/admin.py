from django.contrib import admin

from .models import Appointment, StaffMember


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('last_modified', 'name', 'start_time',
                    'end_time', 'staffmember', 'room_name')
    list_filter = ['start_time']
    search_fields = ['name', 'description']


class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ['name', 'email']


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(StaffMember, StaffMemberAdmin)
