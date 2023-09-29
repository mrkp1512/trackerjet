import csv
from django.core.management.base import BaseCommand
from settings.models import State, District


class Command(BaseCommand):
    help = 'Import districts from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = 'D:/oneteamhtml/TrackerJet/city.csv'
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                state_name = row[0]
                district_name = row[1].strip()  # Strip leading/trailing spaces
                state, created = State.objects.get_or_create(name=state_name)
                District.objects.create(name=district_name, state=state)
