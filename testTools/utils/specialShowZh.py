# -*- coding:utf-8 -*-

import requests
import json
from releasefilm import getTimes


filmTime = getTimes()
startTime = filmTime[2]

print(startTime)



def special_show_zh():
    host = 'http://activity-manage-test.smartcinema-inc.com'
    path = '/inner/activity/addPremiere'

    headers = {
        'Content-Type':'application/json',
        'X-User-Id':'89'
    }

    data = json.dumps({
        "filmId":4994894073919712,
        "filmName":"测试20分钟电影",
        "spuId":"8fRMmGwCKfZXfiF",
        "spuReleaseStartTime":1598889600,
        "spuReleaseEndTime":1730390399,
        "name":"测试20分钟电影首映礼",
        "subName":"测试20分钟电影主题介绍",
        "remark":"测试20分钟电影描述",
        "beignTime":startTime,
        "beautifyStatus":1,
        "userNum":1000,
        "interactionType":1,
        "projectionStatus":1,
        "roomId":0,
        "backPictureUrl":""
    })

    result = requests.post(url=host+path,data=data,headers=headers)
    resultJ = json.loads(result.content)
    print(resultJ)
    return resultJ


def sort_user(roomId):

    host = 'http://activity-manage-test.smartcinema-inc.com'
    path = '/inner/activity/interactive/addCast'

    headers = {
        'Content-Type': 'application/json',
        'X-User-Id': '89'
    }

    data = json.dumps(
        {
            "roomId": 213121,
            "interactiveList": "[{\"userId\":12059,\"checked\":1}]"
        }
    )

    result = requests.post(url=host+path,data=data,headers=headers)
    resultJ = json.loads(result.content)
    print(resultJ)


def host_user(roomId):

    host = 'http://activity-manage-test.smartcinema-inc.com'
    path = '/inner/activity/interactive/addCompere'

    headers = {
        'Content-Type': 'application/json',
        'X-User-Id': '89'
    }

    data = json.dumps({
        "phone": "18403558945",
        "roomId": roomId
    })

    result = requests.post(url=host+path,data=data,headers=headers)
    resultJ = json.loads(result.content)
    print(resultJ)


def img_save(roomId):

    host = 'http://activity-manage-test.smartcinema-inc.com'
    path = '/inner/activity/editBackPicture'

    headers = {
        'Content-Type': 'application/json',
        'X-User-Id': '89'
    }

    data = json.dumps({
        "activityImgUrl":"https://g.smartcinema.com.cn/images/50297d17bc9f45cb92acff8a399f5db1-1675-1358.jpg",
        "backPictureUrl":"https://g.smartcinema.com.cn/images/911cfec56a474fd6b0f35d5d991eebb5-1125-900.jpg",
        "roomId":roomId
    })

    result = requests.post(url=host+path,data=data,headers=headers)
    resultJ = json.loads(result.content)
    print(resultJ)


def activity_info(roomId):

    host = 'http://activity-manage-test.smartcinema-inc.com'
    path = '/inner/activity/studio/editActivityDesc'

    headers = {
        'Content-Type': 'application/json',
        'X-User-Id': '89'
    }

    data = json.dumps({
        "activeStatus":1,
        "roomId":roomId,
        "activityDescList":[{"time":"2021-04-23 12:24:30","title":"走上红毯"},
                            {"time":"2021-04-23 12:34:30","title":"发布正式开始"},
                            {"time":"2021-04-23 12:49:30","title":"测试20分钟电影正式首映"}]
    })

    result = requests.post(url=host+path,data=data,headers=headers)
    resultJ = json.loads(result.content)
    print(resultJ)


def activity_shareType(roomId):

    host = 'http://activity-manage-test.smartcinema-inc.com'
    path = '/inner/activity/studio/editShare'

    headers = {
        'Content-Type': 'application/json',
        'X-User-Id': '89'
    }

    data = json.dumps({
        "shareType":2,
        "shareUrlType":3,
        "roomId":roomId
    })

    result = requests.post(url=host+path,data=data,headers=headers)
    resultJ = json.loads(result.content)
    print(resultJ)

def interaction_methods(roomId):

    host = 'http://activity-manage-test.smartcinema-inc.com'
    path = '/inner/activity/studio/editHuDongInfo'

    headers = {
        'Content-Type': 'application/json',
        'X-User-Id': '89'
    }

    data = json.dumps({
        "activityName":" ",
        "headBgUrl":"https://g.smartcinema.com.cn/images/23ead67774074d4aa7c648977e78f7f7-1125-264.png",
        "bottomBgUrl":"https://g.smartcinema.com.cn/images/fd0fb7dfe4164d858c43f11a2704f8d7-1125-1539.jpg",
        "warmLiveUrl":"http://183.207.249.14/PLTV/3/224/3221225550/index.m3u8",
        "celebrateLiveUrl":"http://183.207.249.14/PLTV/3/224/3221225550/index.m3u8",
        "shareStatus":1,
        "liveShareUrl":"https://www.baidu.com",
        "interactionShareUrl":"https://g.smartcinema.com.cn/images/6a1c1cab86bc4e57baf009401a90f17e-200-112.png",
        "liveShareTitle":"测试主标题",
        "liveShareContent":"测试副标题",
        "type":3,
        "roomId":roomId
    })

    result = requests.post(url=host+path,data=data,headers=headers)
    resultJ = json.loads(result.content)
    print(resultJ)




# 创建专场
# roomInfo = special_show_zh()
# roomId = roomInfo['data']['id']
# print('创建首映礼场次号：{}'.format(roomId))

# 添加主创人员
# sort_user(roomId)

# 添加主持人
# host_user(roomId)

# 添加图片配置
# img_save(roomId)

# 添加活动节目单
# activity_info(roomId)

# 添加活动分享类型
# activity_shareType(roomId)

# 添加互动方式
# interaction_methods(roomId)


