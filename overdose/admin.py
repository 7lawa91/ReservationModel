from django.contrib import admin
from .models import Reservation 
from import_export.admin import ExportActionMixin
@admin.register(Reservation)
class ReservationAdmin(ExportActionMixin,admin.ModelAdmin):
    list_display = ('customer_name','hotel_name')
    list_filter = ('hotel_name','trip_date',)



# Register your models here.
