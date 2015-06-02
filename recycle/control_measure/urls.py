from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<user_id>[0-9]+)/$', views.dashboard, name = 'dashboard'),
	url(r'^$', views.index, name = 'index'),
	url(r'^add/$', views.add_bin, name = 'add_bin'),
]