
# -*- coding:utf-8 -*-

import unittest
from AutoApiTest.utils.testCase.testCase import case_run

class Test_211(unittest.TestCase):
    def setUp(self):
        pass
    def test_1_阿拉斯加(self):
        case_singular = {'id': 24, 'case_name': '阿拉斯加', 'status': 1, 'request_info': '{\'method\': \'post\', \'headers\': {\'Content-Type\': \'application/json\', \'X-User-Id\': \'89\'},\'host\': \'http://goods-manage-test.smartcinema-inc.com\', \'path\': \'/outside/getGoodsFilmList\', \'params\': "{\'sff\':\'f\'}", \'data\': "{\'sff\':\'f\'}"}', 'author': '信息', 'belong_project': '211', 'belong_module': '1', 'type': 1, 'include': ''}
        case_run(**case_singular)
        self.assertEqual(2,2)
