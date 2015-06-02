from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.dashboard, name = 'dashboard'),
	#url(r'^$', views.index, name = 'index'),
	url(r'^(?P<bin_ident>[0-9]+)/$', views.detail, name = 'detail'),
	url(r'^add/$', views.add_bin, name = 'add_bin'),
	url(r'^(?P<bin_ident>[0-9]+)/add_meas/$', views.add_measurement, name = 'add_measurement'),
]