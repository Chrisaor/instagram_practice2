from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post-list'),
    path('post_create/', views.post_create, name='post-create'),
    path('<int:pk>/', views.post_detail, name='post-detail'),
]