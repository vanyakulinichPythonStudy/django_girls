from django.urls import path
from django.conf.urls import url
from . import views
from django.urls import register_converter


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/add_comm', views.add_comm, name='add_comm'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/discus', views.post_discus, name='post_discus'),
    path('post/fresher', views.post_fresher, name='post_fresher'),
    path('test/', views.test, name='test'),
    path('comments/', views.all_comments, name='all_comments'),
    path('images/', views.images, name='images')
    #url('test/', views.test, name='test'),
    #url('test/([0-9]([0-9]{2}))', views.test, name='test'),


















    #url('^test/(?P<sub_id>[0-9]{1,5})/([0-9]{1,5})$', views.test, name='test'),
    #url('^test/(?P<sub_id>[0-9]{1,5}/(?P<x>[0-9]{1}))$', views.test, name='test' ),
    #url('^test/(?P<sub_id>[0-9]{1,5}/(?P<x>[0-9]{1}))$', views.test, {x:'10'},name='test' ),

]
