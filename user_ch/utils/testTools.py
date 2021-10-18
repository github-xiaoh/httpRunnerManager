# -*- coding:utf-8 -*-


import requests
import json


def getCodeInfo(platform,regionId,channel,mobile):

    if platform == 'client':
        if regionId == '0':
            path = 'clientLogin/getCode'
            if channel == 'test':
                ip = '172.19.36.182'
                url = f'http://{ip}:8080/{path}'
            elif channel == 'prod':
                ip = '172.16.231.61'
                url = f'http://{ip}:8080/{path}'
        elif regionId == '1':
            path = 'clientPassport/getCode'
            if channel == 'test':
                ip = '172.26.186.145'
                url = f'http://{ip}:8080/{path}'
            elif channel == 'prod':
                ip = '172.27.4.24'
                url = f'http://{ip}:8080/{path}'
    elif platform == 'h5':
        if regionId == '0':
            path = 'web/getCode'
            if channel == 'test':
                ip = '172.19.36.182'
                url = f'http://{ip}:8080/{path}'
            elif channel == 'prod':
                ip = '172.16.231.61'
                url = f'http://{ip}:8080/{path}'
        elif regionId == '1':
            path = 'clientPassport/getCode'
            if channel == 'test':
                ip = '172.26.186.145'
                url = f'http://{ip}:8080/{path}'
            elif channel == 'prod':
                ip = '172.27.4.24'
                url = f'http://{ip}:8080/{path}'
    else: return {"code": 0,"msg": "success","data": '获取请求数据无效，导致URL拼接错误'}


    params = {'mobile':mobile}

    result = requests.get(url=url,params=params)
    resultJ = json.loads(result.content)
    # print(resultJ)

    return resultJ


# getCodeInfo('client','0','prod','18403558966')
