# -*- coding:utf-8 -*-

import requests
import unittest
import json
import ast
import os
from BeautifulReport import BeautifulReport
import datetime
from AutoApiTest.utils.request_method import case_db_id

def case_run(**kwargs):
    '''
    运行用例，用例请求接口API
    :return:
    '''


    '''
    # 获取用户信息
    # x-origin-host: http://user-manage-test.smartcinema-inc.com
    # x-origin-path: /user/warning/queryUserInfo
    :return:
    '''

    request_info = kwargs['request_info']
    request_info = ast.literal_eval(request_info)
    # print(type(request_info))
    # print((request_info))
    method = request_info['method']
    headers = request_info['headers']
    host = request_info['host']
    path = request_info['path']
    params = request_info['params']
    data = request_info['data']

    if method == 'get':
        result = requests.get(url=host + path, headers=headers,params=params)
    if method == 'post':
        result = requests.post(url=host + path, headers=headers, data=data)

    resultJ = json.loads(result.content)
    # print(resultJ)
    return resultJ

# class TestCaseTemplate(unittest.TestCase):
#     def setUp(self):
#         print("======说明======")
#
#
#     def test_user_true(self):
#         case_singular = {
#             "code": 200,
#             "data": {
#                 "id": 1,
#                 "case_name": "第一个测试用例",
#                 "status": 1,
#                 "request_info": "{'method': 'get', 'headers': {'Content-Type': 'application/json', 'X-User-Id': '89'}, 'host': 'http://goods-manage-test.smartcinema-inc.com', 'path': '/outside/getGoodsFilmList', 'params': {'groundStatus': '1,2', 'screenType': '4,6,7,9,10,11'}, 'data': None}",
#                 "author": "陈航",
#                 "belong_project": "20",
#                 "belong_model": "522"
#             },
#             "msg": "success"
#         }
#         case_run(**case_singular)
#         self.assertEqual(1,2)


def main_run(test_case_path):
    '''
    生成测试报告
    :param test_case_path:
    :return:
    '''
    # test_case_path = os.path.join(os.getcwd(), "caseList")
    # print(test_case_path)
    # print(os.getcwd())

    # 测试报告名称
    now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
    reportPath =  'AutoApiTest/utils/testCase/report/'

    # 测试报告存放位置
    filename = now_time + 'requort.html'
    # filename_report = reportPath + filename

    # 测试报告存放位置
    reportPath = os.path.join(os.getcwd(), 'AutoApiTest/utils/testCase/report')
    # reportPath = 'report/'

    # 用例名称
    description = 'smartCinema_test '

    # testcase_dir_path = os.path.join(test_case_path, get_time_stamp())
    pattern = "*.py"
    test_suite = unittest.defaultTestLoader.discover(test_case_path,pattern=pattern)
    # os.remove('/Users/chenhang/Desktop/pythonFile/python/untitled/practice/Django-program/HttpRunnerManager/AutoApiTest/utils/testCase/Test0.py')
    result = BeautifulReport(test_suite)
    print('result', result)
    result_num = result.report(filename=filename,description=description,report_dir=reportPath)
    print('result_num',result_num)
    return filename

def loading_caseInfo(case_data):
    '''
    加载用例信息
    :return:
    '''

    print('case_data',case_data)

    # 判断是否有配置关联
    if case_data['type'] == 1:
        if case_data['include'] == None or case_data['include'] == '':

            case_info = {}
            case_info['belong_project'] = case_data['belong_project']
            case_info['belong_module'] = case_data['belong_module']
            case_info['case_name'] = case_data['case_name']
            case_info['case_data'] = case_data

            return case_info

        else:

            # 加载配置内容
            case_info = {}
            for k in case_data['include']:

                config_case = case_db_id(k)
                config_case_info = ast.literal_eval(config_case['request_info'])
                # print(config_case_info['headers'])
                # print(config_case_info['params'])
                # print(config_case_info['data'])

                # 将配置中的 params data headers 数据整合到 case的request_info 中
                case_request_info = ast.literal_eval(case_data['request_info'])
                case_request_info['params'] = {**config_case_info['params'],**case_request_info['params']}
                case_request_info['data'] = {**config_case_info['data'],**case_request_info['data']}
                case_request_info['headers'] = {**config_case_info['headers'],**case_request_info['headers']}


                # 整合用例信息
                # print(case_request_info)
                case_data['request_info'] = str(case_request_info)

                case_info['belong_project'] = case_data['belong_project']
                case_info['belong_module'] = case_data['belong_module']
                case_info['case_name'] = case_data['case_name']
                case_info['case_data'] = case_data
            print('case_data',case_data)

            return case_info

def write_testCase_py(test_case_path,**kwargs):
    '''
    创建测试用例py文件
    :param test_case_:
    :return:
    '''

    test_case_file = os.path.join(test_case_path , 'test_'+kwargs['case_name']+'.py')

    test_case_code = f"""
# -*- coding:utf-8 -*-

import unittest
from AutoApiTest.utils.testCase.testCase import case_run

class Test_{kwargs['belong_project']}(unittest.TestCase):
    def setUp(self):
        pass
    def test_{kwargs['belong_module']}_{kwargs['case_name']}(self):
        case_singular = {kwargs['case_data']}
        case_run(**case_singular)
        self.assertEqual(2,2)
"""

    with open(test_case_file,'w') as f:
        f.write(test_case_code)



# if __name__ == '__main__':

    # headers = {
    #     'Content-Type': 'application/json',
    #     'X-User-Id': '89',
    # }
    #
    # channel = 'test'
    # method = 'post'
    #
    # if method == 'get':
    #     host = f'http://goods-manage-{channel}.smartcinema-inc.com'
    #     path = '/outside/getGoodsFilmList'
    #
    #     params = {
    #         'groundStatus': '1,2',
    #         'screenType': '4,6,7,9,10,11'
    #     }
    #     data = None
    #
    # if method == 'post':
    #     host = f'http://user-manage-{channel}.smartcinema-inc.com'
    #     path = '/user/warning/queryUserInfo'
    #     params = None
    #     data = json.dumps({"department": "质量保障中心", 'departmentCode': "aih8"})
    # # caseInfo = case_info(method,host,path,headers,params,data)
    # # main_run(**caseInfo)

    # server_name = 'user_server'
    # model_name = 'userInfo'
    # case_name = '登录密码错误'


    # case_db_info={
    #     "code": 200,
    #     "data": {
    #         "id": 1,
    #         "case_name": "get_user_info",
    #         "status": 1,
    #         "request_info": {'method': 'get', 'headers': {'Content-Type': 'application/json', 'X-User-Id': '89'}, 'host': 'http://goods-manage-test.smartcinema-inc.com', 'path': '/outside/getGoodsFilmList', 'params': {'groundStatus': '1,2', 'screenType': '4,6,7,9,10,11'}, 'data': None},
    #         "author": "陈航",
    #         "belong_project": "smartcinema",
    #         "belong_model": "user_server"
    #     },
    #     "msg": "success"
    # }
    #
    # test_case_path = os.path.join(os.getcwd(),'caseList')
    # print(test_case_path)
    #
    # case_code_info = loading_caseInfo(case_db_info)
    # write_testCase_py(test_case_path,**case_code_info)
    # main_run(test_case_path)
