from rest_framework import serializers
from .models import Listing,Booking


class ListingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields= 'listing_id','host_id','name','description','location','pricepernight','created_at','updated_at'


class BookingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields= 'booking_id','property_id','user_id','start_date','end_date','total_price','created_at'
