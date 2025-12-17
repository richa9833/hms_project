from django.contrib import admin
from .models import Availability, Booking

@admin.register(Availability)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'start_time', 'end_time', 'is_booked')
    list_filter = ('is_booked', 'date')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'availability')
