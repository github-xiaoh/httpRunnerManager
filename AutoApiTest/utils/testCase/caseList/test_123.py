
# -*- coding:utf-8 -*-

import unittest
from AutoApiTest.utils.testCase.testCase import case_run

class Test_123(unittest.TestCase):
    def setUp(self):
        pass
    def test_2_123(self):
        case_singular = {'id': 22, 'case_name': '123', 'status': 1, 'request_info': "{'method': 'get', 'headers': {'Content-Type': 'application/json', 'X-User-Id': '89'}, 'host': 'http://goods-manage-test.smartcinema-inc.com', 'path': '/outside/getGoodsFilmList', 'params': {'groundStatus': '1,2', 'screenType': '4,6,7,9,10,11'}, 'data': {}}", 'author': '123', 'belong_project': '123', 'belong_module': '2', 'type': 1, 'include': ''}
        case_run(**case_singular)
        self.assertEqual(2,2)
