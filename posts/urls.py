from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
]
