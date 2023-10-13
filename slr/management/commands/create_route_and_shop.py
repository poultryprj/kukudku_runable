from django.core.management.base import BaseCommand
from slr.models import Route, Shop

class Command(BaseCommand):
    help = 'Create a Route and associate a Shop with it'

    def handle(self, *args, **kwargs):
        # Create a Route
        route = Route.objects.create(name="Kalepadal")
        
        # Create a Shop and associate it with the Route by name
        shop = Shop.objects.create(name="KRISHNANAGAR", route="Kalepadal")
        shop = Shop.objects.create(name="AKURDI", route="Chinchwad")

        
        self.stdout.write(self.style.SUCCESS('Successfully created Route and Shop'))
