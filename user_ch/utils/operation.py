# -*- coding:utf-8 -*-

import requests
import json


class Operation_tickets_Zh():
    '''
    # 国内赠票相关
    '''

    def __init__(self,channel):
        self.channel = channel
        self.userInfo = self.getUserInfo()['data']['list'][0]
        self.headers = {
            'Content-Type': 'application/json',
            'X-User-Id': str(self.userInfo['id']),
        }


    def getGoodsInfo(self):
        '''
        # 获取影片列表
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /outside/getGoodsFilmList
        :return:
        '''

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/outside/getGoodsFilmList'

        params = {
            'groundStatus':'1,2',
            'screenType':'4,6,7,9,10,11'
        }

        result = requests.get(url=host + path, headers=self.headers,params=params)
        resultJ = json.loads(result.content)
        # print(resultJ)
        return resultJ

    def getUserInfo(self):
        '''
        # x-origin-host: http://user-manage-test.smartcinema-inc.com
        # x-origin-path: /user/queryAll
        :return:
        '''

        host = f'http://user-manage-{self.channel}.smartcinema-inc.com'
        path = '/user/queryAll'

        params = {"name": "陈航"}

        result = requests.get(url=host + path, headers={'Content-Type': 'application/json'}, params=params)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getTiccketInfo(self,activityName,filmname,startTime,endTime,skuId,spuId):
        '''
        # x-origin-host: http://ticket-manage-test.smartcinema-inc.com
        # x-origin-path: /activity/entry
        :return:
        '''

        host = f'http://ticket-manage-{self.channel}.smartcinema-inc.com'
        path = '/activity/entry'

        body = json.dumps({
            "activityName": activityName,
            "filmName": filmname,
            "operatorName": self.userInfo['id'],
            "department": "质量保障中心",
            "operatorExplain": "测试活动票码定制生成",
            "activityLabel": "",
            "retailPricing": "0.99",
            "warningSwitch": "2",
            "acceptLimit": 1,
            "newUser": 0,
            "districtLimit": 1,
            "activityType": 0,
            "inventory": "10",
            "price": "25",
            "orgCode": "ORG20200610154900181012",
            "videoType": 1,
            "scheduleType": 4,
            "language": "原声",
            "allowedWatch": 0,
            "activityTime": ["2020-08-31T16:00:00.000Z", "2021-10-31T15:59:59.000Z"],
            "contractCode": "CONTRACT20201102174253861013",
            "display": 0,
            "contractType": 1,
            "allList": [{
                "id": self.userInfo['id'],
                "userId": self.userInfo['id'],
                "userName": self.userInfo['username'],
                "department": self.userInfo['department'],
                "departmentCode": self.userInfo['departmentCode'],
                "userEmail": self.userInfo['email'],
                "userMobile": self.userInfo['mobile'],
                "createTime": "2020-05-21 17:23:22",
                "modifyTime": "2020-05-21 17:23:22"
            }],
            "enterType": 0,
            "roomData": {},
            "deptCode": "aih8",
            "ownerId": self.userInfo['id'],
            "planList": [],
            "startTime": startTime,
            "endTime": endTime,
            "filmType": 1,
            "ticketSkuId": skuId,
            "file": "",
            "spuId": spuId,
            "mailInfo": [],
            "roomName": "",
            "pageTitle": "移动电影院",
            "mainTitle": "移动电影院",
            "subTitle": "欢迎使用移动电影院",
            "activityRule": " 1.每个手机号限领一张电影票。赠票被领取后，所有权将从赠票方转至领票方;\n 2.未注册过'移动电影院'的用户，领票后，应先下载'移动电影院'App，以领票手机号完成注册，即可在App的'放映'区看到该赠票，并可开始观影;\n 3.已注册过'移动电影院'的用户，建议使用注册手机号领票。领取赠票后，可在App的'放映'区看到该赠票，并可开始观影;\n 4.领票成功后，应在'移动电影院'影片上映期内完成观影。影片下线后，将无法再观影;\n 5.'移动电影院'保留法律范围内的最终解释权。如有疑问，请致电官方客服： 4006-2018-05。",
            "linkNum": 1,
            "webchatMainHead": "移动电影院邀您看电影《测试20分钟电影》",
            "webchatSubHead": "获取了国内外各大奖项，拿到手软！！！",
            "icon": "https://g.smartcinema.com.cn/images/0a78cca92af54f7da8fe8f9a92d7a2a4-1268-1268.jpg",
            "starImg": "",
            "subscript": "",
            "sponsorLogo": ""
        })
        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getAuditData(self):
        """
        获取审核列表
        # x-origin-host: http://user-manage-test.smartcinema-inc.com
        # x-origin-path: /common/audit/getAuditList
        :return:
        """

        host = f'http://user-manage-{self.channel}.smartcinema-inc.com'
        path = '/common/audit/getAuditList'

        body = json.dumps({"resKey":"MENU_OMS_AUDIT_LIST","auditGenre":"","auditName":"","currentPage":1,"pageSize":20,"auditListType":0})

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)

        return resultJ


    def updateAuditData(self,aduitId,activityId):
        """
        审核票接口
        # x-origin-host: http://user-manage-test.smartcinema-inc.com
        # x-origin-path: /common/audit/updateAuditData
        :param activityId:
        :return:
        """

        host = f'http://user-manage-{self.channel}.smartcinema-inc.com'
        path = '/common/audit/updateAuditData'

        body = json.dumps({"auditStatus":1,"auditData":[{"id":aduitId,"dateId":activityId,"auditGenre":"5"}]})

        result = requests.post(url=host+path,headers=self.headers,data=body)
        resultJ = json.loads(result.content)
        print(resultJ)

        return resultJ


class Operation_tickets_Inc():
    '''
    # 海外赠票相关
    '''

    def __init__(self,regionId,channel):
        self.regionId = regionId
        self.channel = channel

        self.userInfo = self.getUserInfo()['data']['list'][0]
        self.headers = {
            'Content-Type': 'application/json',
            'X-Region-Id': str(self.regionId),
            'X-User-Id': str(self.userInfo['id']),
        }


    def getGoodsInfo(self):
        '''
        # 获取影片列表
        # x-origin-host: http://aws-goods-manage-test.smartcinema-inc.com
        # x-origin-path: /outside/getGoodsFilmList
        :return:
        '''

        host = f'http://aws-goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/outside/getGoodsFilmList'

        result = requests.get(url=host+path,headers=self.headers)
        resultJ = json.loads(result.content)
        # print(resultJ)
        return resultJ

    def getUserInfo(self):
        '''
        # x-origin-host: http://user-manage-test.smartcinema-inc.com
        # x-origin-path: /user/queryAll
        :return:
        '''

        host = f'http://aws-user-manage-{self.channel}.smartcinema-inc.com'
        path = '/user/queryAll'

        params = {"name": "陈航"}

        result = requests.get(url=host+path, headers={'Content-Type': 'application/json'}, params=params)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ


    def getTiccketInfo(self,activityName,filmname,startTime,endTime,skuId,spuId):
        '''
        # 生成票链接
        # x-origin-host: http://aws-operation-manage-test.smartcinema-inc.com
        # x-origin-path: c
        :return:
        '''

        host = f'http://aws-operation-manage-{self.channel}.smartcinema-inc.com'
        path = '/activity/entry'

        body = json.dumps({
            "international":{
                "en_US":{
                    "pageTitle":"Smart Cinema Intl",
                     "titleType":0,
                     "mainTitle":"移动电影院",
                     "subTitle":"欢迎使用移动电影院",
                     "activityRule":"1. Each mobile number or email is limited to one movie ticket. After the ticket is received, ownership will be transferred from the ticket holder to the receiver;\n 2. Users who have not registered for 'Smart Cinema USA' should download the app first and complete the registration with the mobile number or email of the ticket. You can see the ticket in the 'Screening' section of the app and then start watching;\n 3. Users who have registered for 'Smart Cinema USA' are advised to use the registered mobile number or email to get the ticket. After receiving the free ticket, you can see it in the 'Screening' section of the app and then start watching;\n 4. After receiving the ticket successfully, you can watch the movie during its screening period in the 'Smart Cinema USA' . After the movie goes offline, you will no longer be able to watch it;\n 5. 'Smart Cinema USA' reserves the right of final interpretation within the law.",
                     "webchatMainHead":"A movie ticket in Smart Cinema Intl. is ready for you","webchatSubHead":"Wonderful movies are available for you with the ticket"
                },
                "zh_CN":{
                    "pageTitle":"Smart Cinema Intl",
                    "titleType":0,"mainTitle":"移动电影院",
                    "subTitle":"欢迎使用移动电影院",
                    "activityRule":"1. Each mobile number or email is limited to one movie ticket. After the ticket is received, ownership will be transferred from the ticket holder to the receiver;\n 2. Users who have not registered for 'Smart Cinema USA' should download the app first and complete the registration with the mobile number or email of the ticket. You can see the ticket in the 'Screening' section of the app and then start watching;\n 3. Users who have registered for 'Smart Cinema USA' are advised to use the registered mobile number or email to get the ticket. After receiving the free ticket, you can see it in the 'Screening' section of the app and then start watching;\n 4. After receiving the ticket successfully, you can watch the movie during its screening period in the 'Smart Cinema USA' . After the movie goes offline, you will no longer be able to watch it;\n 5. 'Smart Cinema USA' reserves the right of final interpretation within the law.",
                    "webchatMainHead":"A movie ticket in Smart Cinema Intl.",
                    "webchatSubHead":"Wonderful movies are available"
                }
            },
            "activityName":activityName,
            "filmName":filmname,
            "activityTime":["2019-09-30T16:00:00.000Z","2027-07-31T15:59:59.000Z"],
            "operatorName":self.userInfo['username'],
            "department":self.userInfo['department'],
            "operatorExplain":"活动票码定制生成-测试使用",
            "activityLabel":"",
            "channelName":"渠道名称",
            "retailPricing":"4.99",
            "acceptLimit":1,
            "districtLimit":1,
            "activityType":0,
            "inventory":"10",
            "price":4.99,
            "warningSwitch":2,
            "videoType":1,
            "filmVersion":1,
            "scheduleType":4,
            "display":0,
            "allList":[{
                "id":self.userInfo['id'],
                "userId":self.userInfo['id'],
                "userName":self.userInfo['username'],
                "department":self.userInfo['department'],
                "departmentCode":self.userInfo['departmentCode'],
                "userEmail":self.userInfo['email'],
                "userMobile":self.userInfo['mobile'],
                "createTime":"2019-11-30 14:04:56",
                "modifyTime":"2019-11-30 14:04:56"
            }],
            "enterType":0,
            "roomData":{},
            "deptCode":"aih8",
            "ownerId":self.userInfo['id'],
            "startTime":startTime,
            "endTime":endTime,
            "filmType":1,
            "ticketSkuId":skuId,
            "file":"",
            "spuId":spuId,
            "mailInfo":[],
            "roomName":"",
            "blackMask":0,
            "isFuzzy":0,
            "icon":"",
            "facebookImage":"",
            "starImg":"",
            "subscript":""
        })

        result = requests.post(url=host+path,headers=self.headers,data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getAuditData(self):
        """
        获取审核列表
        x-origin-host: http://aws-user-manage-test.smartcinema-inc.com
        x-origin-path: /common/audit/getAuditList
        :return:
        """

        host = f'http://aws-user-manage-{self.channel}.smartcinema-inc.com'
        path = '/common/audit/getAuditList'

        body = json.dumps({"resKey":"MENU_OMS_AUDIT_LIST","auditGenre":"","auditName":"","currentPage":1,"pageSize":20,"auditListType":0})

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)

        return resultJ

    def updateAuditData(self,aduitId,activityId):
        """
        审核票接口
        x-origin-host: http://aws-user-manage-test.smartcinema-inc.com
        x-origin-path: /common/audit/updateAuditData
        :param activityId:
        :return:
        """

        host = f'http://aws-user-manage-{self.channel}.smartcinema-inc.com'
        path = '/common/audit/updateAuditData'

        body = json.dumps({"auditStatus":1,"auditData":[{"id":aduitId,"dateId":activityId,"auditGenre":"5"}]})

        result = requests.post(url=host+path,headers=self.headers,data=body)
        resultJ = json.loads(result.content)
        # print(resultJ)

        return resultJ

    def getH5Token(self):
        '''
        获取H5页面token
        x-origin-host: https://aws-api-test.smartcinemausa.com
        x-origin-path: /user/passwordLogin
        :return:
        '''

        host = f'https://aws-api-{self.channel}.smartcinemausa.com'
        path = '/user/web/h5/passwordLogin'

        body = json.dumps({
            'uMobile':18403558945,
            'uCode':'4679',
            'uPassword':'3be4673c751088c3cc72c76c56321606',
            'uAreaCode':86,
            'uCid':'1',
            'uLgtype':1
        })

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)

        return resultJ

class Premiere():
    def __init__(self,channel):
        self.channel = channel
        self.userInfo = self.getUserInfo()['data']['list'][0]
        self.headers = {
            'Content-Type': 'application/json',
            'X-User-Id': str(self.userInfo['id'])
        }

    def getUserInfo(self):
        '''
        # 获取用户信息
        # x-origin-host: http://user-manage-test.smartcinema-inc.com
        # x-origin-path: /user/queryAll
        :return:
        '''

        host = f'http://user-manage-{self.channel}.smartcinema-inc.com'
        path = '/user/queryAll'

        params = {"name": "陈航"}

        result = requests.get(url=host+path, headers={'Content-Type': 'application/json'}, params=params)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getSpuLists(self):
        """
        # 获取Spu列表
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /spu/getSpuLists
        :return:
        """
        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/spu/getSpuLists'

        body = json.dumps(
            {"filmName": "", "type": 1}
        )

        result = requests.post(url=host + path, data=body, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ


    def premiere_create(self,filmId,filmName,spuId,startTime,endTime,beignTime,premiereName,beautifyStatus,interactionType,remark):
        """
        # 创建添加首映礼
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/addPremiere
        :param filmId:
        :param filmName:
        :param spuId:
        :param startTime:
        :param endTime:
        :param beignTime:
        :return:
        """
        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/addPremiere'

        data = json.dumps({
            "filmId": filmId,
            "filmName": filmName,
            "spuId": spuId,
            "spuReleaseStartTime": startTime,
            "spuReleaseEndTime": endTime,
            "name": premiereName,
            "subName": filmName+"主题介绍",
            "remark": filmName+str(remark),
            "beignTime": beignTime,
            "beautifyStatus": beautifyStatus,
            "userNum": 1000,
            "interactionType": interactionType,
            "projectionStatus": 1,
            "roomId": 0,
            "backPictureUrl": ""
        })

        result = requests.post(url=host + path, data=data, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def sort_user(self,roomId):
        '''
        # 添加主创人员
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/interactive/sort
        :param roomId:
        :return:
        '''
        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/interactive/sort'

        data = json.dumps(
            {
                "roomId": roomId,
                "interactiveList": "[{\"userId\":12059,\"checked\":1}]"
            }
        )

        result = requests.post(url=host + path, data=data, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)

    def addCompere(self,roomId):
        '''
        # 获取用户信息
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/interactive/addCompere
        :param roomId:
        :return:
        '''

        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/interactive/addCompere'

        body = json.dumps({
            "phone": "18403558945",
            "roomId": roomId
        })

        result = requests.post(url=host+path, data=body,headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def saveImg(self,roomId):
        '''
        # 保存图片配置
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/editBackPicture
        :param roomId:
        :return:
        '''

        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/editBackPicture'

        data = json.dumps({
            "activityImgUrl": "https://g.smartcinema.com.cn/images/50297d17bc9f45cb92acff8a399f5db1-1675-1358.jpg",
            "backPictureUrl": "https://g.smartcinema.com.cn/images/911cfec56a474fd6b0f35d5d991eebb5-1125-900.jpg",
            "roomId": roomId
        })

        result = requests.post(url=host + path, data=data, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)


    def program_info(self,roomId):
        '''
        # 活动节目单
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/studio/editActivityDesc
        :param roomId:
        :return:
        '''

        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/studio/editActivityDesc'

        data = json.dumps({
            "activeStatus": 0,
            "roomId": roomId,
            "activityDescList": [{"time": "2021-04-23 12:24:30", "title": "走上红毯"},
                                 {"time": "2021-04-23 12:34:30", "title": "发布正式开始"},
                                 {"time": "2021-04-23 12:49:30", "title": "测试20分钟电影正式首映"}]
        })

        result = requests.post(url=host + path, data=data, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)


    def activity_shareType(self,roomId):
        '''
        # 活动分享信息
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/studio/editShare
        :param roomId:
        :return:
        '''

        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/studio/editShare'

        data = json.dumps({
            "shareType": 2,
            "shareUrlType": 3,
            "roomId": roomId
        })

        result = requests.post(url=host + path, data=data, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)

    def interaction_methods(self,roomId):
        '''
        # 互动方式信息
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/studio/editHuDongInfo
        :param roomId:
        :return:
        '''
        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/studio/editHuDongInfo'

        data = json.dumps({
            "activityName": "测试使用活动",
            "headBgUrl": "https://g.smartcinema.com.cn/images/23ead67774074d4aa7c648977e78f7f7-1125-264.png",
            "bottomBgUrl": "https://g.smartcinema.com.cn/images/fd0fb7dfe4164d858c43f11a2704f8d7-1125-1539.jpg",
            "warmLiveUrl": "http://183.207.249.14/PLTV/3/224/3221225550/index.m3u8",
            "celebrateLiveUrl": "http://183.207.249.14/PLTV/3/224/3221225550/index.m3u8",
            "shareStatus": 1,
            "liveShareUrl": "https://www.baidu.com",
            "interactionShareUrl": "https://g.smartcinema.com.cn/images/6a1c1cab86bc4e57baf009401a90f17e-200-112.png",
            "liveShareTitle": "测试主标题",
            "liveShareContent": "测试副标题",
            "type": 3,
            "roomId": roomId
        })

        result = requests.post(url=host + path, data=data, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)

    def getPositiveInfo(self,skuId):
        '''
        # 获取正片信息
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /goods/getGoodsDetails
        :param skuId:
        :return:
        '''

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/goods/getGoodsDetails'

        body = json.dumps(
            {"skuId": skuId}
        )

        result = requests.post(url=host + path, data=body, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def updataPremiere(self,filmId,spuName,spuId,skuId,productId,positiveTitleValue,startTime,endTime):
        '''
        # 更新首映礼价格
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /goods/goodsUpdate
        :param filmId:
        :param spuName:
        :param spuId:
        :param skuId:
        :param productId:
        :param positiveTitleValue:
        :param startTime:
        :param endTime:
        :return:
        '''

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/goods/goodsUpdate'

        body = json.dumps(
            {
                "fileLanguage": 1,
                "videoClarity": 1,
                "isClarity": 1,
                "videoCaption": 1,
                "videoType": 1,
                "videoSpec": 1,
                "isCdpf": 0,
                "clarityDesc": "2K（购票后即可观影）",
                "veriosnDesc": "院线上映原声版",
                "spuId": spuId,
                "filmId": filmId,
                "spuName": spuName,
                "spuCoverImage": "https://g.smartcinema.com.cn/images/4549dbcae4cc442a995a4efe90c53ece-1057-1511.jpg",
                "skuId": skuId,
                "sortNum": 0,
                "spuTag": "[\"院线同步\"]",
                "spuDescribe": "无",
                "productId": productId,
                "positiveTitleValue": positiveTitleValue,
                "sellerName": "北京云途时代影业科技有限公司",
                "screenType": "首映礼",
                "screenDesc": "首映礼",
                "stockNum": 1000,
                "standardPrice": 25,
                "releasePrice": 0,
                "basePrice": 25,
                "iosPrice": 25,
                "isActivity": 1,
                "servicePrice": 0,
                "iosServicePrice": 0,
                "activityPrice": "0.00",
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

        result = requests.post(url=host + path, data=body, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)

    def getPremiereList(self):
        '''
        # 获取首映礼列表
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/list
        :return:
        '''

        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/list'

        body = json.dumps(
            {
                "page": 1,
                "filmId": "",
                "filmName": "",
                "type": 0,
                "onlineStatus": 0,
                "size": str(20)
            }
        )

        result = requests.post(url=host + path, data=body, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def releasePremiere(self,roomId):
        '''
        # 上线首映礼
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/updateStatus
        :param roomId:
        :return:
        '''
        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/updateStatus'

        body = json.dumps(
            {"roomId":roomId,"onlineStatus":1}
        )

        result = requests.post(url=host + path, data=body, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

class Create_film():
    """
    # 国内影片创建
    """

    def __init__(self,filmName,channel):
        """
        # 初始化数据
        :param filmName:
        :param channel:
        """
        self.filmName = filmName
        self.channel = channel
        self.userInfo = self.getUserInfo()['data']['list'][0]
        self.headers = {
            'Content-Type': 'application/json',
            'X-User-Id': str(self.userInfo['id']),
        }

    def create_film_baseInfo(self):
        """
        # 创建影片基本信息
        # x-origin-host: http://media-manage-test.smartcinema-inc.com
        # x-origin-path: /filmInfo/addInfo
        :return:
        """

        host = f"http://media-manage-{self.channel}.smartcinema-inc.com"
        path = "/filmInfo/addInfo"

        body = json.dumps(
            {
                "filmDefaultName": 1,
                "madeCounties": "239",
                "filmSubtitle": "1",
                "filmLanguage": "1",
                "filmNation": "1",
                "filmCategories": "1,3",
                "movieCode": "TestFilm",
                "filmName": self.filmName,
                "filmNameEn": "testAutoAdd",
                "filmLength": "120",
                "filmCreator": "测试主创",
                "filmRecommend": "我是推荐语",
                "filmRecommendRate": 5,
                "filmBackgroundImage": "https://g.smartcinema.com.cn/images/2f268c38396743f0b0a2126e6df3a279-691-294.png",
                "filmVrBackgroundImage": "https://g.smartcinema.com.cn/images/2366483d3f7948699b82fc867162681c-1125-1607.jpg",
                "licenseCode": "Testfilm",
                "filmIntro": self.filmName+"测试简介"
            }
        )

        result = requests.post(url=host+path,data=body,headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getUserInfo(self):
        '''
        # 获取用户信息
        # x-origin-host: http://user-manage-test.smartcinema-inc.com
        # x-origin-path: /user/queryAll
        :return:
        '''

        host = f'http://user-manage-{self.channel}.smartcinema-inc.com'
        path = '/user/queryAll'

        params = {"name": "陈航"}

        result = requests.get(url=host+path, headers={'Content-Type': 'application/json'}, params=params)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getfilmList(self):
        """
        # 获取媒资影片列表
        x-origin-host: http://media-manage-test.smartcinema-inc.com
        x-origin-path: /filmInfo/getList
        :return:
        """

        host = f'http://media-manage-{self.channel}.smartcinema-inc.com'
        path = '/filmInfo/getList'

        params = {
            "filmId":"",
            "word":"",
            "limit": 20,
            "orderBy": 1,
            "sorted": 0,
            "page": 1
        }

        result = requests.get(url=host + path, headers=self.headers, params=params)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def saveFilmCast(self,filmId):
        """
        # 添加影人信息
        # x-origin-host: http://media-manage-test.smartcinema-inc.com
        # x-origin-path: /filmInfo/saveFilmCast
        :param filmId:
        :return:
        """
        host = f'http://media-manage-{self.channel}.smartcinema-inc.com'
        path = '/filmInfo/saveFilmCast'

        body = json.dumps(
            {
                "filmId": filmId,
                "actors": [{
                    "castId": 4688350014204488,
                    "castName": "测试cms的图片同步",
                    "headImage": "http://smart-test1-php-1255596649.file.myqcloud.com/images/cms/6a5f3d159dbe6955c5bfb80b1e6e1398.jpg",
                    "phone": "",
                    "roleId": 2,
                    "roleName": "",
                    "id": 1
                }]
            }
        )

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def saveAddImgInfo(self,filmId):
        """
        # 保存影片图片信息
        # x-origin-host: http://media-manage-test.smartcinema-inc.com
        # x-origin-path: /filmImage/addInfo
        :param filmId:
        :return:
        """

        host = f'http://media-manage-{self.channel}.smartcinema-inc.com'
        path = '/filmImage/addInfo'

        img = []
        img1 = json.dumps(
            {
                "imageType": 1,
                "subType": 3,
                "imageUrl": "https://g.smartcinema.com.cn/images/4549dbcae4cc442a995a4efe90c53ece-1057-1511.jpg",
                "filmId": filmId
            }
        )
        img2 = json.dumps(
            {
                "imageType": 5,
                "imageUrl": "https://g.smartcinema.com.cn/images/d580fed56a0840069b29c1c88b7acf51-650-365.jpg",
                "filmId": filmId
            }
        )
        img3 = json.dumps(
            {
                "imageType": 1,
                "subType": 2,
                "imageUrl": "https://g.smartcinema.com.cn/images/65fd733412134b65be0f0a661359cc42-1482-1000.jpg",
                "filmId": filmId
            }
        )
        img4 = json.dumps(
            {
                "imageType": 4,
                "imageUrl": "https://g.smartcinema.com.cn/images/45432df9aaea482e8ba1e71e575d079a-1057-1511.jpg",
                "filmId": filmId
            }
        )
        img5 = json.dumps(
            {
                "imageType": 2,
                "imageSort": 1,
                "subType": 0,
                "imageUrl": "https://g.smartcinema.com.cn/images/6318dee7f66b4a858e645e93a11d4256-1125-1672.jpg",
                "filmId": filmId
            }
        )
        img6 = json.dumps(
            {
                "imageType": 2,
                "imageSort": 2,
                "subType": 0,
                "imageUrl": "https://g.smartcinema.com.cn/images/476b7677b6de48edb2e0ed31561f27ec-1125-1906.jpg",
                "filmId": filmId
            }
        )
        img7 = json.dumps(
            {
                "imageType": 2,
                "imageSort": 3,
                "subType": 0,
                "imageUrl": "https://g.smartcinema.com.cn/images/780bc5f8956e4eb6b700aafc82f292cb-433-433.jpg",
                "filmId": filmId
            }
        )
        img8 = json.dumps(
            {
                "imageType": 2,
                "imageSort": 4,
                "subType": 0,
                "imageUrl": "https://g.smartcinema.com.cn/images/87eb71b537bb4d1986d3e3b9e55c3278-466-466.jpg",
                "filmId": filmId
            }
        )
        img9 = json.dumps(
            {
                "imageType": 2,
                "imageSort": 5,
                "subType": 0,
                "imageUrl": "https://g.smartcinema.com.cn/images/f318b3666c1c44e7ab30f2f445d54500-1024-557.jpg",
                "filmId": filmId
            }
        )
        img10 = json.dumps(
            {
                "imageType": 2,
                "imageSort": 0,
                "subType": 0,
                "imageUrl": "https://g.smartcinema.com.cn/images/2a2549e510094e1eb83f003258539443-700-393.jpg",
                "filmId": filmId
            }
        )
        img.append(img1)
        img.append(img2)
        img.append(img3)
        img.append(img4)
        img.append(img5)
        img.append(img6)
        img.append(img7)
        img.append(img8)
        img.append(img9)
        img.append(img10)

        for i in img:
            result = requests.post(url=host + path, headers=self.headers, data=i)
            resultJ = json.loads(result.content)
            print(resultJ)
        return resultJ

    def saveAddVideoInfo(self,filmId):
        """
        # 保存影片 预告片信息
        # x-origin-host: http://media-manage-test.smartcinema-inc.com
        # x-origin-path: /filmVideo/addInfo
        :param filmId:
        :return:
        """

        host = f'http://media-manage-{self.channel}.smartcinema-inc.com'
        path = '/filmVideo/addInfo'

        video = []
        video1 = json.dumps(
            {
                "videoType": ["1"],
                "videoLength": 20,
                "videoUrl": "http://smart-java-test.smartcinema.com.cn/trailer/1630920227251_PMkXB.MP4",
                "videoImageUrl": "",
                "isDisplay": 1,
                "displayChange": True,
                "editChange": True,
                "videoName": "预告片",
                "videoIntro": "预告片1",
                "videoImgUrl": "https://g.smartcinema.com.cn/images/501e6a2ad7224c51a18af619c1544ade-800-450.jpg",
                "filmId": filmId
            }
        )
        video2 = json.dumps(
            {
                "videoType": ["3"],
                "videoLength": 15,
                "videoUrl": "http://smart-java-test.smartcinema.com.cn/trailer/1630920297873_dXwyC.mp4",
                "videoImageUrl": "",
                "isDisplay": 1,
                "displayChange": True,
                "editChange": True,
                "videoName": "花絮",
                "videoIntro": "花絮1",
                "videoImgUrl": "https://g.smartcinema.com.cn/images/300704ad7f8c4bdda0ace9d2eb7b48ae-1280-720.jpg",
                "filmId": filmId
            }
        )
        video.append(video1)
        video.append(video2)

        for i in video:
            result = requests.post(url=host + path, headers=self.headers, data=i)
            resultJ = json.loads(result.content)
            print(resultJ)
        return resultJ

    def addSpu(self,filmId,filmName,startTime,endTime):
        """
        # 添加商品Spu
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /spu/addProduct
        :param filmId:
        :param filmName:
        :param startTime:
        :param endTime:
        :return:
        """

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/spu/addProduct'

        body = json.dumps(
            {
                "filmId": filmId,
                "filmName": filmName,
                "filmImage": "https://g.smartcinema.com.cn/images/4549dbcae4cc442a995a4efe90c53ece-1057-1511.jpg",
                "spuBasePrice": "0.00",
                "spuTag": "[\"院线同步\"]",
                "spuReleaseStartTime": startTime,
                "spuReleaseEndTime": endTime,
                "spuDescribe": "无",
                "spuType": 1
            }
        )

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getSpuList(self):
        '''
        # 获取SPU列表
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /spu/getSpuAreaList
        :return:
        '''

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/spu/getSpuAreaList'

        body = json.dumps(
            {"page": 1, "keyWords": "", "limit": 20}
        )

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getfilmDate(self,filmId):
        """
        # 获取正片信息
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /mediaApi/getFilmData
        :param filmId:
        :return:
        """

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/mediaApi/getFilmData'

        body = json.dumps(
            {"movieId": filmId}
        )

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getSyncFilmList(self):
        '''
        # 获取同步的影片列表
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /mediaApi/getFilmList
        :return:
        '''

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/mediaApi/getFilmList'

        result = requests.get(url=host + path, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ


    def addGoodsSku(self,filmId,spuId,spuName,positiveTitleValue,startTime,endTime):
        """
        # 增加 sku
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /goods/addGoods
        :param filmId:
        :param spuId:
        :param spuName:
        :param positiveTitleValue:
        :param startTime:
        :param endTime:
        :return:
        """

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/goods/addGoods'

        body = json.dumps(
            {
                "fileLanguage": 1,
                "videoClarity": 1,
                "isClarity": 1,
                "videoCaption": 1,
                "videoType": 1,
                "videoSpec": 1,
                "isCdpf": 0,
                "clarityDesc": "2K（购票后即可观影）",
                "veriosnDesc": "院线上映原声版",
                "spuId": spuId,
                "filmId": filmId,
                "spuName": spuName,
                "spuCoverImage": "https://g.smartcinema.com.cn/images/4549dbcae4cc442a995a4efe90c53ece-1057-1511.jpg",
                "sortNum": 0,
                "spuTag": "[\"院线同步\"]",
                "spuDescribe": "无",
                "positiveTitleValue": positiveTitleValue,
                "sellerName": "北京云途时代影业科技有限公司",
                "screenType": "公映场",
                "screenDesc": "公映场",
                "standardPrice": 0,
                "releasePrice": 0,
                "basePrice": 0,
                "iosPrice": 0,
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

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getSkuList(self,spuId):
        """
        # 获取sku列表
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /goods/getGoodsList
        :return:
        """

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/goods/getGoodsList'

        body = json.dumps(
            {
                "spuId": spuId,
                "groundStatus": "",
                "environment": "",
                "page": 1,
                "limit": 20
            }
        )

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ


    def bindupdateGroup(self,skuId):
        """
        # 绑定sku渠道
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /sku/updateGroup
        :param skuId:
        :return:
        """

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/sku/updateGroup'

        body = json.dumps(
            {
                "skuId": skuId,
                "groupNum": "40,41,42,43"
            }
        )

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def updateEnvironment(self,skuId):
        """
        # 更新配置环境
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /sku/updateEnvironment
        :param skuId:
        :return:
        """


        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/sku/updateEnvironment'

        body = json.dumps(
            {
                "skuId": skuId,
                "environment": "1,2"
            }
        )

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def updateGoodsStatus(self,skuId,filmId):
        """
        # 更改sku上架设置
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /sell/updateGoodsStatus
        :param skuId:
        :param filmId:
        :return:
        """

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/sell/updateGoodsStatus'

        body = json.dumps(
            {
                "skuId": skuId,
                "filmId": filmId,
                "groundStatus": 1
            }
        )

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def cmsReleaseFilm(self,filmId):
        """
        # CMS同步影片 发布线上
        # x-origin-host: http://cms-manage-test.smartcinema-inc.com
        # x-origin-path: /cmsFilm/releaseFilm
        :param filmId:
        :return:
        """

        host = f'http://cms-manage-{self.channel}.smartcinema-inc.com'
        path = '/cmsFilm/releaseFilm'

        body = json.dumps(
            {"filmId":filmId}
        )

        result = requests.post(url=host + path, headers=self.headers, data=body)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

class Special():
    def __init__(self,channel):
        self.channel = channel
        self.userInfo = self.getUserInfo()['data']['list'][0]
        self.headers = {
            'Content-Type': 'application/json',
            'X-User-Id': str(self.userInfo['id'])
        }

    def getUserInfo(self):
        '''
        # 获取用户信息
        # x-origin-host: http://user-manage-test.smartcinema-inc.com
        # x-origin-path: /user/queryAll
        :return:
        '''

        host = f'http://user-manage-{self.channel}.smartcinema-inc.com'
        path = '/user/queryAll'

        params = {"name": "陈航"}

        result = requests.get(url=host+path, headers={'Content-Type': 'application/json'}, params=params)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getGuestUser(self):
        '''
        # 获取咖列表
        # x-origin-host: http://ucenter-manage-test.smartcinema-inc.com
        # x-origin-path: /ucenter/getGuestData
        :return:
        '''

        host = f'http://ucenter-manage-{self.channel}.smartcinema-inc.com'
        path = '/ucenter/getGuestData'

        result = requests.get(url=host + path, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getSpuLists(self):
        """
        # 获取Spu列表
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /spu/getSpuLists
        :return:
        """
        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/spu/getSpuLists'

        body = json.dumps(
            {"filmName": "", "type": 1}
        )

        result = requests.post(url=host + path, data=body, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def special_create(self,filmId,filmName,spuId,specialName,remark,userId,nickname,userPhoto,beignTime,beautifyStatus,interactionType,startTime,endTime):
        '''
        # 创建专场
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/editRoom
        :param spuId:
        :param specialName:
        :param remark:
        :param userId:
        :param beignTime:
        :param beautifyStatus:
        :param interactionType:
        :param filmId:
        :param filmName:
        :param startTime:
        :param endTime:
        :param nickname:
        :param userPhoto:
        :return:
        '''
        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/editRoom'

        body = json.dumps(
            {
                "spuId": spuId,
                "name": specialName,
                "remark": remark,
                "userId": userId,
                "beignTime": beignTime,
                "beautifyStatus": beautifyStatus,
                "userNum": 100,
                "interactionType": interactionType,
                "projectionStatus": 1,
                "filmId": filmId,
                "filmName": filmName,
                "spuReleaseStartTime": startTime,
                "spuReleaseEndTime": endTime,
                "nickname": nickname,
                "photo": userPhoto,
                "role": 2,
                "type": 1,
                "roomId": 0
            }
        )

        result = requests.post(url=host + path, data=body, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def saveImg(self, roomId):
        '''
        # 保存图片配置
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/editBackPicture
        :param roomId:
        :return:
        '''

        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/editBackPicture'

        data = json.dumps({
            "activityImgUrl": "https://g.smartcinema.com.cn/images/50297d17bc9f45cb92acff8a399f5db1-1675-1358.jpg",
            "backPictureUrl": "https://g.smartcinema.com.cn/images/911cfec56a474fd6b0f35d5d991eebb5-1125-900.jpg",
            "roomId": roomId
        })

        result = requests.post(url=host + path, data=data, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)

    def program_info(self,roomId):
        '''
        # 活动节目单
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/studio/editActivityDesc
        :param roomId:
        :return:
        '''

        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/studio/editActivityDesc'

        data = json.dumps(
            {
                "activeStatus": 0,
                "roomId": roomId,
                "activityDescList": [{
                    "time": "2021-09-13 10:57:23",
                    "title": ""
                }, {
                    "time": "2021-09-13 11:07:23",
                    "title": ""
                }]
            }
        )

        result = requests.post(url=host + path, data=data, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)

    def interaction_methods(self,roomId):
        '''
        # 互动方式信息
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/studio/editHuDongInfo
        :param roomId:
        :return:
        '''
        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/studio/editHuDongInfo'

        data = json.dumps(
            {
                "warmLiveUrl": "http://183.207.249.14/PLTV/3/224/3221225550/index.m3u8",
                "celebrateLiveUrl": "http://183.207.249.14/PLTV/3/224/3221225550/index.m3u8",
                "type": 1,
                "roomId": roomId
            }
        )

        result = requests.post(url=host + path, data=data, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)

    def getPositiveInfo(self,skuId):
        '''
        # 获取正片信息
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /goods/getGoodsDetails
        :param skuId:
        :return:
        '''

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/goods/getGoodsDetails'

        body = json.dumps(
            {"skuId": skuId}
        )

        result = requests.post(url=host + path, data=body, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def updateSpecial(self,spuId,filmId,spuName,productId,skuId,positiveTitleValue,startTime,endTime):
        '''
        # 更新专场信息
        # x-origin-host: http://goods-manage-test.smartcinema-inc.com
        # x-origin-path: /goods/goodsUpdate
        :param spuId:
        :param filmId:
        :param spuName:
        :param productId:
        :param skuId:
        :param positiveTitleValue:
        :param startTime:
        :param endTime:
        :return:
        '''

        host = f'http://goods-manage-{self.channel}.smartcinema-inc.com'
        path = '/goods/goodsUpdate'

        body = json.dumps(
            {
                "fileLanguage": 1,
                "videoClarity": 1,
                "isClarity": 1,
                "videoCaption": 1,
                "videoType": 1,
                "videoSpec": 1,
                "isCdpf": 0,
                "clarityDesc": "2K（购票后即可观影）",
                "veriosnDesc": "院线上映原声版",
                "spuId": spuId,
                "filmId": filmId,
                "spuName": spuName,
                "spuCoverImage": "https://g.smartcinema.com.cn/images/4549dbcae4cc442a995a4efe90c53ece-1057-1511.jpg",
                "productId": productId,
                "skuId": skuId,
                "sortNum": 0,
                "spuTag": "[\"院线同步\"]",
                "spuDescribe": "无",
                "positiveTitleValue": positiveTitleValue,
                "sellerName": "北京云途时代影业科技有限公司",
                "screenType": "专场",
                "screenDesc": "嗯吧专场 09月13日 10:43",
                "stockNum": 100,
                "standardPrice": 25,
                "releasePrice": 0,
                "basePrice": 25,
                "iosPrice": 25,
                "isActivity": 1,
                "servicePrice": 10,
                "iosServicePrice": 10,
                "activityPrice": "0.00",
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

        result = requests.post(url=host + path, data=body, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def getSpecialList(self):
        '''
        获取专场审核列表
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/getAuditList
        :return:
        '''

        host = 'http://activity-manage-test.smartcinema-inc.com'
        path = '/inner/activity/getAuditList'

        params = {
                "page": 1,
                "filmId": "",
                "filmName": "",
                "type": 1,
                "onlineStatus": 0,
                "size": str(20)
            }

        result = requests.get(url=host + path, headers=self.headers, params=params)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

    def releaseSpecial(self,roomId):
        '''
        # 上线首映礼
        # x-origin-host: http://activity-manage-test.smartcinema-inc.com
        # x-origin-path: /inner/activity/updateStatus
        :param roomId:
        :return:
        '''
        host = f'http://activity-manage-{self.channel}.smartcinema-inc.com'
        path = '/inner/activity/updateStatus'

        body = json.dumps(
            {"roomId":roomId,"onlineStatus":1}
        )

        result = requests.post(url=host + path, data=body, headers=self.headers)
        resultJ = json.loads(result.content)
        print(resultJ)
        return resultJ

'''创建专场'''
# create_special = Special('test')
# create_special.getGuestUser()
# film_info = create_special.getSpuLists()['data'][112]
# specialName = 'ouuoiu'
# remark = '就是个描述'
# userId = 179
# nickname = '嗯吧'
# userPhoto = ''
# beignTime = 1631501024612
# beautifyStatus = 1
# interactionType = 1
# special_info = create_special.special_create(film_info['filmId'],film_info['filmName'],film_info['spuId'],specialName,remark,userId,nickname,userPhoto,beignTime,beautifyStatus,interactionType,film_info['spuReleaseStartTime'],film_info['spuReleaseEndTime'])
# create_special.saveImg(special_info['data']['id'])
# create_special.program_info(special_info['data']['id'])
# create_special.interaction_methods(special_info['data']['id'])



# create_special.getSpecialList()
# create_special.releasePremiere(213167)

'''创建首映礼'''
# create_premiere = Premiere('test')
# test_film = create_premiere.getSpuLists()['data']
# print(test_film)
# premiere_info = create_premiere.premiere_create(test_film['filmId'],test_film['filmName'],test_film['spuId'],test_film['spuReleaseStartTime'],test_film['spuReleaseEndTime'],1631314800000)
# create_premiere.sort_user(premiere_info['data']['id'])
# create_premiere.addCompere(premiere_info['data']['id'])
# create_premiere.saveImg(premiere_info['data']['id'])
# create_premiere.program_info(premiere_info['data']['id'])
# create_premiere.activity_shareType(premiere_info['data']['id'])
# create_premiere.interaction_methods(premiere_info['data']['id'])
# create_premiere.getPremiereList()

''' 国内创建影片测试 '''
create_film = Create_film('我是快乐的小猫咪','test')
# create_film.create_film_baseInfo()
# create_film.saveAddVideoInfo()
# create_film.updateGoodsStatus(7405,4994894073919712)
filmId = 5012878937526380
filmName = '国内优化带水印'
startTime = 1630425600
endTime = 1632931200
positiveTitleValue = 5088984844196085
spuId = "8KmxU1rqqdEMvhF"
spuName = '陈情没有令牌'

# create_film.getSyncFilmList()
# create_film.addSpu(filmId,filmName,startTime,endTime)
# create_film.addGoodsSku(filmId,spuId,spuName,positiveTitleValue,startTime,endTime)
# create_film.updateGoodsStatus(7413,4951032860941138)

'''海外创建影片测试'''


''' 国内赠票调试 '''

# operation_treate = Operation_tickets_Zh('prod')
# operation_treate.getUserInfo()

# # operation_treate.getTiccketInfo('2','2',12432434,2342344,'33','sdcxj342sdcd')
# # operation_treate.updateAuditData(4237,691)
#
# q = operation_treate.getGoodsInfo()['data']
# print(q)
# j={}
# for k in q:
#     if k['skuId'] == 2005:
#         print(k)
#         j = k
#         break
# l = operation_treate.getTiccketInfo('测试使用',j['filmName'],j['onlineStartTime'],j['onlineEndTime'],j['skuId'],j['spuId'])
#
# print(l)

''' 海外赠票调试 '''

# operation_treate = Operation_tickets_Inc(1,'test')
# operation_treate.getUserInfo()

# q = operation_treate.getGoodsInfo()['data']
# print(q)
# j={}
# for k in q:
#     if k['skuId'] == 1442:
#         print(k)
#         j = k
#         break
# l = operation_treate.getTiccketInfo('测试使用',j['filmName'],j['onlineStartTime'],j['onlineEndTime'],j['skuId'],j['spuId'])
#
# print(l)

