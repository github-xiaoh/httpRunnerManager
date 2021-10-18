from django.test import TestCase


import os

if __name__ == '__main__':
    # 加载Django项目配置信息
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HttpRunnerManager.settings")
    # 导入启动Django项目
    import django
    django.setup()

    # 以下为正常Django项目使用
    from AutoApiTest import models

    case_info = models.ModuleInfo.objects.first()
    print(case_info.belong_project_id)

    # project_info = case_info.ProjectInfo.objects.all()
    # print(project_info)

    from django.db import connections

    connections.close_all()
    with connections['auto_api_test'].cursor() as cursor:
        cursor.execute('select * from `cmsplatform`.`project_info`')

        project = cursor.fetchall()
        print(project)

        cursor.execute("INSERT INTO `cmsplatform`.`module_info`(`module_name`, `status`, `test_user`, `belong_project_id`, `simple_desc`) VALUES ('test', 1, 'test', 1, 'test')")

        module = cursor.fetchall()
        if module:
            print(module)

        cursor.execute('select * from `cmsplatform`.`module_info` INNER JOIN `cmsplatform`.`project_info` ON `cmsplatform`.`module_info`.`belong_project_id` = `cmsplatform`.`project_info`.`id` ')

        models_project = cursor.fetchall()
        print(models_project)

        cursor.execute('select * from `cmsplatform`.`module_info`')

        module = cursor.fetchall()
        print(module)

    print("++++++++++++++=====测试测试测试=====+++++++++++")

    a = {
        'id': 22,
        'case_name': '123',
        'status': 1,
        'request_info': '{\'method\': \'get\', \'headers\': None, \'host\': \'http://goods-manage-test.smartcinema-inc.com\', \'path\': \'/outside/getGoodsFilmList\', \'params\': "{\'groundStatus\': \'1,2\', \'screenType\': \'4,6,7,9,10,11\'}", \'data\': None}',
        'author': '123',
        'belong_project': '123',
        'belong_module': '2',
        'type': 1,
        'include': ['','']
    }
    for i in a['include']:
        if i:
            print(len(a['include']))
        else:
            print("kkong")

    print("++++++++++++++=====测试测试测试=====+++++++++++")

    case = {
        'id': 1,
        'case_name': 'one_test_case',
        'status': 1,
        'request_info': {
            'method': 'get',
            'headers': {
                'Content-Type': 'application/json',
                'X-User-Id': '89'
            },
            'host': 'http://goods-manage-test.smartcinema-inc.com',
            'path': '/outside/getGoodsFilmList',
            'params': {
                'groundStatus': '1,2',
                'screenType': '4,6,7,9,10,11'
            },
            'data': {}
        }
    }

    import unittest
    from AutoApiTest.utils.operation import requests_case

    class Test_kk_oo(unittest.TestCase):
        def setUp(self):
            pass

        def test_OO_XX(self):
            response = requests_case(case)
            self.assertEqual(2, 3)

    if __name__ == '__main__':
        unittest.main()


print("++++++++++++++==========+++++++++++")



print("++++++++++++++=====测试测试测试=====+++++++++++")




# Create your tests here.
