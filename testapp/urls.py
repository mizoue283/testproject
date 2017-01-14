from django.conf.urls import url
from . import views


urlpatterns = [
               url(r'^$', views.TopPageView.as_view(), name='index'),
               url(r'^mypage/$', views.MyPageView.as_view(), name='mypage'),
               url(r'^create/$', views.CreateUserView.as_view(), name='create'),
               url(r'^login/$', views.login, name='login'),
               url(r'^logout/$', views.logout, name='logout'),
               ]
