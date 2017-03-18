from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^postList', views.post_list, name='post_list'),
    url(r'^post_list/', views.post_list, name='post_list'),
    url(r'^posts_json/', views.posts_json, name='posts_json'),
    # url(r'^query_posts/', views.query_posts, name='query_posts')
]
