from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Bin, Measurement, Type, Bag, Unload, City_Pace, Demos
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from pytz import timezone
import pytz
from datetime import datetime, timedelta
from django.contrib.auth.models import User
import json
from django.conf import settings
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)

def my_view(request, arg1, arg):
    if bad_mojo:
        logger.error('Something went wrong!')
#import date
tz = 'Europe/Moscow'

def inside(request):
	#from django.contrib.auth import authenticate, login
	if request.user.is_authenticated():
		bins_list = Bin.objects.all().order_by('bin_id')
		context = {}
		if bins_list:
			city_pace = 0
			recycle_now_in_bins = 0
			for a_bin in bins_list:
				city_pace += a_bin.bin_generate_volume_pace()
				recycle_now_in_bins += a_bin.bin_get_current_fill_litres()
			city_pace *= 0.024
			recycle_now_in_bins /= 1000
			city_pace = ("{0:.2f}".format(city_pace))
			recycle_now_in_bins = ("{0:.2f}".format(recycle_now_in_bins))
			context = RequestContext = {'bins_list': bins_list, 'bins_list_ordered': bins_list[0].bin_get_ordered_bins_list, 'types': Type.objects.all(), 'pace': city_pace, 'volume': recycle_now_in_bins }
		return render(request, 'control_measure/dashboard.html', context)
	else:
		try:
			e_mail = request.POST['e_mail']
			passw = request.POST['passw']
		except (KeyError, User.DoesNotExist):
			return render(request, 'control_measure/inside.html', {'err_msg': ''})
		else:
			logger.info("LOGGGGGGGGGGGGGGG")
			try:
				demos_search = Demos.objects.get(username = e_mail)
			except (KeyError, Demos.DoesNotExist):
				user = authenticate(username = e_mail, password = passw)
				if user is not None:
					if user.is_active:
						login(request, user)
						#bins_list = Bin.objects.all().order_by('bin_id')
						#context = {}
						#if bins_list:
						#	city_pace = 0
						#	recycle_now_in_bins = 0
						#	for a_bin in bins_list:
						#		city_pace += a_bin.bin_generate_volume_pace()
						#		recycle_now_in_bins += a_bin.bin_get_current_fill_litres()
						#	city_pace *= 0.024
						#	recycle_now_in_bins /= 1000
						#	city_pace = ("{0:.2f}".format(city_pace))
						#	recycle_now_in_bins = ("{0:.2f}".format(recycle_now_in_bins))
						#	context = RequestContext = {'bins_list': bins_list, 'bins_list_ordered': bins_list[0].bin_get_ordered_bins_list, 'types': Type.objects.all(), 'pace': city_pace, 'volume': recycle_now_in_bins }
						return HttpResponseRedirect("/city") #render(request, 'control_measure/dashboard.html', context)
					else:
						err_msg = 'Account has been disabled'
				else:
					err_msg = 'Account and password are incorrect'
				return render(request, 'control_measure/inside.html', {'err_msg': err_msg})
			else :
				logger.info(demos_search)
				if demos_search:
					user = authenticate(username = e_mail, password = passw)
					if user is not None:
						if user.is_active:
							login(request, user)
							context = {'user': demos_search, 'ava': demos_search.demos_avatar }
							logger.info(demos_search.demos_avatar.url)
							return HttpResponseRedirect("/soznaik")#render_to_response('control_measure/demos_workspace.html', context)
						else:
							err_msg = 'Account has been disabled'
							return render(request, 'control_measure/inside.html', {'err_msg': err_msg})
					else:
						err_msg = 'Account and password are incorrect'
						return render(request, 'control_measure/inside.html', {'err_msg': err_msg})
			
				

def soznaik (request):
	if request.user.is_authenticated():
		demos_search = Demos.objects.get(email = request.user.email)
		demos_bins_list = demos_search.demos_bins
		logger.info(demos_search)
		logger.info(demos_bins_list)
		return render(request, 'control_measure/demos_workspace.html', {'user': demos_search, 'ava': demos_search.demos_avatar, 'bins': demos_bins_list })

def rootpage (request):
	if request.user.is_authenticated():
		return render(request, 'control_measure/rootpage.html', context)
	else:
		return render(request, 'control_measure/inside.html', context)


def log_out(request):
	logout(request)
	return HttpResponseRedirect("/")#render(request, 'control_measure/inside.html', {'err_msg': ''})


def unload(request):
	if request.user.is_authenticated():
		unload_list_planned = Unload.objects.all().filter(unload_status = 1).order_by('unload_date')
		unload_list_fulfilled = Unload.objects.all().filter(unload_status = 0).order_by('unload_date')
		context = {'unload_list_planned': unload_list_planned, 'unload_list_fulfilled': unload_list_fulfilled }
		return render(request, 'control_measure/unload.html', context)
	else:
		return render(request, 'control_measure/inside.html', {})

		


def dashboard(request):
	if request.user.is_authenticated():
		bins_list = Bin.objects.all().order_by('bin_id')
		context = {}
		if bins_list:
			city_pace = 0
			recycle_now_in_bins = 0
			for a_bin in bins_list:
				city_pace += a_bin.bin_generate_volume_pace()
				recycle_now_in_bins += a_bin.bin_get_current_fill_litres()
			city_pace *= 0.024
			recycle_now_in_bins /= 1000
			city_pace = ("{0:.2f}".format(city_pace))
			recycle_now_in_bins = ("{0:.2f}".format(recycle_now_in_bins))
			context = RequestContext = {'bins_list': bins_list, 'bins_list_ordered': bins_list[0].bin_get_ordered_bins_list, 'types': Type.objects.all(), 'pace': city_pace, 'volume': recycle_now_in_bins }
		#from django.conf import settings
		return render(request, 'control_measure/dashboard.html', context)
	else:
		return render(request, 'control_measure/inside.html', {})


def warehouse(request):
	if request.user.is_authenticated():
		inside_bin_bags = Bag.objects.filter(bag_status=1)
		full_bags = Bag.objects.filter(bag_status=2)
		empty_bags = Bag.objects.filter(bag_status=3)
		context = { 'inside_bin_bags': inside_bin_bags, 'full_bags':full_bags, 'empty_bags': empty_bags, 'unload': Unload.objects.all().order_by('unload_date').first() }
		return render(request, 'control_measure/warehouse.html', context)
	else:
		return render(request, 'control_measure/inside.html', {'err_msg': ""})


def change_bag_status(request):
	bag_ident = request.GET['bag_ident']
	bag_stat = request.GET['bag_status']
	a_bag = get_object_or_404(Bag, bag_id = bag_ident)
	a_bag.bag_status = bag_stat
	a_bag.save()
	inside_bin_bags = Bag.objects.filter(bag_status=1)
	full_bags = Bag.objects.filter(bag_status=2)
	empty_bags = Bag.objects.filter(bag_status=3)
	context = { 'inside_bin_bags': inside_bin_bags, 'full_bags':full_bags, 'empty_bags': empty_bags }
	return render(request, 'control_measure/warehouse.html', context)


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
	if request.user.is_authenticated():
		a_bin = get_object_or_404(Bin, bin_id = bin_ident)
		measure_set = a_bin.measurement_set.all().order_by('measurement_date')
		if measure_set.count() > 1:
			mes_first = measure_set[0]
			for mes in measure_set[1:]:
				if mes.measurement_volume > mes_first.measurement_volume:
					pace_of_date = a_bin.bin_generate_volume_pace_of_date(mes.measurement_date)
					if pace_of_date:
						time_delta_usual = mes.measurement_date - mes_first.measurement_date
						time_delta_in_hours = time_delta_usual.days * 24 + time_delta_usual.seconds / 3600
						fill_of_date = mes_first.measurement_volume + pace_of_date * time_delta_in_hours
						mes.measurement_error = ((fill_of_date - mes.measurement_volume) / mes.measurement_bin.bin_get_volume()) * 100
						mes.save()
				mes_first = mes
		return render(request, 'control_measure/detail.html', { 'a_bin': a_bin })
	else:
		return render(request, 'control_measure/inside.html', {'err_msg': ""})


def count_error(request, bin_ident):
	a_bin = get_object_or_404(Bin, bin_id = bin_ident)
	measure_set = a_bin.measurement_set.all().order_by('measurement_date')
	if measure_set.count() > 1:
		mes_first = measure_set[0]
		for mes in measure_set[1:]:
			if mes.measurement_volume > mes_first.measurement_volume:
				pace_of_date = a_bin.bin_generate_volume_pace_of_date(mes.measurement_date)
				if pace_of_date:
					time_delta_usual = mes.measurement_date - mes_first.measurement_date
					time_delta_in_hours = time_delta_usual.days * 24 + time_delta_usual.seconds / 3600
					fill_of_date = mes_first.measurement_volume + pace_of_date * time_delta_in_hours
					mes.measurement_error = ((fill_of_date - mes.measurement_volume) / mes.measurement_bin.bin_get_volume()) * 100
					mes.save()
			mes_first = mes
	#return HttpResponse("You're looking at question %s." % a_bin.bin_adress)
	return render(request, 'control_measure/detail.html', { 'a_bin': a_bin })

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
	#return render(request, 'control_measure/detail.html', { 'a_bin': a_bin  })

def data_for_global_chart(request):
	dict_for_send = []
	if City_Pace.objects.all():
		for a_city_pace in City_Pace.objects.all().order_by('city_pace_date'):
			dict_elem = {}
			dict_elem['day'] = a_city_pace.city_pace_date.day
			dict_elem['month'] = a_city_pace.city_pace_date.month
			dict_elem['pace'] = float(a_city_pace.city_pace_value)
			logger.info(dict_elem)
			dict_for_send.append(dict_elem)
		dump = json.dumps(dict_for_send)
		return HttpResponse(dump, content_type='application/json')



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
		a_bag_id = int(request.POST['unload_bag_id'])
		a_bag_id_new = int(request.POST['unload_bag_id_new'])
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
			if a_bag_id <= Bag.objects.all().order_by('bag_id').last().bag_id:
				old_bag = Bag.objects.get(bag_id = a_bag_id)
				new_bag = Bag.objects.get(bag_id = a_bag_id_new)
				if old_bag.bag_status == 1:
					if new_bag.bag_status == 3:
						old_bag.bag_status = 2
						old_bag.bag_in_bin = None
						old_bag.save()
						new_bag.bag_status = 1
						new_bag.bag_in_bin = a_bin
						new_bag.save()
						volume_in_fact_before = (percent_before * a_bin.bin_type.type_get_volume()) / 100
						the_date_of_finish = the_date_of_begin_datetime + timedelta(minutes = 5)
						a_bin.measurement_set.create(measurement_date = the_date_of_begin_datetime, measurement_percentage = percent_before, measurement_volume = volume_in_fact_before, measurement_bag = a_bag_id)
						a_bin.measurement_set.create(measurement_date = the_date_of_finish, measurement_percentage = percent_after, measurement_volume = (percent_after * a_bin.bin_type.type_get_volume()) / 100)
						a_bin.bin_status = 'False'
						a_bin.save()
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

def add_mass(request, bin_ident, meas_id):
	a_measurement = get_object_or_404(Measurement, id = meas_id)
	a_bin = get_object_or_404(Bin, bin_id = bin_ident)
	need_index = "measurement_mass_" + str(meas_id)
	try:
		a_mass = int(request.POST[need_index])
	except (KeyError, Measurement.DoesNotExist):
		return render(request, 'control_measure/detail.html', {'a_bin': a_bin })
	else:
		a_measurement.measurement_mass = a_mass
		a_measurement.save()
		return render(request, 'control_measure/detail.html', {'a_bin': a_bin })

def office(request):
	context = {}
	if request.user.is_authenticated():
		#if Bin.bin_get_bins_not_included_into_unloadings():
		unload_list = Unload.objects.all()
		City_Pace.city_pace_count_rest()
		context = { 'waiting_bins_list': Bin.bin_get_bins_not_included_into_unloadings(), 'unload_list': unload_list }
		logger.info(context)
		return render(request, 'control_measure/office.html', context)
	else:
		return render(request, 'control_measure/inside.html', context)

def plan_new_unload(request):
	context = {}
	a_bins_list = []
	#logger.info(Unload.objects.all().order_by('unload_id').last().unload_id)
	if Unload.objects.all().order_by('unload_id'):
		new_id = Unload.objects.all().order_by('unload_id').last().unload_id + 1
	else:
		logger.info('first unload')
		new_id = 1
	try:
		a_date = request.GET['date_of_unload']
	except (KeyError, Measurement.DoesNotExist):
		logger.info('stop')
	else:
		a_date += " 10:00"
		logger.info(a_date)
		new_unload = Unload(unload_id = new_id, unload_date = a_date, unload_status = 1)
		new_unload.save()
	#пока можно максимум 6 контейнеров добавить в вывоз
	for i in range (6):
		try:
			new_bin_for_unload = request.GET[str(i)]
		except (KeyError, Measurement.DoesNotExist):
			logger.info('error')
			break
		else:
			a_bins_list.append(new_bin_for_unload)
			a_real_bin = Bin.objects.get(bin_adress = new_bin_for_unload)
			a_real_bin.bin_status = 'True'
			a_real_bin.save()
			new_unload.unload_bins_list.add(a_real_bin)
			new_unload.save()

			logger.info(a_real_bin)
	logger.info(a_bins_list)
	return render(request, 'control_measure/office.html', context)

	#new_unload = Unload(unload_date = a_date, unload_status = 1)
	#for a_bin in a_bins_list:
	#	a_real_bin = Bin.objects.get(bin_adress = a_bin)
	#	new_unload.unload_bins_list.add(a_real_bin)
	#	a_real_bin.bin_status = True
	#return render(request, 'control_measure/office.html', context)

def cancel_planned_unload(request):
	context = {}
	try:
		an_unload_id = request.GET['id']
	except (KeyEror, Measurement.DoesNotExist):
		logger.info('error')
	else:
		logger.info(an_unload_id)
		an_unload = Unload.objects.get(unload_id = an_unload_id)
		for a_bin in an_unload.unload_get_bins():
			#changed_bin = Bin.objects.get(bin_id = a_bin.bin_id)
			a_bin.bin_status = False
			a_bin.save()
			#logger.info(Bin.objects.get(bin_id = a_bin.bin_id).bin_status)
		an_unload.delete()
		#an_unload.save()
		return render (request, 'control_measure/office.html', context)
