from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^core/', include('core.urls')),
]

# Redirects
urlpatterns += [
    url(r'^$', RedirectView.as_view(url='/core/register', permanent=False)),
    url(r'^core/$', RedirectView.as_view(url='/core/register', permanent=False)),
]