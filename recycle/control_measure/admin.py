from django.contrib import admin

# Register your models here.
from .models import Measurement, Bin

class MeasurementInline(admin.TabularInline):
	model = Measurement
	extra = 1


class BinAdmin(admin.ModelAdmin):
	fields = ['bin_id', 'bin_adress', 'bin_volume']
	list_display = ('bin_id', 'bin_adress', 'bin_get_last_fill')
	ordering = ('bin_id',)
	inlines = [MeasurementInline]

admin.site.register(Bin, BinAdmin)