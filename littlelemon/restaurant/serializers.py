from rest_framework import serializers
from .models import Booking, Menu

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['Name', 'No_of_guests', 'BookingDate']

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['Title', 'Price', 'Inventory']
