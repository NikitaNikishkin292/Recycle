from django.contrib import admin

# Register your models here.
from .models import Measurement, Event, Bin, Type, Bag

class MeasurementInline(admin.TabularInline):
	model = Measurement
	ordering = ('-measurement_date',)
	extra = 0

class EventInline(admin.TabularInline):
	model = Event
	extra = 0

class BinAdmin(admin.ModelAdmin):
	fields = ['bin_id', 'bin_adress', 'bin_type']
	list_display = ('bin_id', 'bin_adress', 'bin_get_average_pace_per_day_output', 'bin_type', 'bin_get_volume')
	ordering = ('bin_id',)
	inlines = [MeasurementInline, EventInline]

class TypeAdmin(admin.ModelAdmin):
	list_display = ('type_name', 'type_description', 'type_heigth', 'type_width', 'type_length', 'type_get_volume')

class MeasurementAdmin(admin.ModelAdmin):
	fieldsets = [
		('Important Information', {'fields': ['measurement_bin', 'measurement_date', 'measurement_volume', 'measurement_mass', 'measurement_bag']}),
		('Left Information', {'fields': ['measurement_percentage', 'measurement_error']}),
	]
	list_display = ['id', 'measurement_date', 'measurement_bin', 'measurement_percentage', 'measurement_volume', 'measurement_mass', 'measurement_error']
	ordering = ('-measurement_date',)
	list_filter = ['measurement_bin']

class BagAdmin(admin.ModelAdmin):
	ordering = ('bag_id',)
	list_display = ('bag_id', 'bag_status')
	list_filter = ['bag_status']


admin.site.register(Bin, BinAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(Event)
admin.site.register(Bag, BagAdmin)