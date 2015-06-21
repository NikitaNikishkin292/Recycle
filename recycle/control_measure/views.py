from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from .models import Bin, Measurement, Type
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from pytz import timezone
import pytz
from datetime import datetime, timedelta
tz = 'Europe/Moscow'

def index(request):
    return render(request, 'control_measure/index.html', {})


def dashboard(request):
	bins_list = Bin.objects.all().order_by('bin_id')
	context = RequestContext = {'bins_list': bins_list, 'types': Type.objects.all() }
	from django.conf import settings
	return render(request, 'control_measure/dashboard.html', context)

def add_bin(request):
	all_number = Bin.objects.count() + 1
	try:
		new_bin_adress = request.POST['bin_adress']
		new_bin_type_name = request.POST['bin_type']
	except (KeyError, Bin.DoesNotExist):
		return render(request, 'control_measure/dashboard.html', {'bins_list': bins_list})
	else:
		new_bin_type = Type.objects.all().get(type_short_name = new_bin_type_name)
		new_bin = Bin(bin_id = all_number, bin_adress = new_bin_adress, bin_type = new_bin_type)
		new_bin.save()
		bins_list = Bin.objects.all()
		context = RequestContext = {'bins_list': bins_list, 'types': Type.objects.all() }
		return render(request, 'control_measure/dashboard.html', context)

def detail(request, bin_ident):
	a_bin = get_object_or_404(Bin, bin_id = bin_ident)
	#return HttpResponse("You're looking at question %s." % a_bin.bin_adress)
	return render(request, 'control_measure/detail.html', { 'a_bin': a_bin  })

def add_measurement(request, bin_ident):
	a_bin = get_object_or_404(Bin, bin_id = bin_ident)
	try:
		new_date = request.POST['measurement_date']
		new_time = request.POST['measurement_time']
		new_cells_inside = int(request.POST['measurement_cells_inside'])
		new_cells_maximum = int(request.POST['measurement_cells_maximum'])
	except (KeyError, Measurement.DoesNotExist):
		return render(request, 'control_measure/detail.html', {'a_bin': a_bin})
	else:
		the_date_of_begin_string = new_date + " " + new_time
		the_date_of_begin_datetime = datetime.strptime(the_date_of_begin_string, "%Y-%m-%d %H:%M")
		tz = 'Europe/Moscow'
		current_server_time = datetime.utcnow()
		current_client_time = timezone(tz).fromutc(current_server_time)
		our_date_for_comparison = pytz.utc.localize(the_date_of_begin_datetime)  - timedelta(hours = 3)
		if our_date_for_comparison <= current_client_time:
			new_percentage = 100 * (new_cells_inside/ new_cells_maximum)
			a_bin.measurement_set.create(measurement_date = the_date_of_begin_datetime, measurement_cells_inside = new_cells_inside, measurement_cells_maximum = new_cells_maximum, measurement_percentage = new_percentage * 0.95)
		return render(request, 'control_measure/detail.html', {'a_bin' : a_bin})

def unload_bin(request, bin_ident):
	a_bin = get_object_or_404(Bin, bin_id = bin_ident)
	try:
		unload_date = request.POST['unload_date']
		unload_time = request.POST['unload_time']
		cells_inside_before = int(request.POST['unload_cells_inside_before'])
		cells_inside_after = int(request.POST['unload_cells_inside_after'])
		cells_inside_maximum = int(request.POST['unload_cells_inside_maximum'])
	except (KeyError, Bin.DoesNotExist):
		return render(request, 'control-measure/detail.html', {'a_bin': a_bin})
	else:
		the_date_of_begin_string = unload_date + " " + unload_time
		the_date_of_begin_datetime = datetime.strptime(the_date_of_begin_string, "%Y-%m-%d %H:%M")
		tz = 'Europe/Moscow'
		current_server_time = datetime.utcnow()
		current_client_time = timezone(tz).fromutc(current_server_time)
		our_date_for_comparison = pytz.utc.localize(the_date_of_begin_datetime) - timedelta(hours = 3)
		if our_date_for_comparison <= current_client_time:
			the_date_of_finish = the_date_of_begin_datetime + timedelta(minutes = 5)
			percentage_before = 100 * (cells_inside_before / cells_inside_maximum)
			percentage_after = 100 * (cells_inside_after / cells_inside_maximum)
			a_bin.measurement_set.create(measurement_date = the_date_of_finish, measurement_cells_inside = cells_inside_after, measurement_cells_maximum = cells_inside_maximum, measurement_percentage = percentage_after * 0.95)
			a_bin.measurement_set.create(measurement_date = the_date_of_begin_datetime, measurement_cells_inside = cells_inside_before, measurement_cells_maximum = cells_inside_maximum, measurement_percentage = percentage_before * 0.95)
			return render(request, 'control_measure/detail.html', {'a_bin': a_bin})
		else:
			return render(request, 'control_measure/detail.html', {'a_bin': a_bin })

def add_measurement_percent(request, bin_ident):
	a_bin = get_object_or_404(Bin, bin_id = bin_ident)
	try:
		date_of_measurement = request.POST['measurement_date_percent']
		time_of_measurement = request.POST['measurement_time_percent']
		measurement_percent = request.POST['measurement_percent_inside']
	except (KeyError, Measurement.DoesNotExist):
		return render(request, 'control_measure/detail.html', {'a_bin': a_bin})
	else:
		the_date_string = date_of_measurement + " " + time_of_measurement
		the_date_datetime = datetime.strptime(the_date_string, "%Y-%m-%d %H:%M")
		tz = 'Europe/Moscow'
		current_server_time = datetime.utcnow()
		current_client_time = timezone(tz).fromutc(current_server_time)
		our_date_for_comparison = pytz.utc.localize(the_date_datetime) - timedelta(hours = 3)
		print("time", our_date_for_comparison, current_client_time)
		if our_date_for_comparison <= current_client_time:
			a_bin.measurement_set.create(measurement_date = the_date_datetime, measurement_percentage = measurement_percent)
	return render(request, 'control_measure/detail.html', {'a_bin': a_bin})

def unload_bin_percent(request, bin_ident):
	a_bin = get_object_or_404(Bin, bin_id = bin_ident)
	try:
		unload_date = request.POST['unload_date_percent']
		unload_time = request.POST['unload_time_percent']
		percent_before = int(request.POST['unload_percent_before'])
		percent_after = int(request.POST['unload_percent_after'])
	except (KeyError, Bin.DoesNotExist):
		return render(request, 'control-measure/detail.html', {'a_bin': a_bin})
	else:
		the_date_of_begin_string = unload_date + " " + unload_time
		the_date_of_begin_datetime = datetime.strptime(the_date_of_begin_string, "%Y-%m-%d %H:%M")
		tz = 'Europe/Moscow'
		current_server_time = datetime.utcnow()
		current_client_time = timezone(tz).fromutc(current_server_time)
		our_date_for_comparison = pytz.utc.localize(the_date_of_begin_datetime) - timedelta(hours = 3)
		if our_date_for_comparison <= current_client_time:
			the_date_of_finish = the_date_of_begin_datetime + timedelta(minutes = 5)
			a_bin.measurement_set.create(measurement_date = the_date_of_finish, measurement_percentage = percent_after)
			a_bin.measurement_set.create(measurement_date = the_date_of_begin_datetime, measurement_percentage = percent_before)
			return render(request, 'control_measure/detail.html', {'a_bin': a_bin})
		else:
			return render(request, 'control_measure/detail.html', {'a_bin': a_bin })

