from statistics import mean
from django.shortcuts import render

from .models import Route, Station


def station_view(request):
    template_name = 'stations.html'
    route = request.GET.get('route')
    routes = Route.objects.all()
    context = {'routes': routes}
    if route:
        current_route = routes.prefetch_related('stations').get(name=route)
        stations = current_route.stations.all()
        longitude_list = []
        latitude_list = []
        station_list = []
        for station in stations:
            longitude_list.append(station.longitude)
            latitude_list.append(station.latitude)
            rt_numbers = []
            for rt in station.routes.all():
                rt_numbers.append(rt.name)
            station_list.append({'longitude': station.longitude, 'latitude': station.latitude,
                                 'name': station.name, 'route_numbers': rt_numbers})
        center = {'x': mean(longitude_list), 'y': mean(latitude_list)}

        context['stations'] = station_list
        context['center'] = center

    return render(
        request,
        template_name,
        context
    )
