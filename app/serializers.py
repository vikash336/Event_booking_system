from rest_framework import serializers
from .models import EventOrganizers, Customers, Event, TicketType, Booking

class EventOrganizersSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventOrganizers
        fields = "__all__"

class EventUserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = EventOrganizers
        fields = ['email', 'password']
class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = "__all__"

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
