from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'list-home' ),
    # path('add', views.add, name= 'add' ),


]
