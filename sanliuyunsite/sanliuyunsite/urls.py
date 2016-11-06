"""sanliuyunsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
<<<<<<< HEAD
from sanliuyunapp.views import editor, login
=======
from sanliuyunapp.views import registerView,loginView,indexView
>>>>>>> tcudorp/master
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^editor', editor, name='editor'),
    url(r'^logout/$', logout, {'next_page':'/login'}, name='logout'),
    url(r'^login/$', login, name='login'),
=======
    url(r'^$', indexView,name='index'),
    url(r'^index$', indexView,name='index'),
    url(r'^register/', registerView,name='register'),
    url(r'^login/', loginView,name='login'),
    url(r'^logout/', logout,{'next_page': '/index'},name='logout'),
>>>>>>> tcudorp/master
]
