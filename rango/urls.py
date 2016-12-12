from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
                       #http://www.tangowithdjango.com/rango/) is removed and remaining is sent over
                       url(r'^$', views.index, name='index'), # matches empty string -
                       # name attribute - plausible that two separate URL mappings expressions could end calling the same view
                       url(r'^about/', views.about, name='about'),
)
