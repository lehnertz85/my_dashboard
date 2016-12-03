from django.conf import settings

from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^dashboard/', views.index, name='index'),
    url(r'^service/(?P<app_id>\d+)/$', views.getiframe, name='iframe'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
