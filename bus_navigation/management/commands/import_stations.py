import csv
from django.core.management.base import BaseCommand
from bus_navigation.models import Station, Route
from django.conf import settings


class Command(BaseCommand):
    help = 'Import from CSV to database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open(settings.CSV_PATH, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            station_list = list(reader)[1:]
            length = len(station_list)
            for i, line in enumerate(station_list):
                name = line[1]
                longitude = float(line[2])
                latitude = float(line[3])
                routes = line[7].split('; ')
                station = Station.objects.create(name=name, latitude=latitude, longitude=longitude)
                for route in routes:
                    route_obj, created = Route.objects.get_or_create(name=route)
                    station.routes.add(route_obj)
                print('{} out of {} imported'.format(i + 1, length))
