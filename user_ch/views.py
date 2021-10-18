from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from . import models
from .utils.operation import Operation_tickets_Inc,Operation_tickets_Zh
from .utils.operation import Create_film
from .utils.operation import Premiere,Special
from .utils.testTools import getCodeInfo



def test_menus(request):
    '''
    # 权限菜单
    :param request:
    :return:
    '''
    content = {
            "data": [{
                "id": 100,
                "authName": "用户管理",
                "path": "users",
                "children": [{
                    "id": 110,
                    "authName": "用户列表",
                    "path": "users",
                    "children": [],
                    "order": None
                }],
                "order": 1
            }, {
                "id": 200,
                "authName": "接口自动化",
                "path": "users",
                "children": [{
                    "id": 210,
                    "authName": "项目列表",
                    "path": "projectlist",
                    "children": [],
                    "order": None
                },{
                    "id": 220,
                    "authName": "模块列表",
                    "path": "modulelist",
                    "children": [],
                    "order": None
                },{
                    "id": 230,
                    "authName": "用例列表",
                    "path": "testlist",
                    "children": [],
                    "order": None
                },{
                    "id": 240,
                    "authName": "配置列表",
                    "path": "configlist",
                    "children": [],
                    "order": None
                },{
                    "id": 250,
                    "authName": "测试套件",
                    "path": "suitelist",
                    "children": [],
                    "order": None
                },{
                    "id": 260,
                    "authName": "测试报告",
                    "path": "reportlist",
                    "children": [],
                    "order": None
                },{
                    "id": 270,
                    "authName": "定时任务",
                    "path": "periodictask",
                    "children": [],
                    "order": None
                }],
                "order": 1
            },{
                "id": 300,
                "authName": "权限管理",
                "path": "rights",
                "children": [{
                    "id": 310,
                    "authName": "角色列表",
                    "path": "roles",
                    "children": [],
                    "order": None
                }, {
                    "id": 320,
                    "authName": "权限列表",
                    "path": "rights",
                    "children": [],
                    "order": None
                }],
                "order": 2
            }, {
                "id": 400,
                "authName": "测试管理",
                "path": "goods",
                "children": [
                    {
                        "id": 410,
                        "authName": "添加影片",
                        "path": "createfilm",
                        "children": [],
                        "order": 1
                    }, {
                        "id": 420,
                        "authName": "添加首映礼",
                        "path": "premiere",
                        "children": [],
                        "order": 1
                    }, {
                        "id": 430,
                        "authName": "添加专场",
                        "path": "special",
                        "children": [],
                        "order": 2
                    }, {
                        "id": 440,
                        "authName": "辅助工具🔧",
                        "path": "tools",
                        "children": [],
                        "order": 3
                    },{
                        "id": 450,
                        "authName": "运营活动创建",
                        "path": "operation",
                        "children": [],
                        "order": 4
                    },
                ],
                "order": 3
            }, {
                "id": 500,
                "authName": "订单管理",
                "path": "orders",
                "children": [{
                    "id": 510,
                    "authName": "订单列表",
                    "path": "orders",
                    "children": [],
                    "order": None
                }],
                "order": 4
            }, {
                "id": 600,
                "authName": "数据统计",
                "path": "reports",
                "children": [{
                    "id": 610,
                    "authName": "数据报表",
                    "path": "reports",
                    "children": [],
                    "order": None
                }],
                "order": 5
            }],
            "meta": {
                "msg": "获取菜单列表成功",
                "status": 200
            }
        }

    return HttpResponse(json.dumps(content),content_type='application/json')

def test_page(request):
    '''
    # 测试环境用户信息
    :param request:
    :return:
    '''
    pagenum = request.GET.get('pagenum')
    perPage = request.GET.get('pagesize')
    query = request.GET.get('query')

    if(pagenum == None):pagenum = 1
    if(perPage == None):perPage = 10

    if query == '' or query is None:
        setUserInfo = models.ClientUser.objects.all()
    else:
        setUserInfo = models.ClientUser.objects.filter(u_nickname__contains=query)

    pagtor = Paginator(setUserInfo,per_page=perPage)

    pagesize = pagtor.num_pages

    total = pagtor.count

    pagedata = pagtor.page(pagenum).object_list

    # print("页面总数",pagesize)
    # print("当前页数据",(pagedata))
    # print("页面总数据",total)

    userInfoList = []
    userInfo = {}
    for i in pagedata:

        # 把获取的数据添加到 用户信息dict中
        userInfo['id'] = i.id
        userInfo['u_mobile'] = i.u_mobile
        userInfo['u_nickname'] = i.u_nickname
        userInfo['u_image'] = i.u_image
        userInfo['u_update_time'] = i.u_update_time
        userInfo['u_status'] = i.u_status

        # 使用list集合整页数据
        userInfoList.append(userInfo)
        userInfo = {}

    result = {'code':200,'data':{'pagesize':pagesize,'total':total,'userList':userInfoList},'msg':'success'}

    # print(userInfo)
    # print(userInfoList)
    # return HttpResponse(json.dumps({'test':'123'}),content_type='application/json')
    return HttpResponse(json.dumps(result),content_type='application/json')



def test_report(request):

    return render(request,'report_template.html')

# 创建赠票-国内
def operation_ticket_create_zh(request):

    if request.method == 'GET':
        channel = request.GET.get('channel')
        operation_tickets = Operation_tickets_Zh(channel=channel)
        movieList = operation_tickets.getGoodsInfo()
        schedule_list = {"code": 0, "msg": "success", "data": []}
        for movieList_schedule in movieList['data']:
            if movieList_schedule['schedule'] == '特邀场':
                schedule_list['data'].append(movieList_schedule)

        return HttpResponse(json.dumps(schedule_list), content_type='application/json')

    if request.method == 'POST':

        # 获取json请求数据
        json_str = request.body
        json_data = json.loads(json_str)
        filmName = json_data['filmName']
        startTime = json_data['onlineStartTime']
        endTime = json_data['onlineEndTime']
        skuId = json_data['skuId']
        spuId = json_data['spuId']
        activityName = json_data['activityName']
        channel = json_data['channel']
        print(json_data)
        print(endTime)

        operation_tickets = Operation_tickets_Zh(channel=channel)
        # 生成票码
        createTicket = operation_tickets.getTiccketInfo(activityName,filmName,startTime,endTime,skuId,spuId)
        # 审核票
        getAuditInfo = operation_tickets.getAuditData()['data']['pageData']
        auditUserInfo = operation_tickets.userInfo
        for audiInfo in getAuditInfo:
            if audiInfo['ownerId'] == auditUserInfo['id']:
                operation_tickets.updateAuditData(audiInfo['id'],audiInfo['dateId'])

        return HttpResponse(json.dumps(createTicket),content_type='application/json')

# 创建赠票-海外
def operation_ticket_create_inc(request):

    if request.method == 'GET':
        regionId = request.GET.get('regionId')
        channel = request.GET.get('channel')
        operation_tickets = Operation_tickets_Inc(regionId,channel=channel)
        movieList = operation_tickets.getGoodsInfo()
        schedule_list = {"code": 0,"msg": "success","data": []}
        for movieList_schedule in movieList['data']:
            if movieList_schedule['schedule'] == '特邀场':
                schedule_list['data'].append(movieList_schedule)

        return HttpResponse(json.dumps(schedule_list),content_type='application/json')


    if request.method == 'POST':
        regionId = '1'
        print(request)

        # 获取json请求数据
        json_str = request.body
        json_data = json.loads(json_str)
        filmName = json_data['filmName']
        startTime = json_data['onlineStartTime']
        endTime = json_data['onlineEndTime']
        skuId = json_data['skuId']
        spuId = json_data['spuId']
        activityName = json_data['activityName']
        channel = json_data['channel']

        operation_tickets = Operation_tickets_Inc(regionId,channel=channel)
        # 生成票码
        createTicket = operation_tickets.getTiccketInfo(activityName,filmName,startTime,endTime,skuId,spuId)
        # 审核票
        getAuditInfo = operation_tickets.getAuditData()['data']['pageData']
        auditUserInfo = operation_tickets.userInfo
        for audiInfo in getAuditInfo:
            if audiInfo['ownerId'] == auditUserInfo['id']:
                operation_tickets.updateAuditData(audiInfo['id'],audiInfo['dateId'])

        return HttpResponse(json.dumps(createTicket),content_type='application/json')

# 获取验证码-国内
def getCode(request):

    if request.method == 'GET':

        channel = request.GET.get('channel')
        regionId = request.GET.get("regionId")
        mobile = request.GET.get("mobile")
        platformtype = request.GET.get('platFormType')

        codemsg = {'mobile':mobile,'code':None,'msg':'查无验证码，请再次确认发送信息'}
        content = {"code": 0, "msg": "success", "data": [codemsg]}

        if platformtype == 'client':
            if regionId == '0':
                if channel == 'test':
                    codeInfo = getCodeInfo(platformtype,regionId,channel,mobile)
                    if codeInfo.get('data'):
                        codemsg['code'] = codeInfo.get('data')['code']
                        codemsg['msg'] = codeInfo['msg']
                        return HttpResponse(json.dumps(content),content_type='application/json')
                    else: return HttpResponse(json.dumps(content),content_type='application/json')
                elif channel == 'prod':
                    codeInfo = getCodeInfo(platformtype, regionId, channel, mobile)
                    if codeInfo.get('data'):
                        codemsg['code'] = codeInfo.get('data')['code']
                        codemsg['msg'] = codeInfo['msg']
                        return HttpResponse(json.dumps(content), content_type='application/json')
                    else:
                        return HttpResponse(json.dumps(content), content_type='application/json')
                else: return HttpResponse(json.dumps(content), content_type='application/json')
            elif regionId == '1':
                return HttpResponse(json.dumps(content), content_type='application/json')
            else: return HttpResponse(json.dumps(content), content_type='application/json')
        elif platformtype == 'h5':
            if regionId == '0':
                if channel == 'test':
                    codeInfo = getCodeInfo(platformtype, regionId, channel, mobile)
                    if codeInfo.get('data'):
                        codemsg['code'] = codeInfo.get('data')['code']
                        codemsg['msg'] = codeInfo['msg']
                        return HttpResponse(json.dumps(content), content_type='application/json')
                    else:
                        return HttpResponse(json.dumps(content), content_type='application/json')
                elif channel == 'prod':
                    codeInfo = getCodeInfo(platformtype, regionId, channel, mobile)
                    if codeInfo.get('data'):
                        codemsg['code'] = codeInfo.get('data')['code']
                        codemsg['msg'] = codeInfo['msg']
                        return HttpResponse(json.dumps(content), content_type='application/json')
                    else:
                        return HttpResponse(json.dumps(content), content_type='application/json')
                else:
                    return HttpResponse(json.dumps(content), content_type='application/json')
            elif regionId == '1':
                return HttpResponse(json.dumps(content), content_type='application/json')
            else: return HttpResponse(json.dumps(content), content_type='application/json')

# 获取影片列表
def getFilmZH(request):

    if request.method == 'GET':

        filmName = request.GET.get('filmName')
        channel = request.GET.get('channel')
        create_film = Create_film(filmName,channel)

        filmList = create_film.getfilmList()
        syncFilmList = create_film.getSyncFilmList()

        try:
            result = {'code':0,'filmList':filmList['data']['data'],'syncFilmList':syncFilmList['data'],"msg":'success'}
        except:
            result = {'code': 0,"msg":'获取影片列表失败'}
            return JsonResponse(result,content_type='application/json')
        return JsonResponse(result,content_type='application/json')

# 创建影片及补充基础信息
def createBaseInfo(request):

    if request.method == 'POST':
        json_str = request.body
        json_data = json.loads(json_str)
        channel = json_data['channel']
        filmName = json_data['filmName']

        create_film = Create_film(filmName, channel)
        result = create_film.create_film_baseInfo()
        filmId = result['data']['filmId']
        create_film.saveFilmCast(filmId)
        create_film.saveAddVideoInfo(filmId)
        create_film.saveAddImgInfo(filmId)

        return JsonResponse(result, content_type='application/json')

# 创建影片
def createSyncFilm(request):

    if request.method == 'POST':
        json_str = request.body
        json_data = json.loads(json_str)
        filmId = json_data['filmId']
        filmName = json_data['filmName']
        channel = json_data['channel']
        filmTime = json_data['filmTime']
        filmTime[0] = int(filmTime[0]/1000)
        filmTime[1] = int(filmTime[1]/1000)

        create_film = Create_film(filmName, channel)

        # 依据获取的filmId获取影片名
        filmList = create_film.getfilmList()
        for filminfo in filmList['data']['data']:
            if str(filminfo['filmId']) == str(filmId):
                filmName = filminfo['filmName']
                break
        print("filmName",filmName)
        create_film.addSpu(filmId, filmName, filmTime[0], filmTime[1])
        print("filmId",filmId)

        # 获取影片相关SPU信息
        spuInfo = {}
        spu_list = create_film.getSpuList()
        for spu_info in spu_list['data']['list']:
            if str(spu_info['filmId']) == str(filmId):
                spuInfo = spu_info
                break

        positiveTitleValue = create_film.getfilmDate(filmId)['data'][0]['positive'][0]['value']
        create_film.addGoodsSku(filmId,spuInfo['spuId'],spuInfo['spuName'],positiveTitleValue,filmTime[0],filmTime[1])
        skuId = create_film.getSkuList(spuInfo['spuId'])['data']['list'][0]['skuId']
        create_film.bindupdateGroup(skuId)
        create_film.updateEnvironment(skuId)
        create_film.updateGoodsStatus(skuId,filmId)
        result = create_film.cmsReleaseFilm(filmId)

        return JsonResponse(result,content_type='application/json')

# 添加首映礼
def createPremiere(request):

    if request.method == 'GET':
        channel = request.GET.get('channel')
        create_premiere = Premiere(channel)
        spu_list = create_premiere.getSpuLists()

        result = {'code': 0, 'spuList': spu_list['data'], "msg": 'success'}

        return JsonResponse(result, content_type='application/json')

    if request.method == 'POST':
        json_str = request.body
        json_data = json.loads(json_str)
        channel = json_data['channel']
        premiereName = json_data['premiereName']
        beignTime = json_data['beignTime']
        interactionType = json_data['interactionType']
        beautifyStatus = json_data['beautifyStatus']
        remark = json_data['remark']
        filmId = json_data['spuinfo']


        create_premiere = Premiere(channel)

        spu_list = create_premiere.getSpuLists()
        for spu_info in spu_list['data']:
            if spu_info['filmId'] == filmId:
                spuinfo = spu_info
                break
        if spuinfo is None:
            result = {'code': 200, "msg": '无法匹配filmId，请重新创建'}
            return JsonResponse(result, content_type='application/json')

        premiere_info = create_premiere.premiere_create(spuinfo['filmId'],spuinfo['filmName'],spuinfo['spuId'],
                                                        spuinfo['spuReleaseStartTime'],spuinfo['spuReleaseEndTime'],
                                                        beignTime,premiereName,beautifyStatus,interactionType,remark)
        # if '获取影片正片信息为空' in premiere_info['msg']:
        #     result = {'code': 200, "msg": '获取影片正片信息为空，请重新创建'}
        #     return JsonResponse(result, content_type='application/json')
        create_premiere.sort_user(premiere_info['data']['id'])
        create_premiere.addCompere(premiere_info['data']['id'])
        create_premiere.saveImg(premiere_info['data']['id'])
        create_premiere.program_info(premiere_info['data']['id'])
        create_premiere.activity_shareType(premiere_info['data']['id'])
        create_premiere.interaction_methods(premiere_info['data']['id'])
        premiere_list = create_premiere.getPremiereList()['data']['list']
        for premiere in premiere_list:
            if premiere['roomId'] == premiere_info['data']['id']:
                create_premiere_skuId = premiere['skuId']

        if create_premiere_skuId is None:
            result = {'code': 200, "msg": '无法匹配skuId，请重新创建'}
            return JsonResponse(result, content_type='application/json')

        positive_info = create_premiere.getPositiveInfo(create_premiere_skuId)['data']
        updataPremiere = create_premiere.updataPremiere(spuinfo['filmId'],spuinfo['filmName'],spuinfo['spuId'],
                                create_premiere_skuId,positive_info['goods']['productId'],
                                positive_info['goods']['positiveTitleValue'],spuinfo['spuReleaseStartTime'],spuinfo['spuReleaseEndTime'])

        create_film = Create_film(spuinfo['filmName'],channel)
        create_film.bindupdateGroup(create_premiere_skuId)
        create_film.updateEnvironment(create_premiere_skuId)
        create_film.updateGoodsStatus(create_premiere_skuId,spuinfo['filmId'])

        result = create_premiere.releasePremiere(premiere_info['data']['id'])

        return JsonResponse(result, content_type='application/json')

# 添加专场
def createSpecial(request):

    if request.method == 'GET':
        channel = request.GET.get('channel')
        create_special = Special(channel)
        spu_list = create_special.getSpuLists()
        guest_user_list = create_special.getGuestUser()

        result = {'code': 0, 'spuList': spu_list['data'],'userGuestList': guest_user_list['data'], "msg": 'success'}

        return JsonResponse(result, content_type='application/json')

    if request.method == 'POST':
        json_str = request.body
        json_data = json.loads(json_str)
        channel = json_data['channel']
        specialName = json_data['specialName']
        beignTime = json_data['beignTime']
        interactionType = json_data['interactionType']
        beautifyStatus = json_data['beautifyStatus']
        remark = json_data['remark']
        filmId = json_data['spuinfo']
        userGuestId = json_data['userGuestId']


        create_special = Special(channel)

        spu_list = create_special.getSpuLists()
        for spu_info in spu_list['data']:
            if spu_info['filmId'] == filmId:
                film_info = spu_info
                break
        if film_info is None:
            result = {'code': 200, "msg": '无法匹配filmId，请重新创建'}
            return JsonResponse(result, content_type='application/json')

        guest_user = create_special.getGuestUser()
        for user_g in guest_user['data']:
            if user_g['userId'] == userGuestId:
                userG = user_g
                break
        if userG is None:
            result = {'code': 200, "msg": '无法匹配filmId，请重新创建'}
            return JsonResponse(result, content_type='application/json')

        special_info = create_special.special_create(film_info['filmId'],film_info['filmName'],film_info['spuId'],
                                                     specialName,remark,userG['userId'],userG['nickname'],userG['photo'],
                                                     beignTime,beautifyStatus,interactionType,film_info['spuReleaseStartTime'],
                                                     film_info['spuReleaseEndTime'])
        # if '获取影片正片信息为空' in special_info['msg']:
        #     result = {'code': 200, "msg": '获取影片正片信息为空，请重新创建'}
        #     return JsonResponse(result, content_type='application/json')

        create_special.saveImg(special_info['data']['id'])
        create_special.program_info(special_info['data']['id'])
        create_special.interaction_methods(special_info['data']['id'])
        special_list = create_special.getSpecialList()['data']['list']

        for special in special_list:
            if special['roomId'] == special_info['data']['id']:
                create_special_skuId = special['skuId']

        if create_special_skuId is None:
            result = {'code': 200, "msg": '无法匹配skuId，请重新创建'}
            return JsonResponse(result, content_type='application/json')

        positive_info = create_special.getPositiveInfo(create_special_skuId)['data']
        updataSpecial = create_special.updateSpecial(film_info['spuId'],film_info['filmId'],film_info['filmName'],
                                positive_info['goods']['productId'],create_special_skuId,
                                positive_info['goods']['positiveTitleValue'],film_info['spuReleaseStartTime'],film_info['spuReleaseEndTime'])

        create_film = Create_film(film_info['filmName'],channel)
        create_film.bindupdateGroup(create_special_skuId)
        create_film.updateEnvironment(create_special_skuId)

        create_film.updateGoodsStatus(create_special_skuId,film_info['filmId'])

        result = create_special.releaseSpecial(special_info['data']['id'])

        return JsonResponse(result, content_type='application/json')



# Create your views here.
