"""
URL configuration for swiftCRM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add-new-record/',views.add_new_record_view,name='add-new-record'),
    path('view-record/<int:pk>/',views.view_record,name='view-record'),
    path('update-record/<int:pk>/',views.update_record_view,name='update-record'),
    path('delete-record/<int:pk>/',views.delete_record_view,name='delete-record'),
]
