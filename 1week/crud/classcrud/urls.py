from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    # Blog~~ is class!
    # .as_view() is a method.
    # the second parameter of path is function. So we can`t input class in second params.

    path('', views.BlogView.as_view(), name='list'),
    path('newblog/', views.BlogCreate.as_view(), name='new'),
    path('detail/<int:pk>', views.BlogDetail.as_view(), name='detail'),
    path('update/<int:pk>', views.BlogUpdate.as_view(), name='change'),
    path('delete/<int:pk>', views.BlogDelete.as_view(), name='del'),
    
]