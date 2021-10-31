from . import views
from django.urls import path
urlpatterns = [
    path("",views.registerform,name='register'),
    path("Dashboard/",views.stdashboard,name='stdashboard'),
]