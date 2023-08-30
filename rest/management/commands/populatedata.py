from django.core.management.base import BaseCommand
from rest.models import Kurulus

class Command(BaseCommand):
    help = 'Populate sample data'

    def handle(self, *args, **kwargs):
        kurulus1 = Kurulus(
            name="Örnek Kuruluş 1",
            logo="/home/abdullah/Pictures/Screenshots/Screenshot from 2023-08-30 11-15-09.png",
            type="S",
            country="Turkey",
            date="2023-08-30",
            employees=100
        )
        kurulus1.save()

        kurulus2 = Kurulus(
            name="Örnek Kuruluş 2",
            logo="/home/abdullah/Pictures/Screenshots/Screenshot from 2023-08-30 11-15-09.png",
            type="BI",
            country="USA",
            date="2023-08-30",
            employees=1000
        )
        kurulus2.save()

        self.stdout.write(self.style.SUCCESS('Sample data populated successfully'))