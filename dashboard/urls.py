from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'profile/(?P<username>.+)/$', views.profile_view, name='profile'),
    url(r'^dashboard/', views.index, name='index'),
    url(r'^service/(?P<service_id>\d+)/$', views.getiframe, name='iframe'),
]
