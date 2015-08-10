from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.inside, name = 'inside'),
	url(r'^unload/$', views.unload, name = 'unload'),
	url(r'^root/$', views.rootpage, name = 'rootpage'),
	url(r'^city/$', views.dashboard, name = 'dashboard'),
	url(r'^warehouse/$', views.warehouse, name = 'warehouse'),
	url(r'^office/$', views.office, name = 'office'),
	url(r'^warehouse/change_bag_status/$', views.change_bag_status, name = "change_bag_status"),
	url(r'^office/plan_new_unload/$', views.plan_new_unload, name = "plan_new_unload"),
	url(r'^office/cancel_planned_unload/$', views.cancel_planned_unload, name = "cancel_planned_unload"),
	url(r'^office/data_for_global_chart/$', views.data_for_global_chart, name = "data_for_global_chart"),
	url(r'^logout/$', views.log_out, name = 'log_out'),
	#url(r'^$', views.index, name = 'index'),
	url(r'^city/(?P<bin_ident>[0-9]+)/$', views.detail, name = 'detail'),
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