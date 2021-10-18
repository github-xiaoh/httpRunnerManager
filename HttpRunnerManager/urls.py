"""HttpRunnerManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import RedirectView

from HttpRunnerManager.activator import process
from ApiManager import views as views
# from sc_pay import urls as url_sc_pay
# from testTools import urls as url_sc_cms
# from testTools.views import ajax_file
from user_ch import urls as user_ch
from AutoApiTest import urls as auto_api

urlpatterns = [
    # url(r'^sc_cms/',include((url_sc_cms,'sc_cms'),namespace='sc_cms')),
    # url(r'^sc_pay/',include((url_sc_pay,'sc_pay'),namespace="sc_pay")),
    url(r'^user_ch/',include((user_ch,'user_ch'),namespace="user_ch")),
    url(r'^auto_api/',include((auto_api,'auto_api'),namespace="auto_api")),
    # url(r'ajax_file/$',ajax_file),
    url(r'^admin/', admin.site.urls),
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/assets/img/favicon.ico')),
    url('^(?P<app>(\w+))/(?P<function>(\w+))/$', process),
    url('^(?P<app>(\w+))/(?P<function>(\w+))/(?P<id>(\w+))/$', process),
    url('',views.index),

]
