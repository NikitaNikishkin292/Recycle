from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from .models import Bin, Measurement
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'control_measure/index.html')

def dashboard(request):
	#user = get_object_or_404(User, pk = user_id)
	bins_list = Bin.objects.all().order_by('bin_id')
	context = RequestContext = {'bins_list': bins_list}
	return render(request, 'control_measure/dashboard.html', context)

def add_bin(request):
	all_number = Bin.objects.count() + 1
	try:
		new_bin_adress = request.POST['bin_adress']
		new_bin_volume = int(request.POST['bin_volume'])
	except (KeyError, Bin.DoesNotExist):
		return render(request, 'control_measure/dashboard.html', {'bins_list': bins_list})
	else:
		new_bin = Bin(bin_id = all_number, bin_adress = new_bin_adress, bin_volume = new_bin_volume)
		new_bin.save()
		bins_list = Bin.objects.all().order_by('bin_id')
		context = RequestContext = {'bins_list': bins_list}
		return render(request, 'control_measure/dashboard.html', context)

def detail(request, bin_ident):
	a_bin = get_object_or_404(Bin, bin_id = bin_ident)
	#return HttpResponse("You're looking at question %s." % a_bin.bin_adress)
	return render(request, 'control_measure/detail.html', { 'a_bin': a_bin })

def add_measurement(request, bin_ident):
	a_bin = get_object_or_404(Bin, bin_id = bin_ident)
	try:
		new_date = request.POST['measurement_date']
		new_cells_inside = int(request.POST['measurement_cells_inside'])
		new_cells_maximum = int(request.POST['measurement_cells_maximum'])
	except (KeyError, Measurement.DoesNotExist):
		return render(request, 'control_measure/detail.html', {'a_bin': a_bin})
	else:
		a_bin.measurement_set.create(measurement_date = new_date, measurement_cells_inside = new_cells_inside, measurement_cells_maximum = new_cells_maximum)
		return render(request, 'control_measure/detail.html', {'a_bin' : a_bin})

