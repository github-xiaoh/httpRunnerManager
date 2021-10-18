from django.shortcuts import render,redirect
from django.http import HttpResponse
from AutoApiTest.models import ReportInfo,CaseInfo,ModuleInfo
from AutoApiTest.utils.request_method import case_list_db,case_create_db,case_db_id,report_create_db,report_list_db,project_list_db,module_list_db,module_db_id,case_db_by_moduleId,module_db_by_projectId
from AutoApiTest.utils.testCase.testCase import loading_caseInfo,write_testCase_py,main_run
import json
import os
from django.utils.safestring import mark_safe
from AutoApiTest.tasks import test1,test2
from AutoApiTest.utils.operation import run_type_case,\
    case_data_merge,case_find_db

def get_test(request):
    case_info = ['1']
    result = module_db_by_projectId("1")
    # result = module_find_db(case_info)
    # result = case_data_merge('singular',case_info)

    return HttpResponse(json.dumps(result))

import time
def get_task1(request):
    test1.delay()
    print("执行task_1")
    return HttpResponse("task_1")

def get_task2(request):
    test2.delay()
    print("执行task_2")
    return HttpResponse("task_2")


def module_list(request):
    '''
    获取模块列表
    :param request:
    :return:
    '''
    if request.method == 'GET':
        pagenum = request.GET.get('pagenum')
        perPage = request.GET.get('pagesize')
        query = request.GET.get('query')
        project_id = request.GET.get('projectId')


        if (pagenum == None):pagenum = 1
        if (perPage == None):perPage = 10

        if project_id:
            by_project_module_list = module_db_by_projectId(project_id)
            moduleList = {'code': 200, 'data': {'pagesize': "嘿嘿", 'total': '呼呼', 'moduleList': by_project_module_list}, 'msg': 'success'}
        else:
            moduleList = module_list_db(query,pagenum,perPage)

        return HttpResponse(json.dumps(moduleList), content_type='application/json')


def project_list(request):
    '''
    获取项目列表
    :param request:
    :return:
    '''

    if request.method == 'GET':
        pagenum = request.GET.get('pagenum')
        perPage = request.GET.get('pagesize')
        query = request.GET.get('query')


        if (pagenum == None):pagenum = 1
        if (perPage == None):perPage = 10

        projectList = project_list_db(query,pagenum,perPage)

        return HttpResponse(json.dumps(projectList), content_type='application/json')


def case_report_html(request,reportStr):
    '''
    展示当前测试结果报告
    :param request:
    :return:
    '''

    if str(reportStr).isdigit():
        print('reportId', reportStr)
        report_info = {}
        info_db = ReportInfo.objects.get(id=reportStr)
        report_info['id'] = info_db.id
        report_info['report_name'] = info_db.report_name
        report_info['status'] = info_db.status
        report_info['create_time'] = str(info_db.create_time)
        # report_info['update_time'] = info_db.update_time
        report_info['report_html'] = info_db.report_html

        return HttpResponse(mark_safe(report_info['report_html']))
    else:
        print('fileName', reportStr)
        path = os.path.join(os.getcwd(), f'testData/testreport/{reportStr}')
        with open(path, 'r') as f:
            html_text = f.read()

        os.remove(path)

        return HttpResponse(mark_safe(html_text))


def case_list(request):
    '''
    # 获取、添加用例
    :param request:
    :return:
    '''

    if request.method == 'GET':
        pagenum = request.GET.get('pagenum')
        perPage = request.GET.get('pagesize')
        query = request.GET.get('query')
        case_type = request.GET.get('type')
        module_id = request.GET.get('moduleId')

        if (pagenum == None):pagenum = 1
        if (perPage == None):perPage = 10
        if (case_type == None):case_type = 1

        if module_id:
            by_module_case_list = case_db_by_moduleId(module_id,case_type)
            caseList = {'code': 200, 'data': {'pagesize': "嘿嘿", 'total': "呼呼", 'caseList': by_module_case_list}, 'msg': 'success'}
        else:
            caseList = case_list_db(query,pagenum,perPage,case_type)

        return HttpResponse(json.dumps(caseList), content_type='application/json')

    if request.method == 'POST':
        # 获取json请求数据
        json_str = request.body
        json_data = json.loads(json_str)
        print('json_data',json_data)

        if json_data['caseType'] == 1:
            json_data['request_info'] = {
                'method':json_data['reqMethod'],
                'host': 'http://goods-manage-test.smartcinema-inc.com',
                'path': json_data['path'],
                'headers': json_data['headers'],
                'params':json_data['params'],
                'data':json_data['data']
            }
            json_data['type'] = 1
            json_data.pop('reqMethod')
            json_data.pop('headers')
            json_data.pop('params')
            json_data.pop('data')
            # json_data.pop('path')

        if json_data['caseType'] == 2:

            json_data['request_info'] = {
                'host': 'http://goods-manage-test.smartcinema-inc.com',
                'path': json_data['path'],
                'headers': json_data['headers'],
                'params':json_data['params'],
                'data':json_data['data']
            }
            json_data['type'] = 2
            json_data.pop('headers')
            json_data.pop('params')
            json_data.pop('data')
            json_data.pop('path')

        print('json_data',json_data)
        json_data.pop('caseType')
        cs = case_create_db(**json_data)

        caseList = {'code': 200,'msg': 'success','data':cs}

        return HttpResponse(json.dumps(caseList), content_type='application/json')


def run_case(request):
    '''
    执行测试用例
    :param request:
    :return:
    '''

    if request.method == 'POST':
        # 获取json请求数据
        json_str = request.body
        json_data = json.loads(json_str)
        case_list_id = json_data['caseListId']

        if len(case_list_id)>1:
            case_list_id_new = []
            for case_info in case_list_id:
                case_list_id_new.append(case_info['id'])
            case_list_id = case_list_id_new

        # 确认测试路径
        test_path = os.path.join(os.getcwd(), 'testData')
        # 确定用例文件地址、报告路径
        test_case_path = os.path.join(test_path, 'testcase')
        test_report_path = os.path.join(test_path, 'testreport')

        # 执行测试用例
        report_filename = run_type_case("singular",case_list_id,test_path)

        # 测试报告入库
        report_create_db(report_filename,test_report_path)

        case = {'code': 200, 'data': {'fileName':report_filename}, 'msg': 'success'}
        return HttpResponse(json.dumps(case), content_type='application/json')

def run_module(request):
    '''
    运行模块用例
    :param request:
    :return:
    '''

    if request.method == 'POST':
        # 获取json请求数据
        json_str = request.body
        json_data = json.loads(json_str)
        module_list_id = json_data['moduleListId']

        if len(module_list_id) > 1:
            module_list_id_new = []
            for module_info in module_list_id:
                module_list_id_new.append(module_info['id'])
            module_list_id = module_list_id_new

        # 确认测试路径
        test_path = os.path.join(os.getcwd(), 'testData')
        # 确定用例文件地址、报告路径
        test_case_path = os.path.join(test_path, 'testcase')
        test_report_path = os.path.join(test_path, 'testreport')

        # 执行测试模块用例
        report_filename = run_type_case('module',module_list_id,test_path)

        # 测试报告入库
        report_create_db(report_filename,test_report_path)

        case = {'code': 200, 'data': {'fileName': report_filename}, 'msg': 'success'}
        return HttpResponse(json.dumps(case), content_type='application/json')



def report_list(request):
    '''
    # 获取测试报告列表
    :param request:
    :return:
    '''

    if request.method == 'GET':
        pagenum = request.GET.get('pagenum')
        perPage = request.GET.get('pagesize')
        query = request.GET.get('query')

        if (pagenum == None): pagenum = 1
        if (perPage == None): perPage = 10

        reportList = report_list_db(query, pagenum, perPage)
        # print(reportList)

        return HttpResponse(json.dumps(reportList), content_type='application/json')

    if request.method == 'POST':

        # 获取json请求数据
        # json_str = request.body
        # json_data = json.loads(json_str)
        # report_id = json_data['report_id']

        case = {'code': 200, 'data': {}, 'msg': 'success'}
        return HttpResponse(json.dumps(case), content_type='application/json')


'''
执行接口测试用例
'''




# Create your views here.
