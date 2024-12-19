import random
from django.core.management.base import BaseCommand
from listings.models import Listing
from listings.models import User
from faker import Faker
import uuid

class Command(BaseCommand):
    help = 'Populate the database with sample listings data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Fetch some random users (assuming there are already users in the database)
        users = User.objects.all()

        if not users:
            self.stdout.write(self.style.ERROR('No users found. Please create some users first.'))
            return

        # Generate and create sample listings
        for _ in range(10):  # Adjust the number of listings to create as needed
            listing = Listing(
                host_id=random.choice(users),  # Randomly assign a user as the host
                name=fake.company(),
                description=fake.paragraph(),
                location=fake.city(),
                pricepernight=round(random.uniform(50, 500), 2),
            )
            listing.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded the listings data!'))
