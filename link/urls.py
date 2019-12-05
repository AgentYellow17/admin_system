from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('links/', views.LinkListView.as_view(), name='links'),
  path('links/<int:pk>', views.LinkDetailView.as_view(), name='link-detail'),
  path('signup', views.signup, name='signup'),
]
