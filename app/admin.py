from django.contrib import admin
from .models import EventOrganizers, Customers, Event, TicketType, Booking

admin.site.register(EventOrganizers)
admin.site.register(Customers)
admin.site.register(Event)
admin.site.register(TicketType)
admin.site.register(Booking)
