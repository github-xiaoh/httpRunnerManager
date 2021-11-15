
# -*- coding:utf-8 -*-

import unittest
from AutoApiTest.utils.testCase.testCase import case_run

class Test_20(unittest.TestCase):
    def setUp(self):
        pass
    def test_1_two_test_case(self):
        case_singular = {'id': 2, 'case_name': 'two_test_case', 'status': 1, 'request_info': '{\'method\': \'post\', \'headers\': {\'Content-Type\': \'application/json\', \'X-User-Id\': \'89\'}, \'host\': \'http://user-manage-test.smartcinema-inc.com\', \'path\': \'/user/warning/queryUserInfo\', \'params\': {}, \'data\': \'{"department": "\\\\u8d28\\\\u91cf\\\\u4fdd\\\\u969c\\\\u4e2d\\\\u5fc3", "departmentCode": "aih8"}\'}', 'author': '陈航', 'belong_project': '20', 'belong_module': '1', 'type': 1, 'include': ''}
        case_run(**case_singular)
        self.assertEqual(2,2)
