from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('commerce', views.commerce, name='commerce'),
    path('bio', views.bio, name='bio'),
    path('com', views.com, name='com'),
    path('mal', views.mal, name='mal'),
    path('eng', views.eng, name='eng'),
    path('but', views.but, name='but'),
    path('', views.home, name="home"),
    path('hii', views.hii, name="hii"),
    path('nhii', views.nhii, name="nhii"),
    path('final', views.final, name="final"),
]
