# -*- coding:utf-8 -*-

from django.conf.urls import url

from user_ch import views

urlpatterns = [
    url(r'^users',views.test_page,name='test_page'),
    url(r'^test_menus/$',views.test_menus,name='test_menus'),
    url(r'^reports',views.test_report,name='test_report'),
    url(r'^ticketcreateinc',views.operation_ticket_create_inc,name='tiicketcreateinc'),
    url(r'^ticketcreatezh',views.operation_ticket_create_zh,name='tiicketcreatezh'),
    url(r'^getcode',views.getCode,name='getcode'),
    url(r'^getfilmzh',views.getFilmZH,name='getfilmzh'),
    url(r'^createpremiere',views.createPremiere,name='createpremiere'),
    url(r'^createspecial',views.createSpecial,name='createspecial'),
    url(r'^createbaseInfo',views.createBaseInfo,name='createbaseInfo'),
    url(r'^createsyncFilm',views.createSyncFilm,name='createsyncFilm'),

]
