from django.core.management.base import BaseCommand, CommandError

from shortener.models import AppURL


class Command(BaseCommand):
    help = 'Refreshes all AppURL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return AppURL.objects.refresh_shortcodes(items=options['items'])
