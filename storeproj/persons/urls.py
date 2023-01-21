from django.urls import path

from . import views

urlpatterns = [
     path('hi/', views.hiii, name='hii'),
#     path('<int:pk>/', views.person_update_view, name='person_change'),
#
#     path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # AJAX
]