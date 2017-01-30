from django.conf.urls import url
from . import views



urlpatterns = [

               url(r'^$',views.post_lists,name='index'),#notログイン時用
               #url(r'^$', views.TopPageView.as_view(), name='index'),#ログイン時用
               url(r'^mypage/$', views.Mypage_home, name='mypage'),
               url(r'^create/$', views.CreateUserView.as_view(), name='create'),
               url(r'^login/$', views.login, name='login'),
               url(r'^logout/$', views.logout, name='logout'),
               url(r'^user/(?P<id>[0-9]+)/$', views.user_detail,name="user_post"),

               ]
