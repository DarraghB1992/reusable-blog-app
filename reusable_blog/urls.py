from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^blog/$', views.post_list),
    url(r'^blog/popular$', views.post_pop, name='post_pop'),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    # url(r'^post/(?P<id>\d+)/$', views.post_detail),
    url(r'^blog/post/$', views.new_post, name='new_post'),
    url(r'^blog/delete/(?P<id>\d+)$', views.post_delete, name='deleter'),

]

# url(r'^popular/(?P<id>\d)/$', views.post_detail),
# url(r'^/post/(?P<id>\d+)/$', views.post_detail),
# url(r'^popular/$', views.post_pop),
