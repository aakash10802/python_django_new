"""
URL configuration for my_project project.

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
from django.contrib import admin
from django.urls import path
from APP.views import home, index, study, studentview, datadelete, editdata,dataupdate,library,libraryview,librarydelete,editbook_fun
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('in',index),
    path('st',study),
    path('sv',studentview),
    path('del/<int:id>',datadelete),
    path('edit/<int:id>',editdata),
    path('update/<int:id>',dataupdate),
    path('li',library),
    path('lv',libraryview),
    path('delete/<int:id>',librarydelete),
    path('ed/<int:id>',editbook_fun),
    
]
