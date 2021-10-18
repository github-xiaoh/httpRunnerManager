# -*- coding:utf-8 -*-

from django.conf.urls import url

from AutoApiTest import views

urlpatterns = [
    url(r'^projectlist',views.project_list,name='projectlist'),
    url(r'^modulelist',views.module_list,name='modulelist'),
    url(r'^caselist',views.case_list,name='caselist'),
    url(r'^runcase',views.run_case,name='runcase'),
    url(r'^runmodule',views.run_module,name='runmodule'),
    url(r'^gettask1',views.get_task1,name='gettask1'),
    url(r'^gettask2',views.get_task2,name='gettask2'),
    url(r'^get_test',views.get_test,name='get_test'),
    # url(r'^case_report_html/(?P<reportStr>(\d{4}-\d{1,2}-\d{1,2}-\d{1,2}:\d{1,2}:\d{1,2}requort.html$|\d+)?)',views.case_report_html,name='case_report_html'),
    # 单用例执行跳转使用正则 url
    url(r'^case_report_html/(?P<reportStr>\d{4}-\d{1,2}-\d{1,2}-\d{1,2}:\d{1,2}:\d{1,2}requort.html$)',views.case_report_html, name='case_report_html'),
    # 报告列表通过 ID 获取信息 ，与用例执行URL后续优化
    url(r'^case_report_html/(?P<reportStr>\d+)',views.case_report_html,name='case_report_html'),
    url(r'^reportList', views.report_list, name='reportList'),

]
