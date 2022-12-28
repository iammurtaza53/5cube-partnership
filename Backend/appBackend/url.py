from django.contrib import admin
from django.urls import path
from appBackend import views

urlpatterns=[
    path("",views.index, name ='home'),
    path("about",views.about, name ='about'),
    # path("catinfo",views.category_detail),
    path('catinfo/<int:pk>',views.category_detail),
    path('category_list/',views.category_list),
    path('category_create',views.category_create),
    path('category_delete',views.category_delete),
    path('category_update',views.category_update),
]
