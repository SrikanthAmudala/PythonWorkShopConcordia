from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^firstapi/', views.get_data_gps),
    url(r'^secondapi/', views.get_target_fields),
]
