# -*- coding:utf-8 -*-

import requests
import json
import datetime
import time


def req_url(host,url):
    channel = 'http'
    server_str = "aws"
    if server_str == "ali":
        host_str = '.smartcinemausa.com'
    else:
        host_str = ".smartcinema-inc.com"


    if host == "media":
        host ="media-manage-test" + host_str
    elif host == "goods":
        host = "goods-manage-test" + host_str
    elif host == "cms":
        host = "cms-manage-test" + host_str
    elif host == "activity":
        host = "activity-manage-test" + host_str
    elif host == "ucenter":
        host = "ucenter-manage-test" + host_str
    elif host == "operation":
        host = "operation-manage-test" + host_str
    elif host == "user":
        host = "user-manage-test" + host_str
    else:
        reqUrl = False
        print("服务host匹配失败")
        return reqUrl
    if server_str == "ali":
        reqUrl = channel + "://" + host + url
    else:
        reqUrl = channel + "://" + server_str + "-" + host + url
    print('请求地址：',reqUrl)
    return reqUrl

# print(req_url('user','/aa/cc/bb'))
def getTimes():

    nowt = time.time()

    nowt_s = int(nowt)
    nowt_ms = int(round(nowt * 1000))

    # 时间戳打印
    print("原始时间数据:", nowt)  # 原始时间数据
    print("秒级时间戳  :", nowt_s)  # 秒级时间戳
    print("毫秒级时间戳:", nowt_ms)  # 毫秒级时间戳

    # 获取当前时间
    now_time = datetime.datetime.now()
    print(now_time)

    # 时间加减
    nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间
    nowtime = datetime.datetime.strptime(
        nowtime, '%Y-%m-%d %H:%M:%S')  # 当前时间格式转换
    nowtime_future30 = nowtime + datetime.timedelta(days=30)  # 获取当前时间30天之后的日期
    nowtime_old30 = nowtime - datetime.timedelta(days=30)
    print('当前时间：', nowtime)
    print("前时间30天之后的日期", nowtime_future30)
    print("前时间30天之前的日期", nowtime_old30)

    # 将str类型时间转换成时间戳
    # dt = "2016-05-05 20:28:54"
    nowtime_str = str(nowtime_future30)
    # 转换成时间数组
    timeArray = time.strptime(nowtime_str, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = int(time.mktime(timeArray))
    print("字符串转换后的时间戳：", timestamp)
    print('\n\n\n')

    # 将时间戳转换为时间

    return nowt_s, timestamp,nowt_ms
getTimes()

def mediaAddsource(filmName,regionId):
    """

    :param filmName:
    :param regionId:
    :return:
    """
    reqUrl = req_url('media', "/filmSource/add")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {
            "filmName": filmName,
        }
    )

    result = requests.post(url=url, headers=headers, data=body)
    resultJ = json.loads(result.content)
    return resultJ

def mediaGetfilmList(filmName,regionId):
    """

    :param filmName:
    :param regionId:
    :return:
    """
    reqUrl = req_url('media', "/filmInfo/list")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers =  {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = {'filmName': filmName}

    result = requests.get(url=url,headers=headers,params=body)
    resultJ = json.loads(result.content)
    return resultJ



def mediaSendFilm(filmId, filmName,regionId):
    """

    :param filmId:
    :param filmName:
    :param regionId:
    :return:
    """
    reqUrl = req_url('media', "/filmInfo/saveBaseInfo")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {
            "filmId": filmId,
            "filmDefaultName": 1,
            "filmCountries": "133,82,243,244,92",
            "filmSubtitle": "1",
            "filmLanguage": "1",
            "filmCategories": "20,64,86",
            "international": {
                "en_US": {
                    "filmName": "testSource" + filmName,
                    "filmRecommend": "Recommended language",
                    "filmBackgroundImage": "https://g.smartcinemausa.com/images/7008fb6615004d4c949f0812fb4a9d63-691-294.png",
                    "filmVrBackgroundImage": "https://g.smartcinemausa.com/images/e8c6a57638d44c70a8e6f8d798941b6d-443-633.jpg",
                    "filmIntro": "According to the real event of Sichuan Airlines flight 3u8633 successfully handled on May 14, 2018. During the flight mission, the crew encountered the extremely rare dangerous situation that the windshield of the cockpit burst and fell off and the cockpit pressure was released at an altitude of 10000 meters. At the critical moment of life, they did not act in disorder, responded decisively and dealt with correctly, ensuring the life safety of all the people on board and creating a miracle in the history of civil aviation in the world."},
                "zh_CN": {
                    "filmName": filmName,
                    "filmRecommend": "测试不推荐你看这个影片",
                    "filmBackgroundImage": "https://g.smartcinemausa.com/images/7008fb6615004d4c949f0812fb4a9d63-691-294.png",
                    "filmVrBackgroundImage": "https://g.smartcinemausa.com/images/e8c6a57638d44c70a8e6f8d798941b6d-443-633.jpg",
                    "filmIntro": "根据2018年5月14日四川航空3U8633航班机组成功处置特情真实事件改编。机组执行航班任务时，在万米高空突遇驾驶舱风挡玻璃爆裂脱落、座舱释压的极端罕见险情，生死关头，他们临危不乱、果断应对、正确处置，确保了机上全部人员的生命安全，创造了世界民航史上的奇迹。"},
                "zh_TW": {
                    "filmName": "臺灣繁體" + filmName,
                    "filmRecommend": "測試不推薦你看這部影片",
                    "filmBackgroundImage": "",
                    "filmVrBackgroundImage": "",
                    "filmIntro": "根據2018年5月14日四川航空3U8633航班機組成功處置特情真實事件改編。機組執行航班任務時，在萬米高空突遇駕駛艙風擋玻璃爆裂脫落、座艙釋壓的極端罕見險情，生死關頭，他們臨危不亂、果斷應對、正確處置，確保了機上全部人員的生命安全，創造了世界民航史上的奇跡。"},
                "ko_KR": {
                    "filmName": "한국어" + filmName,
                    "filmRecommend": "測試不推薦你看這部影片",
                    "filmBackgroundImage": "",
                    "filmVrBackgroundImage": "",
                    "filmIntro": "2018 년 5 월 14 일 에 쓰 촨 항공 3U 8633 편 비행기 팀 이 특수 상황 실 화 를 성공 적 으로 처리 한 것 에 따라 각색 되 었 다.승무원 들 이 항공 편 임 무 를 수행 할 때 만 미터 고공 에서 갑자기 조종 석 바람막이 유리 가 파열 되 고 좌석 이 분해 되 는 극히 드 문 위험한 상황, 생사 의 고비 에 그들 은 위험 에 직면 하여 어 지 럽 지 않 고 과감하게 대응 하 며 정확 한 처 리 를 하여 비행기의 모든 인원 들 의 생명 안전 을 확보 하고 세계 민간 항공 역사상 기적 을 창조 했다."},
                "zh_HK": {
                    "filmName": "香港繁體" +filmName,
                    "filmRecommend": "測試不推薦你看這部影片",
                    "filmBackgroundImage": "",
                                "filmVrBackgroundImage": "",
                                "filmIntro": "根據2018年5月14日四川航空3U8633航班機組成功處置特情真實事件改編。機組執行航班任務時，在萬米高空突遇駕駛艙風擋玻璃爆裂脫落、座艙釋壓的極端罕見險情，生死關頭，他們臨危不亂、果斷應對、正確處置，確保了機上全部人員的生命安全，創造了世界民航史上的奇跡。"},
            },
            "filmLength": "120",
            "limitLevel": 2,
            "filmCreator": "Test piece",
            "movieCode": "sdcaDDS",
            "licenseCode": "sdWe3",
            "filmSource": 1})

    result = requests.post(url=url, headers=headers, data=body)
    resultJ = json.loads(result.content)
    return resultJ


def mediaAddcastInfo():
    """
    :return:
    """
    reqUrl = req_url('media', "/filmCast/saveFilmCastList")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': '2',
    }
    body = json.dumps(
        {
            "filmId": 4934007395236725,
            "castList": [{
                "castId": 4886219191944844,
                "phone": "",
                "headImage": "https://g.smartcinemausa.com/images/1e4e91eb2d674d64a8922b9530525e94-649-649.jpg",
                "international": {
                    "zh_TW": {
                        "castName": "導演信命",
                        "filmRoleName": "導演角色"
                    },
                    "zh_CN": {
                        "castName": "导演姓名",
                        "filmRoleName": "导演角色"
                    },
                    "en_US": {
                        "castName": "Name of director",
                        "filmRoleName": "Director role"
                    }
                },
                "filmRoleId": "2",
                "roleId": None,
                "idx": 1
            }, {
                "castId": 4886219191944845,
                "phone": "",
                "headImage": "https://g.smartcinemausa.com/images/3239d1b2a1ee4a4a87e6a2f534812e8e-658-658.jpg",
                "international": {
                    "zh_TW": {
                        "castName": "繁体主演姓名",
                        "filmRoleName": "繁体主演角色"
                    },
                    "zh_CN": {
                        "castName": "简体主演姓名",
                        "filmRoleName": "简体主演角色"
                    },
                    "en_US": {
                        "castName": "Starring name",
                        "filmRoleName": "Starring role"
                    }
                },
                "filmRoleId": "1",
                "roleId": None,
                "idx": 2
            }, {
                "castId": 4886219191944846,
                "phone": "",
                "headImage": "https://g.smartcinemausa.com/images/33687cfa20fa49a3b064e4e884d8efe7-900-900.jpg",
                "international": {
                    "zh_TW": {
                        "castName": "我是編劇",
                        "filmRoleName": "編劇人"
                    },
                    "zh_CN": {
                        "castName": "我是编剧",
                        "filmRoleName": "编剧人"
                    },
                    "en_US": {
                        "castName": "Screenwriter",
                        "filmRoleName": "Screenwriter json"
                    }
                },
                "filmRoleId": "4",
                "roleId": None,
                "idx": 3
            }, {
                "castId": 4886219191944847,
                "phone": "",
                "headImage": "https://g.smartcinemausa.com/images/d5f54a31a1e5466f991b50dc31eb024f-441-441.jpg",
                "international": {
                    "zh_TW": {
                        "castName": "我是群演",
                        "filmRoleName": "路人丁"
                    },
                    "zh_CN": {
                        "castName": "我是群演",
                        "filmRoleName": "路人丁"
                    },
                    "en_US": {
                        "castName": "我是群演",
                        "filmRoleName": "路人丁"
                    }
                },
                "filmRoleId": "101",
                "roleId": None,
                "idx": 4
            }]
        }
    )

    result = requests.post(url=url, headers=headers, data=body)
    resultJ = json.loads(result.content)
    return resultJ


def mediaAddphoto(filmId,regionId):
    """
    :param filmId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('media', "/filmImage/save")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps({
        "filmId": filmId,
        "international": {
            "en_US": {"images": [
                {"imageType": 1,
                 "imageSort": 0,
                 "imageUrl": "https://g.smartcinemausa.com/images/a9f172f04f4c4cdf82e4127e637f40e6-1057-1511.jpg"},
                {"imageType": 2,
                 "imageSort": 0,
                 "imageUrl": "https://g.smartcinemausa.com/images/9bbbd9e2712f447dbdda7f0ff382df76-1125-633.jpg"},
                {"imageType": 3,
                 "imageSort": 0,
                 "imageUrl": "https://g.smartcinemausa.com/images/8f224d123b6d43278caa652cd82a248c-1125-759.jpg"},
                {"imageType": 4,
                 "imageSort": 0,
                 "imageUrl": "https://g.smartcinemausa.com/images/52f1ae560b4d41c2b0868b5ab97c699e-1057-1511.jpg"},
                {"imageType": 5,
                 "imageSort": 0,
                 "imageUrl": "https://g.smartcinemausa.com/images/3b96924913d144f2a392e2e8601fd3d5-291-433.jpg"},
                {"imageType": 5,
                 "imageSort": 1,
                 "imageUrl": "https://g.smartcinemausa.com/images/315a20197f834e0989eaa5fb9c5ffc93-275-466.jpg"},
                {"imageType": 5,
                 "imageSort": 2,
                 "imageUrl": "https://g.smartcinemausa.com/images/43039ab9beaa47cf8c28b07e58e8b86f-466-466.jpg"},
                {"imageType": 5,
                 "imageSort": 3,
                 "imageUrl": "https://g.smartcinemausa.com/images/e06f7f5825cb467bb766bca5aad3ede8-433-433.jpg"},
                {"imageType": 5,
                 "imageSort": 4,
                 "imageUrl": "https://g.smartcinemausa.com/images/f95de75c95c242c3b50459713d1a939d-1500-817.jpg"},
                {"imageType": 5,
                 "imageSort": 5,
                 "imageUrl": "https://g.smartcinemausa.com/images/bab9bb24a9124abd86d4e8456ab09c7e-800-450.jpg"},
                {"imageType": 5,
                 "imageSort": 6,
                 "imageUrl": "https://g.smartcinemausa.com/images/2db25661eddc4e71b34c83a103047360-700-393.jpg"},
                {"imageType": 5,
                 "imageSort": 7,
                 "imageUrl": "https://g.smartcinemausa.com/images/5145a8d134404c71a38c2c3d4bd6ca8e-1024-576.jpg"},
                {"imageUrl": "https://g.smartcinemausa.com/images/5ed0dd0355844a6d97a5a751b81dcde7-650-433.jpg",
                 "imageType": 6,
                 "imageSort": 0},
                {"imageUrl": "https://g.smartcinemausa.com/images/efdc3d01bbbd4289b8061d5eea97b874-1500-1000.jpg",
                 "imageType": 6,
                 "imageSort": 1},
                {"imageUrl": "https://g.smartcinemausa.com/images/b378ea0c9cde48269111130cb13b9305-800-533.jpg",
                 "imageType": 6,
                 "imageSort": 2},
                {"imageUrl": "https://g.smartcinemausa.com/images/9e643c514cc946c68d400768f678b28a-700-466.jpg",
                 "imageType": 6,
                 "imageSort": 3},
                {"imageUrl": "https://g.smartcinemausa.com/images/aeda69af1e7c496bb97858585d04b0a6-700-466.jpg",
                 "imageType": 6,
                 "imageSort": 4},
                {"imageUrl": "https://g.smartcinemausa.com/images/2bfc5e66e877406182d538eb7e657a35-700-466.jpg",
                 "imageType": 6,
                 "imageSort": 5},
                {"imageUrl": "https://g.smartcinemausa.com/images/7aa6da023be34136b599de50221b7367-1024-682.jpg",
                 "imageType": 6,
                 "imageSort": 6},
                {"imageType": 7,
                 "imageSort": 0,
                 "imageUrl": "https://g.smartcinemausa.com/images/7e503a2d2d7f4721954e3698168f2c42-1080-1491.jpg"}]},
            "zh_CN": {"images": [
                {"imageType": 1,
                 "imageSort": 0,
                 "imageUrl": "https://g.smartcinemausa.com/images/a9f172f04f4c4cdf82e4127e637f40e6-1057-1511.jpg"},
                {"imageType": 2,
                 "imageSort": 0,
                 "imageUrl": "https://g.smartcinemausa.com/images/9bbbd9e2712f447dbdda7f0ff382df76-1125-633.jpg"},
                {"imageType": 3,
                 "imageSort": 0,
                 "imageUrl": "https://g.smartcinemausa.com/images/8f224d123b6d43278caa652cd82a248c-1125-759.jpg"},
                {"imageType": 4,
                 "imageSort": 0,
                 "imageUrl": "https://g.smartcinemausa.com/images/52f1ae560b4d41c2b0868b5ab97c699e-1057-1511.jpg"},
                {"imageType": 5,
                 "imageSort": 0,
                 "imageUrl": "https://g.smartcinemausa.com/images/3b96924913d144f2a392e2e8601fd3d5-291-433.jpg"},
                {"imageType": 5,
                 "imageSort": 1,
                 "imageUrl": "https://g.smartcinemausa.com/images/315a20197f834e0989eaa5fb9c5ffc93-275-466.jpg"},
                {"imageType": 5,
                 "imageSort": 2,
                 "imageUrl": "https://g.smartcinemausa.com/images/43039ab9beaa47cf8c28b07e58e8b86f-466-466.jpg"},
                {"imageType": 5,
                 "imageSort": 3,
                 "imageUrl": "https://g.smartcinemausa.com/images/e06f7f5825cb467bb766bca5aad3ede8-433-433.jpg"},
                {"imageType": 5,
                 "imageSort": 4,
                 "imageUrl": "https://g.smartcinemausa.com/images/f95de75c95c242c3b50459713d1a939d-1500-817.jpg"},
                {"imageType": 5,
                 "imageSort": 5,
                 "imageUrl": "https://g.smartcinemausa.com/images/bab9bb24a9124abd86d4e8456ab09c7e-800-450.jpg"},
                {"imageType": 5,
                 "imageSort": 6,
                 "imageUrl": "https://g.smartcinemausa.com/images/2db25661eddc4e71b34c83a103047360-700-393.jpg"},
                {"imageType": 5,
                 "imageSort": 7,
                 "imageUrl": "https://g.smartcinemausa.com/images/5145a8d134404c71a38c2c3d4bd6ca8e-1024-576.jpg"},
                {"imageUrl": "https://g.smartcinemausa.com/images/5ed0dd0355844a6d97a5a751b81dcde7-650-433.jpg",
                 "imageType": 6,
                 "imageSort": 0},
                {"imageUrl": "https://g.smartcinemausa.com/images/efdc3d01bbbd4289b8061d5eea97b874-1500-1000.jpg",
                 "imageType": 6,
                 "imageSort": 1},
                {"imageUrl": "https://g.smartcinemausa.com/images/b378ea0c9cde48269111130cb13b9305-800-533.jpg",
                 "imageType": 6,
                 "imageSort": 2},
                {"imageUrl": "https://g.smartcinemausa.com/images/9e643c514cc946c68d400768f678b28a-700-466.jpg",
                 "imageType": 6,
                 "imageSort": 3},
                {"imageUrl": "https://g.smartcinemausa.com/images/aeda69af1e7c496bb97858585d04b0a6-700-466.jpg",
                 "imageType": 6,
                 "imageSort": 4},
                {"imageUrl": "https://g.smartcinemausa.com/images/2bfc5e66e877406182d538eb7e657a35-700-466.jpg",
                 "imageType": 6,
                 "imageSort": 5},
                {"imageUrl": "https://g.smartcinemausa.com/images/7aa6da023be34136b599de50221b7367-1024-682.jpg",
                 "imageType": 6,
                 "imageSort": 6},
                {"imageType": 7,
                 "imageSort": 0,
                 "imageUrl": "https://g.smartcinemausa.com/images/7e503a2d2d7f4721954e3698168f2c42-1080-1491.jpg"}
            ]}
        }
    })

    result = requests.post(url=url, headers=headers, data=body)
    resultJ = json.loads(result.content)
    return resultJ


def mediaGetPostiticeTitle(filmId, filmName,regionId):
    """

    :param filmId:
    :param filmName:
    :param regionId:
    :return:
    """
    reqUrl = req_url('media', "/filmPositive/list")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = {
        'filmId': filmId,
        'filmName': filmName,
        'limit': '20',
        'page': '1',
    }

    result = requests.get(url=url, headers=headers, params=body)
    resultJ = json.loads(result.content)
    return resultJ


def mediaAddvideo(filmId,regionId):
    """

    :param filmId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('media', "/filmVideo/save")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {
            "filmId": filmId,
            "videoList": [{
                "videoName": "Video name",
                "videoType": "1",
                "videoLength": 10,
                "isDisplay": 1,
                "international":
                {
                    "en_US": {
                        "videoImgUrl": "https://g.smartcinemausa.com/images/0d7c892ec9a04568917a4023b281ecda-700-393.jpg",
                        "videoUrl": "http://smart-java-test.smartcinemausa.com/trailer/1584690775131_28rN4.mp4"
                    },
                    "zh_CN": {
                        "videoImgUrl": "https://g.smartcinemausa.com/images/0d7c892ec9a04568917a4023b281ecda-700-393.jpg",
                        "videoUrl": "http://smart-java-test.smartcinemausa.com/trailer/1584690775131_28rN4.mp4"
                    },
                }
            }]
        }
    )

    result = requests.post(url=url, headers=headers, data=body)
    resultJ = json.loads(result.content)
    return resultJ


def mediaAddTitleValue(filmId, filmName,regionId):
    """

    :param filmId:
    :param filmName:
    :param regionId:
    :return:
    """
    reqUrl = req_url('media', "/filmPositive/list")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = {
        'filmId': filmId,
        'filmName': filmName,
        'limit': 20,
        'page': 1,
    }
    result = requests.get(url=url, headers=headers, params=body)
    resultJ = json.loads(result.content)
    return resultJ


def goodsAddspu(filmId, filmName, startTime, endtime,regionId):
    """

    :param filmId:
    :param filmName:
    :param startTime:
    :param endtime:
    :param regionId:
    :return:
    """
    reqUrl = req_url('goods', "/spu/addProduct")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }

    body = json.dumps({
        "filmId": filmId,
        "filmName": filmName,
        "spuTag": "[\"院线同步\"]",
        "spuReleaseStartTime": startTime,
        "spuReleaseEndTime": endtime,
        "spuType": 1,
    })

    result = requests.post(url=url, headers=headers, data=body)
    resultJ = json.loads(result.content)
    return resultJ


def goodsGetpositive(movieId,regionId):
    """

    :param movieId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('goods', "/mediaApi/getFilmData")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {
            "movieId": movieId
        }
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ

def goodsEditProduct(spuId,filmName,startTime,endTime,regionId):
    """

    :param spuId:
    :param filmName:
    :param startTime:
    :param endTime:
    :param regionId:
    :return:
    """
    reqUrl = req_url('goods', "/spu/editProduct")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {
            "spuName":filmName,
            "spuId":spuId,
            "spuTag":"[\"院线同步\"]",
            "isThrowingScreen":1,
            "spuType":1,
            "spuReleaseStartTime": startTime,
            "spuReleaseEndTime":endTime
        }
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ


def goodsAddsku(filmId,spuName,spuId,goodsPositive,startTime,endTime,regionId):
    """

    :param filmId:
    :param spuName:
    :param spuId:
    :param goodsPositive:
    :param startTime:
    :param endTime:
    :param regionId:
    :return:
    """
    reqUrl = req_url('goods', "/goods/addGoods")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {
            "fileLanguage": 1,
            "videoClarity": 1,
            "isClarity": 1,
            "videoCaption": 1,
            "videoType": 1,
            "spuId": spuId,
            "filmId": filmId,
            "spuName": spuName,
            "spuCoverImage": "",
            "sortNum": 0,
            "spuTag": "[\"院线同步\"]",
            "spuDescribe": "",
            "positiveTitleValue": goodsPositive,
            "screenType": "公映场",
            "standardPrice": 0,
            "releasePrice": 0,
            "basePrice": 0,
            "iosPrice": 0,
            "settlementPrice": 0,
            "isActivity": 0,
            "stockNum": 0,
            "onlineStartTime": startTime,
            "onlineEndTime": endTime,
            "releaseStartTime": startTime,
            "releaseEndTime": endTime,
            "spuStartTime": startTime,
            "spuEndTime": endTime,
            "ysSellStartTime": 0,
            "ysSellEndTime": 0,
            "zcSellStartTime": 0,
            "zcSellEndTime": 0,
            "yxViewStartTime": 0,
            "yxViewEndTime": 0,
            "audioId": 0
        }
    )

    result = requests.post(url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ

def goodsUpdateSku(spuId,filmId,spuName,skuId,goodsPositive,spuStartTime,spuEndTime):
    """

    :param spuId:
    :param filmId:
    :param spuName:
    :param skuId:
    :param goodsPositive:
    :param spuStartTime:
    :param spuEndTime:
    :return:
    """
    reqUrl = req_url('goods', "/goods/goodsUpdate")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {
            "fileLanguage": 1,
            "videoClarity": 1,
            "isClarity": 1,
            "videoCaption": 1,
            "videoType": 1,
            "spuId": spuId,
            "filmId": filmId,
            "spuName": spuName,
            "spuCoverImage": "",
            "productId": 104,
            "skuId": skuId,
            "sortNum": 0,
            "spuTag": "[\"院线同步\"]",
            "spuDescribe": "",
            "positiveTitleValue": goodsPositive,
            "screenType": "专场",
            "stockNum": 50,
            "standardPrice": 25,
            "releasePrice": 0,
            "basePrice": 25,
            "iosPrice": 25,
            "settlementPrice": 10,
            "isActivity": 1,
            "servicePrice": 10,
            "iosServicePrice": 10,
            "activityPrice": 0,
            "onlineStartTime": spuStartTime,
            "onlineEndTime": spuEndTime,
            "releaseStartTime": spuStartTime,
            "releaseEndTime": spuEndTime,
            "spuStartTime": spuStartTime,
            "spuEndTime": spuEndTime,
            "ysSellStartTime": 0,
            "ysSellEndTime": 0,
            "zcSellStartTime": 0,
            "zcSellEndTime": 0,
            "yxViewStartTime": 0,
            "yxViewEndTime": 0,
            "audioId": 0
        }
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ

def goodsGetSku(spuId,regionId):
    """

    :param spuId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('goods', "/goods/getGoodsList")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {
            "spuId": spuId,
            "groundStatus": "",
            "environment": "",
            "page": 1,
            "limit": 20
        }
    )

    result =  requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ

def goodsEditSkuChannel(skuId,regionId):
    """

    :param skuId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('goods', "/sku/updateGroup")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {
            "skuId": skuId,
            "groupNum": "40,41,42,43"
        }
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ

def goodsEditSkuEnvironment(skuId,regionId):
    """

    :param skuId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('goods', "/sku/updateEnvironment")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {
            "skuId": skuId,
            "environment": "1,2"
        }
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ

def goodsEditSkuExamine(skuId,regionId):
    """

    :param skuId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('goods', "/sku/updateExamine")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {
            "skuId": skuId,
            "examine": 1
        }
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ

def goodsEditSkuGoodsStatus(filmId,skuId,regionId):
    """

    :param filmId:
    :param skuId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('goods', "/sell/updateGoodsStatus")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {
            "skuId": skuId,
            "filmId": filmId,
            "groundStatus": 1
        }
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ

def cmsFilmRelease(filmId,regionId):
    """
    :param filmId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('cms', "/cmsFilm/releaseFilm")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': regionId,
    }
    body = json.dumps(
        {"filmId":filmId}
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ


def getGuestData(regionId):
    """

    :param regionId:
    :return:
    """
    reqUrl = req_url('ucenter', "/ucenter/getGuestData")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': str(regionId),
    }
    body = {}

    result = requests.get(url=url, headers=headers, params=body)
    resultJ = json.loads(result.content)
    return resultJ


def getPreProSpuList(regionId):
    """
    :param regionId:
    :return:
    """
    reqUrl = req_url('goods', "/spu/getPreProSpuList")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': str(regionId),
    }
    body = json.dumps({
        "filmName": "",
        "type": 1
    })

    result = requests.post(url=url, headers=headers, data=body)
    resultJ = json.loads(result.content)
    return resultJ

def editRoom(specialName,filmName,spuReleaseEndtime,spuReleaseStartTime,spuId,filmId,userName,userId,regionId,startTime,synopsis):
    """
    :param specialName: 专场名称
    :param filmName: 影片名称
    :param spuReleaseEndtime: SPU下映时间
    :param spuReleaseStartTime: SPU上映时间
    :param spuId: SPUID
    :param filmId: 影片ID
    :param userName: 用户名称
    :param userId: 用户ID
    :param regionId: 请求区域ID
    :param startTime: 专场开始时间
    :return: 返回response信息
    """
    reqUrl = req_url('activity', "/inner/activity/editRoom")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': str(regionId),
    }
    body = json.dumps(
        {
            "international": {
                "ko_KR": {
                    "name": "测试-" + specialName,
                    "warmVoiceRecord": "",
                    "backPictureUrl": "https://g.smartcinemausa.com/images/f27d83b8088042fbaffc3141950989d4-700-466.jpg",
                    "activityImgUrl": "https://g.smartcinemausa.com/images/cdf8e8668a3841088f1e4f9ee669bfff-700-466.jpg",
                    "remark": synopsis + "한글 은 테스트 에 사용 되 는 데 이 터 를 장의 별로 의미 있 는 표현 이 아니다.",
                    "filmName": "한국어" + filmName,
                    "spuReleaseEndtime": spuReleaseEndtime,
                    "spuReleaseStartTime": spuReleaseStartTime,
                    "spuId": spuId,
                    "filmId": filmId,
                    "userName": userName,
                    "userRemark": userName,
                    "userImage": "",
                    "userId": userId,
                    "drawerList": []
                },
                "zh_TW": {
                    "name": "测试-" + specialName,
                    "warmVoiceRecord": "",
                    "backPictureUrl": "https://g.smartcinemausa.com/images/f27d83b8088042fbaffc3141950989d4-700-466.jpg",
                    "activityImgUrl": "https://g.smartcinemausa.com/images/cdf8e8668a3841088f1e4f9ee669bfff-700-466.jpg",
                    "remark": synopsis + "繁体场次描述用来测试的数据，不是很有意义的一段语言描述繁体繁体.",
                    "filmName": "繁体" + filmName,
                    "spuReleaseEndtime": spuReleaseEndtime,
                    "spuReleaseStartTime": spuReleaseStartTime,
                    "spuId": spuId,
                    "filmId": filmId,
                    "userName": userName,
                    "userRemark": userName,
                    "userImage": "",
                    "userId": userId,
                    "drawerList": []
                },
                "zh_CN": {
                    "name": "测试-" + specialName,
                    "warmVoiceRecord": "",
                    "backPictureUrl": "https://g.smartcinemausa.com/images/f27d83b8088042fbaffc3141950989d4-700-466.jpg",
                    "activityImgUrl": "https://g.smartcinemausa.com/images/cdf8e8668a3841088f1e4f9ee669bfff-700-466.jpg",
                    "remark": synopsis + "简体场次描述用来测试的数据，不是很有意义的一段语言描述",
                    "filmName": filmName,
                    "spuReleaseEndtime": spuReleaseEndtime,
                    "spuReleaseStartTime": spuReleaseStartTime,
                    "spuId": spuId,
                    "filmId": filmId,
                    "userName": userName,
                    "userRemark": userName,
                    "userImage": "",
                    "userId": userId,
                    "drawerList": []
                },
                "en_US": {
                    "name": "测试-" + specialName,
                    "warmVoiceRecord": "",
                    "backPictureUrl": "https://g.smartcinemausa.com/images/f27d83b8088042fbaffc3141950989d4-700-466.jpg",
                    "activityImgUrl": "https://g.smartcinemausa.com/images/cdf8e8668a3841088f1e4f9ee669bfff-700-466.jpg",
                    "remark": synopsis + "Korean session description is used to test the data, not a very meaningful language description",
                    "filmName": "testSource" + filmName,
                    "spuReleaseEndtime": spuReleaseEndtime,
                    "spuReleaseStartTime": spuReleaseStartTime,
                    "spuId": spuId,
                    "filmId": filmId,
                    "userName": userName,
                    "userRemark": userName,
                    "userImage": "",
                    "userId": userId,
                    "drawerList": []
                }
            },
            "spuId": spuId,
            "userNum": 80,
            "userId": userId,
            "beignTime": startTime,
            "playType": 0,
            "showOwnerPhoto": True,
            "filmId": filmId,
            "type": 1,
            "roomId": 0,
            "celebrateVideoCover": "https://g.smartcinemausa.com/images/bfbf4ea0ec2144a48fcd91975d339a66-700-466.jpg",
            "celebrateVideoType": 2,
            # "celebrateVideoUrl": "http://183.207.249.14/PLTV/3/224/3221225550/index.m3u8",  # 科教频道
            "warmVideoCover": "https://g.smartcinemausa.com/images/c2dbefb027464822bc2d5092ffadd9cc-1500-1000.jpg",
            "warmVideoType": 1,
            "warmVideoUrl": "http://smart-java-test.smartcinemausa.com/trailer/1595493080563_ieWQc.MP4",
            "celebrateVideoUrl": "http://smart-java-test.smartcinemausa.com/trailer/1595493080563_ieWQc.MP4",
        }
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ

def editDrawerInfo(roomId,userName,filmName,regionId):
    """
    :param roomId:
    :param userName:
    :param filmName:
    :param regionId:
    :return:
    """
    reqUrl = req_url('activity', "/inner/activity/editDrawerInfo")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': str(regionId),
    }
    body = json.dumps(
        {
            "roomId": roomId,
            "international": {
                "ko_KR": {
                    "drawerList": [{
                        "type": 1,
                        "show": 1,
                        "title": "전용관",
                        "userName": userName,
                        "userImage": "",
                        "userRemark": userName
                    }, {
                        "type": 2,
                        "show": 1,
                        "title": "영화",
                        "filmName": filmName,
                        "filmType": "코믹/다큐멘터리/로맨스",
                        "filmImg": "",
                        "descInfo": "根据2018年5月14日四川航空3U8633航班机组成功处置特情真实事件改编。机组执行航班任务时，在万米高空突遇驾驶舱风挡玻璃爆裂脱落、座舱释压的极端罕见险情，生死关头，他们临危不乱、果断应对、正确处置，确保了机上全部人员的生命安全，创造了世界民航史上的奇迹。",
                        "subTitle": "",
                        "content": ""
                    }, {
                        "type": 3,
                        "show": 1,
                        "title": "주 제목 사용자 정의",
                        "subTitle": "사용자 정의 눈 에 띄 는 내용",
                        "content": "사용자 정의 내용 을 사용 하여 H5 전단 전시 에 사용 합 니 다."
                    }]
                },
                "en_US": {
                    "drawerList": [{
                        "type": 1,
                        "show": 1,
                        "title": "Host introduction",
                        "userName": userName,
                        "userImage": "",
                        "userRemark": userName
                    }, {
                        "type": 2,
                        "show": 1,
                        "title": "Movie information",
                        "filmName": filmName,
                        "filmType": "Comedy/Documentary/Romance",
                        "filmImg": "https://g.smartcinemausa.com/images/a9f172f04f4c4cdf82e4127e637f40e6-1057-1511.jpg",
                        "descInfo": "根据2018年5月14日四川航空3U8633航班机组成功处置特情真实事件改编。机组执行航班任务时，在万米高空突遇驾驶舱风挡玻璃爆裂脱落、座舱释压的极端罕见险情，生死关头，他们临危不乱、果断应对、正确处置，确保了机上全部人员的生命安全，创造了世界民航史上的奇迹。",
                        "subTitle": "",
                        "content": ""
                    }, {
                        "type": 3,
                        "show": 1,
                        "title": "Custom main title",
                        "content": "Custom content for H5 front display",
                        "subTitle": "Customize eye-catching content"
                    }]
                },
                "zh_CN": {
                    "drawerList": [{
                        "type": 1,
                        "show": 1,
                        "title": "场主介绍",
                        "userName": userName,
                        "userImage": "",
                        "userRemark": userName
                    }, {
                        "type": 2,
                        "show": 1,
                        "title": "影片介绍",
                        "filmName": filmName,
                        "filmType": "喜剧/纪录片/爱情",
                        "filmImg": "https://g.smartcinemausa.com/images/a9f172f04f4c4cdf82e4127e637f40e6-1057-1511.jpg",
                        "descInfo": "根据2018年5月14日四川航空3U8633航班机组成功处置特情真实事件改编。机组执行航班任务时，在万米高空突遇驾驶舱风挡玻璃爆裂脱落、座舱释压的极端罕见险情，生死关头，他们临危不乱、果断应对、正确处置，确保了机上全部人员的生命安全，创造了世界民航史上的奇迹。",
                        "subTitle": "",
                        "content": ""
                    }, {
                        "type": 3,
                        "show": 1,
                        "title": "自定义主标题",
                        "subTitle": "自定义醒目内容",
                        "content": "自定义内容，用来H5前段展示使用"
                    }]
                },
                "zh_TW": {
                    "drawerList": [{
                        "type": 1,
                        "show": 1,
                        "title": "場主介紹",
                        "userName": userName,
                        "userImage": "",
                        "userRemark": userName
                    }, {
                        "type": 2,
                        "show": 1,
                        "title": "影片介紹",
                        "filmName": "新建影片测试直播",
                        "filmType": "喜劇/紀錄片/愛情",
                        "filmImg": "",
                        "descInfo": "根据2018年5月14日四川航空3U8633航班机组成功处置特情真实事件改编。机组执行航班任务时，在万米高空突遇驾驶舱风挡玻璃爆裂脱落、座舱释压的极端罕见险情，生死关头，他们临危不乱、果断应对、正确处置，确保了机上全部人员的生命安全，创造了世界民航史上的奇迹。",
                        "subTitle": "",
                        "content": ""
                    }, {
                        "type": 3,
                        "show": 1,
                        "title": "自定义主标题",
                        "subTitle": "自定义醒目内容",
                        "content": "自定义内容，用来H5前段展示使用"
                    }]
                },
            }
        }
    )

    result = requests.post(url=url, headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ



def getRoomData(filmId,regionId):
    """
    :param filmId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('activity', "/inner/activity/getRoomData")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'X-Region-Id': str(regionId),
    }
    body = {
        "size": 20,
        "page": 1,
        'status': 0,
        'filmId': filmId,
        'filmName':'',
        'type':1,
        'begin': "",
        'end': "",
        'userName': "",
        'onlineStatus':0,
    }

    result = requests.get(url=url,headers=headers,params=body)
    resultJ = json.loads(result.content)
    return resultJ


def updateStatus(roomId,regionId):
    """
    :param roomId:
    :param regionId:
    :return:
    """
    reqUrl = req_url('activity', "/inner/activity/updateStatus")
    if reqUrl:
        url = reqUrl
    else:
        return "服务host匹配失败"

    headers = {
        'Content-Type': 'application/json',
        'X-Region-Id': str(regionId),
    }
    body = json.dumps(
        {
            "roomId": roomId,
            "onlineStatus": 1
        }
    )

    result = requests.post(url=url,headers=headers,data=body)
    resultJ = json.loads(result.content)
    return resultJ




# filmTime = getTimes()
# startTime = filmTime[2]
#
# print(startTime)


# star_info_result = getGuestData(1)
# spu_list_result = getPreProSpuList(1)
# print(star_info_result)
# print(spu_list_result)
#
#
# star_info = []
# spu_list = []
#
# i=0
# for star in star_info_result['data']:
#     if star['userId'] == 532:
#         print("判断成功")
#         break
#     print(star['nickname'])
#     print(star['userId'])
#     star_info.append(star['nickname'])
#     print("==============信息提取%s================="%(str(i)))
#
#
# print("=========================信息分割==========================")
# for spu in spu_list_result['data']:
#     # print("한국어"+spu['filmName'])
#     # print(spu['spuReleaseEndtime'])
#     # print(spu['spuReleaseStartTime'])
#     # print(spu['spuId'])
#     # print(spu['filmId'])
#
#     spu_list.append(spu['filmName'])
#     print("==============信息提取%s=================" % (str(i)))
#
# context = {'star_info':star_info_result['data'],'spu_list':spu_list_result['data']}
#
# print(context)



filmName = "한국어测试影片影迷"
regionId = '3'
specialName = "专场名称定制004"
spuReleaseEndtime = 1596211199
spuReleaseStartTime = 1590940800
spuId = "UFrLVfOc3t0BPZe"
filmId = 4932917517541910
userName = "开飞机的熟客了"
userId = 532

# 编辑场信息

# room_info = editRoom(specialName,filmName,spuReleaseEndtime,spuReleaseStartTime,spuId,filmId,userName,userId,regionId,startTime)
# print("专场信息：",room_info)
#
# roomId = room_info['data']['id']
#
# print("编辑场信息:：",editDrawerInfo(869,"user8945wu","北美测试直播KOL",1))
#
# # 获取专场列表信息，用于寻找skuId
# special_list = getRoomData(filmId,regionId)
# print("专场列表信息",special_list)
#
# special_info = special_list['data']['list']
# print("单个专场信息：",special_info)
#
# for room_id in special_info:
#     print("房间信息结果：",room_id)
#     if room_id['roomId'] == roomId:
#         sku_id = room_id['skuId']
#         film_id = room_id['filmId']
#         break
#     else:
#         continue
#
# print(sku_id,film_id)
#
# # 配置上线"预发"环境
# print('配置上线"预发"环境：',goodsEditSkuEnvironment(sku_id,regionId))
#
# # 审核通过
# print('审核通过：',goodsEditSkuExamine(sku_id,regionId))
#
# # 配置上线"线上"环境
# print('配置上线"线上"环境：',goodsEditSkuEnvironment(sku_id,regionId))
#
# # 配置绑定渠道
# print('配置绑定渠道：',goodsEditSkuChannel(sku_id,regionId))
#
# # 配置上架商品
# print('配置上架商品：',goodsEditSkuGoodsStatus(film_id,sku_id,regionId))
#
# # 查找正片信息ID
# print("正片信息查询：",goodsGetpositive(filmId,regionId)['data'][0])
# goodsPositive = goodsGetpositive(filmId,regionId)['data'][0]['positive'][0]['value']
# print("查找影片正片ID：",goodsPositive)
#

# sku_id = 911
# goodsPositive = 5014674026632768
# print('修改商品价格：',goodsUpdateSku(spuId,filmId,filmName,sku_id,goodsPositive,spuReleaseStartTime,spuReleaseEndtime))
#
# # 配置专场上线
# print('配置专场上线：',updateStatus(roomId,regionId))








# filmTime = getTimes()
# startTime = filmTime[0]
# endTime = filmTime[1]



# print("添加片源：",mediaAddsource(filmName,regionId))
#
# mediaGetfilmlist = mediaGetfilmList(filmName,regionId)
# print(mediaGetfilmlist)
# filmId = mediaGetfilmlist['data']['list'][0]['filmId']
# print("搜索影片列表：",mediaGetfilmlist)
# print("依据搜索的影片列表查找影片ID：",filmId)
#
# print("在站点发布影片：",mediaSendFilm(filmId,filmName,regionId))
# print("为影片添加图片信息：",mediaAddphoto(filmId,regionId))
# print("为影片添加视频信息：",mediaAddvideo(filmId,regionId))
# print("查找影片正片ID(废弃)：",mediaGetPostiticeTitle(filmId,filmName,regionId))
#
# print("正片信息查询：",goodsGetpositive(filmId,regionId)['data'][0])
# goodsPositive = goodsGetpositive(filmId,regionId)['data'][0]['positive'][0]['value']
# print("查找影片正片ID：",goodsPositive)
# spuId = goodsGetpositive(filmId,regionId)['data'][0]['spuId']
# print("查找影片SpuID",spuId)
#
# print("编辑商品信息：",goodsEditProduct(spuId,filmName,startTime,endTime,regionId))
# print("添加商品SPU：",goodsAddspu(filmId,filmName,startTime,endTime,regionId))
#
# print("添加商品SKU：",goodsAddsku(filmId,filmName,spuId,goodsPositive,startTime,endTime,regionId))
#
# skuId = goodsGetSku(spuId,regionId)['data']['list'][0]['skuId']
# print("查找添加商品SkuID：",skuId)
#
# print("编辑SKU发布渠道：",goodsEditSkuChannel(skuId,regionId))
# print("编辑SKU发布环境：",goodsEditSkuEnvironment(skuId,regionId))
# print("编辑SKU通过(预发)审核：",goodsEditSkuExamine(skuId,regionId))
# print("编辑SKU发布上架：",goodsEditSkuGoodsStatus(filmId,skuId,regionId))
#
# print("cms发布上线：",cmsFilmRelease(filmId,regionId))

