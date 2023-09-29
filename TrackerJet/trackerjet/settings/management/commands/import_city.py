# import csv
# from django.core.management.base import BaseCommand
# from settings.models import State, City


# class Command(BaseCommand):
#     help = 'Import cities from a CSV file'

#     def add_arguments(self, parser):
#         parser.add_argument('csv_file', type=str, help='Path to the CSV file')

#     def handle(self, *args, **options):
#         csv_file_path = 'D:/oneteamhtml/TrackerJet/city.csv'

#         with open(csv_file_path, 'r') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 city_name = row['city_name']
#                 state_name = row['state_name']

#                 # Find or create state
                
#                 state_obj, _ = State.objects.get_or_create(name=state_name)
                
#                 # Create the district
#                 city_obj, _ = City.objects.get_or_create(name=city_name, state=state_obj)

#                 self.stdout.write(self.style.SUCCESS(f"Added District: {city_name} {state_name}"))
