
# -*- coding:utf-8 -*-

import unittest
from AutoApiTest.utils.operation import requests_case

class Test_20(unittest.TestCase):
    def setUp(self):
        pass

    def test_1_one_test_case(self):
        ResultContent = requests_case({'id': 1, 'case_name': 'one_test_case', 'status': 1, 'request_info': {'method': 'get', 'headers': {'Content-Type': 'application/json', 'X-User-Id': '89'}, 'host': 'http://goods-manage-test.smartcinema-inc.com', 'path': '/outside/getGoodsFilmList', 'params': {'groundStatus': '1,2', 'screenType': '4,6,7,9,10,11'}, 'data': {}}, 'author': '陈航', 'belong_project': '20', 'belong_module': '1', 'type': 1, 'include': ['21', '25'], 'expect': 'success', 'validate': "ResultContent['msg']"})
        self.assertEqual('success', ResultContent['msg'],'验证是否成功！')

