# -*- coding:utf-8 -*-


from __future__ import absolute_import
from HttpRunnerManager.celery import app
from celery import shared_task
import time
from AutoApiTest.models import CaseInfo
from django.db import connections

from celery.task.base import periodic_task
from celery.schedules import crontab


# @app.tasks
# def modules():
#     pass


@periodic_task(run_every=crontab())
def test2_periodic_task1():
    print("定时任务发送5s")
    time.sleep(5)
    print("5s后定时任务执行完成")

@app.task
def test1():

    print("等了60s后执行1", time.sleep(60))
    with connections['auto_api_test'].cursor() as cursor:
        sqlStr = "INSERT INTO `cmsplatform`.`module_info`(`module_name`, `status`, `test_user`, `belong_project_id`, `simple_desc`) VALUES ('test', 1, 'test', 1, 'test')"
        cursor.execute(sqlStr)
    print("任务1",time.localtime(time.time()))

@shared_task
def test2():
    print("等了10s后执行2",time.sleep(10))
    print("任务2",time.localtime(time.time()))





