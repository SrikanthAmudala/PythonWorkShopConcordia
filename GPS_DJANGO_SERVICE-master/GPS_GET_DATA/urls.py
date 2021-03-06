from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^getallusers/', views.getallusers),
    url(r'^login/', views.login), # login functionality
    url(r'^list_all_books/', views.list_all_books),
    url(r'^reg_books/', views.reg_books),
    url(r'^return_books/', views.return_books),
    url(r'^getrequest/', views.get_data_gps),
    url(r'^sumofnumbers/', views.sum_of_input_numbers),


]
