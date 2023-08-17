# your_app/management/commands/fetchrepos.py
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Fetches user repository list from GitHub API'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='GitHub username')

    def handle(self, *args, **options):
        username = options['username']
        self.stdout.write(f'Fetching repositories for {username}...')