from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.dashboard, name = 'dashboard'),
	#url(r'^$', views.index, name = 'index'),
	url(r'^(?P<bin_ident>[0-9]+)/$', views.detail, name = 'detail'),
	url(r'^add/$', views.add_bin, name = 'add_bin'),
	#url(r'^(?P<bin_ident>[0-9]+)/add_meas/$', views.add_measurement, name = 'add_measurement'),
	#url(r'^(?P<bin_ident>[0-9]+)/unload/$', views.unload_bin, name = "unload_bin"),
	url(r'^(?P<bin_ident>[0-9]+)/add_percent/$', views.add_measurement_percent, name = "add_measurement_percent"),
	url(r'^(?P<bin_ident>[0-9]+)/unload_percent/$', views.unload_bin_percent, name = "unload_bin_percent"),
	url(r'^(?P<bin_ident>[0-9]+)/add_event/$', views.add_event, name = "add_event"),
	url(r'^(?P<bin_ident>[0-9]+)/data_for_chart/$', views.data_for_chart, name = "data_for_chart"),
	url(r'^(?P<bin_ident>[0-9]+)/add_volume/$', views.add_volume, name = "add_volume"),
	url(r'^(?P<bin_ident>[0-9]+)/(?P<meas_id>[0-9]+)/$', views.add_mass, name = "add_mass"),
	url(r'^(?P<bin_ident>[0-9]+)/count_error/$', views.count_error, name = "count_error"),
]