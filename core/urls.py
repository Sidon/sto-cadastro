from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.create_account, name='create_account'),
]
