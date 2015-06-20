from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.dashboard, name = 'dashboard'),
	#url(r'^$', views.index, name = 'index'),
	url(r'^(?P<bin_ident>[0-9]+)/$', views.detail, name = 'detail'),
	url(r'^add/$', views.add_bin, name = 'add_bin'),
	url(r'^(?P<bin_ident>[0-9]+)/add_meas/$', views.add_measurement, name = 'add_measurement'),
	url(r'^(?P<bin_ident>[0-9]+)/unload/$', views.unload_bin, name = "unload_bin"),
	url(r'^(?P<bin_ident>[0-9]+)/add_percent/$', views.add_measurement_percent, name = "add_measurement_percent"),
	url(r'^(?P<bin_ident>[0-9]+)/unload_percent/$', views.unload_bin_percent, name = "unload_bin_percent"),
]