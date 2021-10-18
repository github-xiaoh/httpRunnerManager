# -*- coding:utf-8 -*-

from AutoApiTest.utils.request_method import case_list_db,case_create_db,\
    case_db_id,report_create_db,report_list_db,project_list_db,module_list_db,\
    module_db_id,case_db_by_moduleId,module_db_by_projectId
import ast
import os

def run_type_case(runType,data_list:list,test_path):
    # 依据类型查找、运行用例

    # 确定用例文件地址、报告地址
    test_case_path = os.path.join(test_path, 'testcase')
    test_report_path = os.path.join(test_path, 'testreport')

    if runType == 'singular':
        report_filename =  run_singular(runType,data_list,test_case_path,test_report_path)
        return report_filename

    if runType == 'module':
        report_filename = run_module(runType,data_list,test_case_path,test_report_path)
        return report_filename

    if runType == "project":
        run_project()

def run_project():
    pass

def run_module(runType,module_list_id:list,test_case_path,test_report_path):
    """
    # 运行单/多模块用例
    :param runType:
    :param module_list_id:
    :param test_case_path:
    :param test_report_path:
    :return:
    """

    # 加载模块信息
    module_case_list = case_data_merge(runType, module_list_id)
    # 生成用例文件
    case_write_py(module_case_list, test_case_path)
    # 生成测试报告
    report_filename = report_create(test_case_path, test_report_path)

    return report_filename

def run_singular(runType,case_list_id:list,test_case_path,test_report_path):
    """
    # 运行单/多用例
    :param runType:
    :param case_list_id:
    :param test_case_path:
    :param test_report_path:
    :return:
    """

    # 加载用例信息
    case_data_list = case_data_merge(runType,case_list_id)
    # 生成用例文件
    case_write_py(case_data_list,test_case_path)
    # 生成测试报告
    report_filename =  report_create(test_case_path,test_report_path)

    return report_filename


def case_data_merge(runType,list_id:list):
    # 整合用例信息

    # 依据类型查找用例

    if runType == 'singular':
        case_data = case_find_db(list_id)
        return case_data

    if runType == 'module':
        module_data = module_find_db(list_id)
        return module_data

    if runType == "project":
        project_data = project_find_db(list_id)
        return project_data


def case_write_py(case_data_list,test_case_path):
    """
    # 创建测试用例py文件 # 将用例信息数据保存为py文件
    :param case_data_list:
    :param test_case_path:
    :return:
    """

    for case_data in case_data_list:

        test_case_code = f"""
# -*- coding:utf-8 -*-

import unittest
from AutoApiTest.utils.operation import requests_case

class Test_{case_data['belong_project']}(unittest.TestCase):
    def setUp(self):
        pass

    def test_{case_data['belong_module']}_{case_data['case_name']}(self):
        ResultContent = requests_case({case_data})
        self.assertEqual('{case_data["expect"]}', {case_data['validate']},'验证是否成功！')

"""
        test_file_name = 'test_' + case_data['belong_project']+'_' + case_data['belong_module']+'_' + case_data['case_name'] + '.py'
        test_case_file = os.path.join(test_case_path, test_file_name)

        with open(test_case_file, 'w+') as f:
            f.write(test_case_code)
            f.close()

def project_find_db(project_list_id:list):
    # 查找项目信息
    project_case_data = []
    for project_info_id in project_list_id:

        # 获取模块下用例 该获取方法后续优化
        module_info = module_db_by_projectId(project_info_id)
    pass

def module_find_db(module_list_id:list):
    # 查找模块下用例信息
    # module_case_data_all = []
    module_case_data = []
    for module_info_id in module_list_id:

        # 获取模块下用例 该获取方法后续优化
        case_info = case_db_by_moduleId(module_info_id,1)
        module_case_data = module_case_data + case_info

    module_case_data_all = case_info_merge(module_case_data)

    return module_case_data_all

def case_find_db(case_list_id:list):
    # 查找用例信息
    case_data_all = []
    for case_info_id in case_list_id:
        case_data = case_db_id(id=case_info_id)
        case_data_all.append(case_data)
    case_data_all_new = case_info_merge(case_data_all)
    return case_data_all_new

def case_info_merge(case_data_list:list):
    # 该方法所有用例信息汇总
    # 用例集合 case_data_all
    case_data_all = []
    # 遍历测试用例列表
    for case_data in case_data_list:
        case_data_req = ast.literal_eval(case_data['request_info'])

        # 判断用例配置是否为空
        config_inclue_boolean = False
        for config_inclue in case_data['include']:
            if config_inclue:
                config_inclue_boolean = True
            else:
                config_inclue_boolean = False
        if config_inclue_boolean:
            # 非空整合配置数据
            config_info_list = config_find_db(case_data['include'])
            num = 1  # 计数为后续判断是第几次执行

            # 遍历配置列表获取每一个配置参数整合用例参数
            for config_req in config_info_list:
                config = ast.literal_eval(config_req['request_info'])
                # print('config:', config)
                # 判断params是否为None，None则不整合配置
                if case_data_req['params']:
                    if config['params']:
                        print("开始整合配置")
                        # print("case_data_req['params']",type(case_data_req['params']))
                        # print("config['params']",type(config['params']))
                        if len(config_info_list) > 1 and num > 1:
                            case_data_req['params'] = {**(case_data_req['params']),
                                                       **ast.literal_eval(config['params'])}
                        elif len(config_info_list) > 1 and num == 1:
                            case_data_req['params'] = {**ast.literal_eval(case_data_req['params']),
                                                       **ast.literal_eval(config['params'])}
                        else:
                            case_data_req['params'] = {**ast.literal_eval(case_data_req['params']),
                                                       **ast.literal_eval(config['params'])}
                else:
                    case_data_req['params'] = {}
                    if config['params']:
                        case_data_req['params'] = {**(case_data_req['params']),
                                                   **ast.literal_eval(config['params'])}
                # 判断data是否为None，None则不整合配置
                if case_data_req['data']:
                    if config['data']:
                        # print("case['data']", type(case['data']))
                        # print("config['data']:", type(config['data']))
                        if len(config_info_list) > 1 and num > 1:
                            case_data_req['data'] = {**(case_data_req['data']), **ast.literal_eval(config['data'])}
                        elif len(config_info_list) > 1 and num == 1:
                            case_data_req['data'] = {**ast.literal_eval(case_data_req['data']),
                                                     **ast.literal_eval(config['data'])}
                        else:
                            case_data_req['data'] = {**ast.literal_eval(case_data_req['data']),
                                                     **ast.literal_eval(config['data'])}
                else:
                    case_data_req['data'] = {}
                    if config['data']:
                        case_data_req['data'] = {**(case_data_req['data']),
                                                 **ast.literal_eval(config['data'])}
                # 判断headers是否为None，None则不整合配置
                if case_data_req['headers']:
                    if case_data_req['headers']:
                        # print("case['headers']", type(case['headers']))
                        # print("config['headers']:", type(config['headers']))
                        if len(config_info_list) > 1 and num > 1:
                            case_data_req['headers'] = {**case_data_req['headers'],
                                                        **ast.literal_eval(config['headers'])}
                        elif len(config_info_list) > 1 and num == 1:
                            case_data_req['headers'] = {**ast.literal_eval(case_data_req['headers']),
                                                        **ast.literal_eval(config['headers'])}
                        else:
                            case_data_req['headers'] = {**ast.literal_eval(case_data_req['headers']),
                                                        **ast.literal_eval(config['headers'])}
                else:
                    case_data_req['headers'] = {}
                    if config['headers']:
                        case_data_req['headers'] = {**case_data_req['headers'], **ast.literal_eval(config['headers'])}
                num += 1

            case_data['request_info'] = case_data_req

        # elif config_inclue_boolean == None or config_inclue_boolean == '':
        #     case_data_all.append(case_data)
        else:
            if case_data_req['headers']:
                case_data_req['headers'] = ast.literal_eval(case_data_req['headers'])
            else:
                case_data_req['headers'] = {}
            if case_data_req['data']:
                case_data_req['data'] = ast.literal_eval(case_data_req['data'])
            else:
                case_data_req['data'] = {}
            if case_data_req['params']:
                case_data_req['params'] = ast.literal_eval(case_data_req['params'])
            else:
                case_data_req['params'] = {}

            case_data['request_info'] = case_data_req

        case_data_all.append(case_data)
        print("case_data_all", case_data_all)
    return case_data_all


def config_find_db(config_list:list):
    # 查找配置信息
    config_data = []
    for config_info_id in config_list:
        config_data_one = case_db_id(config_info_id)
        config_data.append(config_data_one)
    print("config_data",config_data)
    return config_data


import requests
import json
def requests_case(case_data:dict):
    '''
    # 运行接口,请求API
    :param case_data:
    :return:
    '''

    case_req = case_data['request_info']

    method = case_req['method']
    headers = case_req['headers']
    host = case_req['host']
    path = case_req['path']
    params = case_req['params']
    data = case_req['data']

    if method == 'get':
        result = requests.get(url=host + path, headers=headers,params=params)
    if method == 'post':
        result = requests.post(url=host + path, headers=headers, data=data)

    resultJ = json.loads(result.content)
    # print(resultJ)
    return resultJ


import datetime
import unittest
from BeautifulReport import BeautifulReport
def report_create(test_case_path,test_report_path):
    """
    # 生成测试报告
    :param test_case_path:
    :param test_report_path:
    :return:
    """

    # 测试报告名称
    filename = datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + 'requort.html'
    print('filename',filename)

    # 用例名称
    description = 'smartCinema_test '

    # 用例检测文件格式
    pattern = "*.py"
    test_suite = unittest.defaultTestLoader.discover(test_case_path, pattern=pattern)

    # 生成测试报告文件
    report_result = BeautifulReport(test_suite).report(description=description,report_dir=test_report_path,filename=filename)

    return filename
