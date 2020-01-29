from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "greeting"

    def handle(self, *args, **options):
        self.stdout.write('Hi, this is Django!')
