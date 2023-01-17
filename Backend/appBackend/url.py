from django.contrib import admin
from django.urls import path
from appBackend import views

urlpatterns=[

    path('catinfo/<int:pk>',views.category_detail),
    path('category_list/',views.category_list),
    path('category_create',views.category_create),
    path('category_delete',views.category_delete),
    path('category_update',views.category_update),
    path('category_type',views.category_type),
    
    path('expense_list/',views.expense_list),
    path('expense_create',views.expense_create),
    path('expense_delete',views.expense_delete),
    path('expense_update',views.expense_update),
    
    path('income_list/',views.income_list),
    path('income_create',views.income_create),
    path('income_delete',views.income_delete),
    path('income_update',views.income_update),
    
    path('group_list/',views.group_list),
    path('group_create',views.group_create),
    path('group_delete',views.group_delete),
    path('group_update',views.group_update),
    path('group_activate',views.group_activate),
    
    path('share_list/',views.share_list),
    path('share_create',views.share_create),
    path('share_delete',views.share_delete),
    path('share_update',views.share_update),
    
    path('stats_filter/<int:pk>',views.filter_data_by_groupId),
    path('activegroup_filter',views.fiter_active_group_data)
]
