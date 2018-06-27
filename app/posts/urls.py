from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('post_create/', views.post_create, name='post-create'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
    path('<int:pk>/comment/create/', views.comment_create, name='comment-create'),
    path('<int:pk>/delete', views.post_delete, name='post-delete'),
]