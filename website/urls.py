from django.conf.urls import include, url
from django.contrib import admin
from market import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^market/', include('market.urls')),
    url(r'^$', views.market, name='market'),
]
