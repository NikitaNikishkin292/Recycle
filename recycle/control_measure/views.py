from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from .models import Bin

def index(request):
	first_five_bins = Bin.objects.all().order_by('bin_id')
	context = RequestContext = {'first_five_bins': first_five_bins}
	return render(request, 'control_measure/index.html', context)
