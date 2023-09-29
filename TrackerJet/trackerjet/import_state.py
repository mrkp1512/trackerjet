import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'trackerjet.settings')
django.setup()

from settings.models import State, District, City
from state import data

for state_name, districts in data.items():
    state = State.objects.create(name=state_name)
    for district_name, cities in districts.items():
        district = District.objects.create(name=district_name, state=state)
        for city_name in cities:
            City.objects.create(name=city_name, district=district)
