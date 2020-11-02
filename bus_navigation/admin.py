from django.contrib import admin
from .models import Station, Route


class RoutesInline(admin.TabularInline):
    model = Station.routes.through
    extra = 0


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    inlines = (RoutesInline,)


@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    pass
