from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^', include('dashboard.urls')),
    url(r'^admin/', admin.site.urls),
]