from django.urls import path
from . import views


urlpatterns = [
    path('create', views.create_shop, name='create_shop'),
    path('view', views.view_shop, name='view_shop'),


]
