from django.contrib import admin

# Register your models here.
from .models import Measurement, Event, Bin, Type

class MeasurementInline(admin.TabularInline):
	model = Measurement
	ordering = ('-measurement_date',)
	extra = 0

class EventInline(admin.TabularInline):
	model = Event
	extra = 0

class BinAdmin(admin.ModelAdmin):
	fields = ['bin_id', 'bin_adress', 'bin_type']
	list_display = ('bin_id', 'bin_adress', 'bin_get_average_pace_per_day', 'bin_type', 'bin_get_volume')
	ordering = ('bin_id',)
	inlines = [MeasurementInline, EventInline]

class TypeAdmin(admin.ModelAdmin):
	list_display = ('type_name', 'type_description', 'type_get_volume')

class MeasurementAdmin(admin.ModelAdmin):
	fieldsets = [
		('Important Information', {'fields': ['measurement_bin', 'measurement_date', 'measurement_volume', 'measurement_error']}),
		('Left Information', {'fields': ['measurement_percentage', 'measurement_cells_inside', 'measurement_cells_maximum']}),
	]
	list_display = ['measurement_date', 'measurement_bin', 'measurement_percentage', 'measurement_volume']
	ordering = ('-measurement_date',)
	list_filter = ['measurement_bin']


admin.site.register(Bin, BinAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Measurement, MeasurementAdmin)