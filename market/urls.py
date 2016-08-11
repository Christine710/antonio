from django.conf.urls import url
from . import views

app_name = 'market'

urlpatterns = [
    # /market/
    url(r'^$', views.market, name='market'),
    url(r'^$', views.IndexView.as_view(), name='market'),

    # /market/<product_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]