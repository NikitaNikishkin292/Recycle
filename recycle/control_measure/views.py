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
import json
#import date
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


def data_for_chart(request, bin_ident):
	a_bin = get_object_or_404(Bin, bin_id = bin_ident)
	dict_for_send = []
	if a_bin.measurement_set.all().order_by('measurement_date').count() > 1:
		mes_beg = a_bin.measurement_set.all().order_by('measurement_date')[0]
		for mes in a_bin.measurement_set.all().order_by('measurement_date')[1:]:
			if mes.measurement_volume > mes_beg.measurement_volume:
				time_delta = mes.measurement_date - mes_beg.measurement_date
				time_delta = time_delta.days + time_delta.seconds / (3600 * 24)
				dict_elem = {}
				dict_elem['day'] = mes.measurement_date.day
				dict_elem['month'] = mes.measurement_date.month
				dict_elem['pace'] = (mes.measurement_volume - mes_beg.measurement_volume) / time_delta
				dict_for_send.append(dict_elem)
			mes_beg = mes
		dump = json.dumps(dict_for_send)
		return HttpResponse(dump, content_type='application/json')
	return render(request, 'control_measure/detail.html', { 'a_bin': a_bin  })


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
			volume_in_fact = (float(measurement_percent) * a_bin.bin_type.type_get_volume()) / 100
			a_bin.measurement_set.create(measurement_date = the_date_datetime, measurement_percentage = measurement_percent, measurement_volume = volume_in_fact)
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
			volume_in_fact_before = (percent_before * a_bin.bin_type.type_get_volume()) / 100
			the_date_of_finish = the_date_of_begin_datetime + timedelta(minutes = 5)
			a_bin.measurement_set.create(measurement_date = the_date_of_finish, measurement_percentage = percent_after, measurement_volume = (percent_after * a_bin.bin_type.type_get_volume()) / 100)
			a_bin.measurement_set.create(measurement_date = the_date_of_begin_datetime, measurement_percentage = percent_before, measurement_volume = volume_in_fact_before)
		return render(request, 'control_measure/detail.html', {'a_bin': a_bin })

def add_event(request, bin_ident):
	a_bin = get_object_or_404(Bin, bin_id = bin_ident)
	try:
		an_event_date = request.POST['event_date']
		an_event_description = request.POST['event_description']
	except (KeyError, Bin.DoesNotExist):
		return render(request, 'control_measure/detail.html', {'a_bin': a_bin })
	else:
		the_date_of_event = datetime.strptime(an_event_date, "%Y-%m-%d")
		tz = 'Europe/Moscow'
		current_server_time = datetime.utcnow()
		current_client_time = timezone(tz).fromutc(current_server_time)
		our_date_for_comparison = pytz.utc.localize(the_date_of_event) - timedelta(hours = 3)
		if our_date_for_comparison <= current_client_time:
			a_bin.event_set.create(event_date = an_event_date, event_description = an_event_description)
	return render(request, 'control_measure/detail.html', {'a_bin': a_bin })


def add_volume(request, bin_ident):
	a_bin = get_object_or_404(Bin, bin_id = bin_ident)
	try:
		a_volume_date = request.POST['volume_date']
		a_volume = request.POST['volume']
	except (KeyError, Bin.DoesNotExist):
		return render(request, 'control_measure/detail.html', {'a_bin': a_bin })
	else:
		#the_date_of_volume = datetime.strptime(a_volume_date, "%Y-%m-%d")
		a_volume_date += " 15:00"
		a_bin.measurement_set.create(measurement_date = a_volume_date, measurement_volume = a_volume, measurement_percentage = (int(a_volume) / a_bin.bin_get_volume() * 100))
	return render(request, 'control_measure/detail.html', {'a_bin': a_bin })
