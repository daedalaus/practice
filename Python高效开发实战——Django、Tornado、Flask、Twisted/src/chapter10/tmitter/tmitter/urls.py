"""tmitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from mvc.views import signup, signin, detail, index_user_page, users_index, users_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^signup/$', signup),
    path(r'^signin/$', signin),
    path(r'^user/(?P<_username>[a-zA-Z\-_\d]+)/(?P<_page_index>\d+)/$', index_user_page),
    path(r'^message/(?P<_id>\d+)/$', detail, name='tmitter-mvc-views-detail'),
    path(r'users/$', users_index),
    path(r'users/(?P<_page_index>\d+)/$', users_list),
]
