from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^advertentie$', views.advertentie, name='advertentie'),
    url(r'^register', views.register, name='register'),
]

