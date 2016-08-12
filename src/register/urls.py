from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.register_donor, name='create'),
    url(r'^(?P<id>[0-9a-z-]+)/donor-card/$', views.download_donor_card, name='pdf'),
    url(r'^(?P<id>[0-9a-z-]+)/$', views.donor_detail, name='detail'),
    #url(r'^thank-you/$', views.register_success, name='sucess')
]


