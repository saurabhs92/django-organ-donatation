from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.register_donor, name='create'),
    url(r'^(?P<id>\d+)/$', views.donor_detail, name='detail'),
    #url(r'^thank-you/$', views.register_success, name='sucess')
]
