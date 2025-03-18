from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'time', 'count', 'notes')  
    list_filter = ('time', 'count') 

admin.site.register(Reservation, ReservationAdmin)