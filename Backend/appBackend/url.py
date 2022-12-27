from django.contrib import admin
from django.urls import path
from appBackend import views

urlpatterns=[
    path("",views.index, name ='home'),
    path("about",views.about, name ='about'),
    # path("catinfo",views.category_detail),
    path('catinfo/<int:pk>',views.category_detail),
    path('catinfo/',views.category_list),
]
