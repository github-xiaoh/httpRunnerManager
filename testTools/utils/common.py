# -*- coding:utf-8 -*-

import logging
import os
import re
from logging.handlers import TimedRotatingFileHandler

from django.core.paginator import Paginator
from django.utils.safestring import mark_safe


class Page():

    def __init__(self,request_url,page_page,info_data,mobile,user_name):
        '''

        :param request_url: 请求路由地址
        :param page_page: 请求页参数
        :param info_data: 查询数据结果
        :param mobile: 输入框参数
        :param user_name: 输入框参数
        '''

        self.request_url = request_url
        self.page_page = page_page
        self.info_data = info_data
        self.mobile = mobile
        self.user_name = user_name


    def html_str(self):

        # 当前请求的地址
        request_url = 'userInfo'
        # 最大显示的页数
        page_max = 11

        # 将查询到的数据按照每页5条数据进行分页
        paginator = Paginator(self.info_data, 5)

        # 获取总的页数
        page_num = paginator.num_pages
        print('获取总的页数：', page_num)

        page_page = int(self.page_page)
        page_start = page_page - 5
        page_end = page_page + 5
        if page_start <= 1:
            page_start = 1
            page_end = page_max

        if page_end >= page_num:
            page_end = page_num

        # print('page：',page[0])
        # print('page：', page)
        # for j in range(0,len(page)):
        #     print('page:',page[j].u_mobile)

        # 生成页码代码html
        htmlStr = ''
        for i in range(page_start, page_end + 1):
            htmlStr = htmlStr + ('<li>' + '<a href="' + '/{0}/' + str(
                i) + '/?user_phone={1}&user_name={2}">' + str(i) + '</a></li>').format(request_url, self.mobile, self.user_name)

        page_first = ('<li><a href="/{0}/1' +
                      '/?user_phone={1}&user_name={2}">' +
                      '首页</a></li>').format(request_url, self.mobile, self.user_name)
        page_last = (
                '<li><a href="/{0}/' +
                str(page_num) +
                '/?user_phone={1}&user_name={2}">尾页</a></li>').format(request_url, self.mobile, self.user_name)

        htmlStr = mark_safe(page_first + htmlStr + page_last)
        # print(htmlStr)
        # id = models.ClientUser.objects.get(id=420)
        # context = model_to_dict(id)

        return htmlStr

    def page_data(self):

        # 显示当前请求页面的数据
        page_data = Paginator(self.info_data, 5).page(self.page_page)

        return page_data

def setup_log(log_name):
    # 创建logger对象。传入logger名字
    logger = logging.getLogger(log_name)
    log_path = os.path.join("",log_name)
    print(log_path)
    # 设置日志记录等级
    logger.setLevel(logging.INFO)
    # interval 滚动周期，
    # when="MIDNIGHT", interval=1 表示每天0点为更新点，每天生成一个文件
    # backupCount  表示日志保存个数
    file_handler = TimedRotatingFileHandler(
        filename=log_path, when="MIDNIGHT", interval=1, backupCount=30
    )
    # filename="mylog" suffix设置，会生成文件名为mylog.2020-02-25.log
    file_handler.suffix = "%Y-%m-%d.log"
    # extMatch是编译好正则表达式，用于匹配日志文件名后缀
    # 需要注意的是suffix和extMatch一定要匹配的上，如果不匹配，过期日志不会被删除。
    file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}.log$")
    # 定义日志输出格式
    file_handler.setFormatter(
        logging.Formatter(
            "[%(asctime)s] [%(process)d] [%(levelname)s] - %(module)s.%(funcName)s (%(filename)s:%(lineno)d) - %(message)s"
        )
    )
    logger.addHandler(file_handler)
    return logger

logging_testTools = setup_log("testTools")

logging_testTools.info("输出日志11")
logging_testTools.info("输出日志22")
logging_testTools.info("输出日志33")

# path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(path)



class GetTimes():

    def __init__(self):
        print("")



