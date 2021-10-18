# -*- coding:utf-8 -*-
import time

import requests
import json
import os
import ast
from AutoApiTest.utils.common import paginator
from AutoApiTest.models import CaseInfo,ReportInfo,ProjectInfo,ModuleInfo


def case_db_id(id):
    '''
    # 通过id获取单个用例信息
    :param id:
    :return:
    '''
    case_singular = CaseInfo.objects.filter(id__exact=id)
    case_info_singular = {}
    for i in case_singular:
        case_info_singular['id'] = i.id
        case_info_singular['case_name'] = i.case_name
        case_info_singular['status'] = i.status
        case_info_singular['request_info'] = i.request_info
        case_info_singular['author'] = i.author
        case_info_singular['belong_project'] = i.belong_project
        case_info_singular['belong_mjodule'] = i.belong_module
        case_info_singular['type'] = i.type
        case_info_singular['include'] = i.include.split(',')
        case_info_singular['expect'] = i.expect
        case_info_singular['validate'] = i.validate
    # print(case_info_singular)

    return case_info_singular

def case_db_by_moduleId(id,caseType):
    '''
    # 通过模块id获取用例信息
    :param id:
    :return:
    '''
    case_singular = CaseInfo.objects.filter(belong_module__exact=id,type__exact=caseType)
    case_list = []
    case_info_singular = {}
    for i in case_singular:
        case_info_singular['id'] = i.id
        case_info_singular['case_name'] = i.case_name
        case_info_singular['status'] = i.status
        case_info_singular['request_info'] = i.request_info
        case_info_singular['author'] = i.author
        case_info_singular['belong_project'] = i.belong_project
        case_info_singular['belong_module'] = i.belong_module
        case_info_singular['type'] = i.type
        case_info_singular['include'] = i.include.split(',')

        case_list.append(case_info_singular)
        case_info_singular = {}
    # print(case_list)

    return case_list

'''接口参数化'''
def case_list_db(query,pagenum,perPage,type):
    '''
    # 查询用例列表
    :param query:
    :param pagenum:
    :param perPage:
    :return:
    '''
    if query == '' or query is None:
        case_info_obj = CaseInfo.objects.all().filter(type__contains=type).order_by('id')
    else:
        case_info_obj = CaseInfo.objects.filter(case_name__contains=query,type__contains=type).order_by('id')

    pagtor = paginator(case_info_obj,pagenum,perPage)
    pagesize = pagtor['pagesize']
    total = pagtor['total']
    pagedata = pagtor['pagedata']

    case_list = []
    case_info_singular = {}

    for i in pagedata:
        case_info_singular['id'] = i.id
        case_info_singular['case_name'] = i.case_name
        case_info_singular['status'] = i.status
        case_info_singular['request_info'] = i.request_info
        case_info_singular['author'] = i.author
        case_info_singular['belong_project'] = i.belong_project
        case_info_singular['belong_module'] = i.belong_module
        case_info_singular['type'] = i.type
        case_info_singular['include'] = i.include

        case_list.append(case_info_singular)
        case_info_singular = {}

    caseResult = {'code': 200, 'data': {'pagesize': pagesize, 'total': total, 'caseList': case_list}, 'msg': 'success'}
    # print(caseResult)
    return caseResult

def case_create_db(**kwargs):
    '''
    # 添加用例
    :param kwargs:
    :return:
    '''

    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    kwargs['create_time'] = create_time
    kwargs['update_time'] = update_time

    case_create_obj = CaseInfo.objects.create(**kwargs)

    return "pass"

def report_list_db(query,pagenum,perPage):
    '''
    查询测试报告列表
    :return:
    '''
    if query == '' or query is None:
        report_info_obj = ReportInfo.objects.all().order_by('id')
    else:
        report_info_obj = ReportInfo.objects.filter(report_name__contains=query).order_by('id')

    pagtor = paginator(report_info_obj,pagenum,perPage)
    pagesize = pagtor['pagesize']
    total = pagtor['total']
    pagedata = pagtor['pagedata']

    report_list = []
    report_info = {}

    for i in pagedata:
        report_info['id'] = i.id
        report_info['report_name'] = i.report_name
        report_info['status'] = i.status
        report_info['create_time'] = str(i.create_time)
        # report_info['update_time'] = i.update_time
        report_info['report_html'] = i.report_html

        report_list.append(report_info)
        report_info = {}

    reportResult = {'code': 200, 'data': {'pagesize': pagesize, 'total': total, 'reportList': report_list}, 'msg': 'success'}
    # print(reportResult)
    return reportResult

def report_create_db(reportName,test_report_path):
    '''
    # 测试报告入库
    :param request:
    :return:
    '''

    kwargs = {}

    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    kwargs['create_time'] = create_time
    kwargs['update_time'] = update_time

    report_filename = reportName
    report_dir = os.path.join(test_report_path,report_filename)

    with open(report_dir,'r',encoding='utf8') as f:
        report = f.read()
    kwargs['report_html'] = report
    kwargs['report_name'] = report_filename
    kwargs['status'] = 1
    ReportInfo.objects.create(**kwargs)
    # os.remove(report_path+report_filename)


def project_list_db(query,pagenum,perPage):
    '''
    获取项目列表
    :param query:
    :param pagenum:
    :param perPage:
    :return:
    '''

    if query == '' or query is None:
        project_info_obj = ProjectInfo.objects.all().order_by('id')
    else:
        project_info_obj = ProjectInfo.objects.filter(project_name__contains=query).order_by('id')

    pagtor = paginator(project_info_obj,pagenum,perPage)
    pagesize = pagtor['pagesize']
    total = pagtor['total']
    pagedata = pagtor['pagedata']

    project_list = []
    project_info = {}

    for i in pagedata:
        project_info['id'] = i.id
        project_info['project_name'] = i.project_name
        project_info['status'] = i.status
        project_info['test_user'] = i.test_user
        project_info['dev_user'] = i.dev_user
        project_info['responsible_name'] = i.responsible_name
        project_info['publish_app'] = i.publish_app
        project_info['simple_desc'] = i.simple_desc
        project_info['create_time'] = str(i.create_time)
        # project_info['update_time'] = i.update_time

        project_list.append(project_info)
        project_info = {}

    projectResult = {'code': 200, 'data': {'pagesize': pagesize, 'total': total, 'projectList': project_list}, 'msg': 'success'}
    # print(projectResult)
    return projectResult


def project_create_db():
    '''
    项目信息获取
    :return:
    '''

    kwargs = {}

    create_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    update_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    kwargs['create_time'] = create_time
    kwargs['update_time'] = update_time


def module_db_id(id):
    '''
    # 通过id获取单个模块信息
    :param id:
    :return:
    '''
    modulle_singular = ModuleInfo.objects.filter(id=id)
    modulle_info_singular = {}
    for i in modulle_singular:
        modulle_info_singular['id'] = i.id
        modulle_info_singular['module_name'] = i.module_name
        modulle_info_singular['status'] = i.status
        modulle_info_singular['test_user'] = i.test_user
        modulle_info_singular['belong_project_id'] = i.belong_project_id
        modulle_info_singular['simple_desc'] = i.simple_desc
        modulle_info_singular['create_time'] = str(i.create_time)
        # modulle_info_singular['update_time'] = i.update_time

    return modulle_info_singular

def module_db_by_projectId(id):
    '''
    # 通过项目id获取模块信息
    :param id:
    :return:
    '''
    module_singular = ModuleInfo.objects.filter(belong_project_id__exact=id)
    module_list = []
    modulle_info_singular = {}
    for i in module_singular:
        modulle_info_singular['id'] = i.id
        modulle_info_singular['module_name'] = i.module_name
        modulle_info_singular['status'] = i.status
        modulle_info_singular['test_user'] = i.test_user
        modulle_info_singular['belong_project_id'] = i.belong_project_id
        modulle_info_singular['simple_desc'] = i.simple_desc
        modulle_info_singular['create_time'] = str(i.create_time)
        # modulle_info_singular['update_time'] = i.update_time


        module_list.append(modulle_info_singular)
        modulle_info_singular = {}
    # print(case_list)

    return module_list



def module_list_db(query,pagenum,perPage):
    '''
    查询模块列表
    :param query:
    :param pagenum:
    :param perPage:
    :return:
    '''

    if query == '' or query is None:
        module_info_obj = ModuleInfo.objects.all().order_by('id')
    else:
        module_info_obj = ModuleInfo.objects.filter(module_name__contains=query).order_by('id')

    pagtor = paginator(module_info_obj,pagenum,perPage)
    pagesize = pagtor['pagesize']
    total = pagtor['total']
    pagedata = pagtor['pagedata']

    module_list = []
    module_info = {}

    for i in pagedata:
        module_info['id'] = i.id
        module_info['module_name'] = i.module_name
        module_info['status'] = i.status
        module_info['test_user'] = i.test_user
        module_info['belong_project_id'] = i.belong_project_id
        module_info['simple_desc'] = i.simple_desc
        module_info['create_time'] = str(i.create_time)
        # module_info['update_time'] = i.update_time

        module_list.append(module_info)
        module_info = {}

    moduleResult = {'code': 200, 'data': {'pagesize': pagesize, 'total': total, 'moduleList': module_list}, 'msg': 'success'}
    # print(projectResult)
    return moduleResult


def case_info(method,host,path,headers,params,data):
    ''''''

    caseInfo = {'method':method,'headers': headers, 'host': host, 'path': path,'params':params, 'data': data}
    print(caseInfo)
    return caseInfo


