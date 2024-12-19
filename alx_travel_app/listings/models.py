from django.db import models
import uuid
from django.utils import timezone


# Create your models here.
class User(models.Model):
    user_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, unique=True, null=False)
    password_hash = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=10, null=True)
    GUEST = 'guest'
    HOST = 'host'
    ADMIN = 'admin'

    ROLE_CHOICES = [(ADMIN,'Admin'),(GUEST,'Guest'),(HOST,'Host')]
    role = models.CharField(max_length=10,choices=ROLE_CHOICES,default=GUEST,null=False)
    created_at = models.TimeField(default=timezone.now)

    class Meta():
        indexes = [
            models.Index(fields=['user_id'])
        ]
        

class Listing(models.Model):
    listing_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    host_id = models.ForeignKey(User, to_field='user_id', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    location = models.CharField(max_length=100, null=False)
    pricepernight = models.DecimalField(decimal_places=2,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta():
        indexes = [
            models.Index(fields=['listing_id'])
        ]
    


class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    property_id = models.ForeignKey(Listing, to_field='listing_id', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, to_field='user_id',on_delete=models.CASCADE)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    total_price = models.DecimalField(decimal_places=2,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        indexes = [
            models.Index(fields=['booking_id'])
        ]


class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    property_id = models.ForeignKey('Listing', to_field='listing_id', on_delete=models.CASCADE)
    user_id = models.ForeignKey('User', to_field='user_id', on_delete=models.CASCADE)
    rating = models.IntegerField(null=False)
    comment = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(rating__gte=1, rating__lte=5), name='rating_between_1_and_5')
        ]
