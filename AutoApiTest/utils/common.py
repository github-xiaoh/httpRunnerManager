# -*- coding:utf-8 -*-

from django.core.paginator import Paginator

def paginator(page_Info,pagenum=1, perPage=10):
    '''
    # 分页方法，返回分页相关数据
    :param page_Info:
    :param pagenum:
    :param perPage:
    :return:
    '''

    pagtor = Paginator(page_Info, per_page=perPage)
    pagesize = pagtor.num_pages
    total = pagtor.count
    pagedata = pagtor.page(pagenum).object_list
    pageInfo = {'pagesize':pagesize,'total':total,'pagedata':pagedata}

    return pageInfo

