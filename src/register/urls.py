from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.register_donor, name='register'),
]